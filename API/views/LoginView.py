# from API.serializers import MyTokenObtainPairSerializer
from logging import exception
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from API.serializers import RegisterSerializer
from rest_framework import generics
import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
#from rest_framework.exceptions import Exception
from API.models import UserModell
from rest_framework.decorators import api_view
import jwt
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
# from API.models import ServiceProvider
from Exceptions.ExceptionsClass import LoginException

@api_view(['POST'])
def RegisterView(request):
    ReqData = request.data
    try:
        email = request.data['email']
        user = UserModell.objects.filter(email=email).first()
        if user is not None:
            return Response("Email/Phone Already Exists",status=status.HTTP_400_BAD_REQUEST)
        ReqData['password'] = make_password(request.data['password'])
        serializers = RegisterSerializer(data=ReqData)
        if serializers.is_valid():
            serializers.save()
            payload = {
                # 'id':str(serializers.userId),
                'exp':datetime.datetime.utcnow()+datetime.timedelta(hours=10),
                'iat':datetime.datetime.utcnow()
            }

            token = jwt.encode(payload, 'secret', algorithm='HS256')
            print(token)
            return Response({"data":serializers.data, "token":token},status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        print(err)
        return Response(str(err), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LoginVieww(APIView):
    def post(self, request):
        try:
            email = request.data['email']
            password = request.data['password']
            userType = ''
            if 'userType' in request.data.keys():
                userType = request.data['userType']

            # if userType == 'serviceProvider':
            #     user = UserModell.objects.filter(email=email).first()
            #     if user is None:
            #         raise LoginException("Service Provider not Found")
            # else:
            user = UserModell.objects.filter(email=email).first()
            if user is None:
                raise LoginException("User not Found")
            
            if not check_password(password, user.password):
                raise LoginException("Incorrect Password")

            payload = {
                'id':str(user.userId),
                'exp':datetime.datetime.utcnow()+datetime.timedelta(hours=1),
                'iat':datetime.datetime.utcnow()
            }

            token = jwt.encode(payload, 'secret', algorithm='HS256')
            
            data = {
                'token':token,
                'email':email,
                'firstName':user.firstName,
                'lastName':user.lastName,
                'userId':str(user.userId)
            }

            return Response({"data":data}, status = status.HTTP_200_OK)
        except LoginException as err:
            return Response(str(err), status = status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        except Exception as err:
            print("Error: " + str(err))
            return Response(str(err), status = status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def CheckTokenView(request):
    token = request.query_params.get('token')
    decodedToken = jwt.decode(token, "secret", algorithms=["HS256"])
    return Response({"data":decodedToken}, status = status.HTTP_200_OK)