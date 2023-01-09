from tkinter.messagebox import RETRY
from API.models import Word
from API.serializers import WordSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from difflib import SequenceMatcher

import eng_to_ipa as p

@api_view(['GET'])
def GetAllWordsView(request):
    AllUsers = Word.objects.all()
    serializer_class = WordSerializer(AllUsers, many=True)
    return Response({"data":serializer_class.data}, status=status.HTTP_200_OK)




import speech_recognition as sr
import sys
import eng_to_ipa as p
from difflib import SequenceMatcher
import os

def score(say, path):
    # say = 'library'
    r = sr.Recognizer()

    # Local voice testing
    # aud_fil = sr.AudioFile(sys.path[0]+'/library.wav')
    aud_fil = sr.AudioFile(path)
    with aud_fil as source:
        # Denoising
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.record(source)

    # speech recognition
    test = r.recognize_google(audio, language="en-IN", show_all=True)
    print(test)

    # Analysis of Speech
    flag = False
    if say in test['alternative'][0]['transcript']:
        return test['alternative'][0]['confidence']

    else:
        a = p.convert(say)
        b = p.convert(test['alternative'][0]['transcript'])
        score = SequenceMatcher(a=a, b=b).ratio()
        return score

    #print(flag)


f = open(sys.path[0]+'\documents\\'+"words.txt", "r")
listOfWords = f.readlines()
listOfWords = [x[:len(x)-1] for x in listOfWords]
import random 

@api_view(['POST'])
def CreateWordView(request):

    ReqData = request.data

    try:
        # ReqData["score"] = str(scoringFunction("hello", ReqData["pronunciation"]))
        ReqData["word"] = random.choice(listOfWords)
        ReqData["correctPhonetics"] = p.convert(ReqData["word"])
        serializers = WordSerializer(data=ReqData)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        print(err)
        return Response(serializers.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def GeWordByIDView(request):
    # Getting UserId in uuid (Queru Param ?word_id=)
    word_id = request.query_params.get('word_id')
    # If UserId is not provided
    if word_id is None:
        return Response({"data": "Word Id Not Provided"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        UserData = Word.objects.get(word_id=word_id)
        print(UserData.word)
        # # filePath = sys.path[0]+'\\documents\\' + UserData.word + '.wav'
        # path = str(UserData.word_id) + str(UserData.wordUser)
        # path = ''.join([x for x in path if x not in '-@.'])
        filePath = 'C:/Users/zubia/Documents/GitHub/G4-geeks/documents/new.wav'
        # filePath = 'C:/Users/zubia/Documents/GitHub/G4-geeks/documents/' + path +'.wav'
        UserData.score = str(score(UserData.word, filePath))
        serializer = WordSerializer(UserData, many=False)
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)

        return Response(str(err), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def GetWordView(request):
    # Getting UserId in uuid (Queru Param ?word_id=)
    word_id = request.query_params.get('word_id')
    # If UserId is not provided
    print("------->",word_id)
    if word_id is None:
        return Response({"data": "Word Id Not Provided"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        UserData = Word.objects.get(word_id=word_id)  
        data = {"data":UserData.word}
        return Response(data, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)
        return Response(str(err), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        