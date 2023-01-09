from django.urls import path
from API.views import UserView, WordView, LoginView

urlpatterns = [
    # ======== Users Enpoints =======
    path("get-all-users", UserView.GetAllUsersView, name="GetAllUsers"),
    path("get-user-by-id", UserView.GeUserByIDView, name="GetUserByID"),
    path("create-user", UserView.CreateUserView, name="CreateUser"),
    path("update-user", UserView.UpdateUserView, name="UpdateUser"),
    path("delete-user", UserView.DeleteUserView, name="DeleteUser"),

    # ========= Login =========
    path("login", LoginView.LoginVieww.as_view(), name="LoginApi"),
    path('register', LoginView.RegisterView, name='Register'),

    # ======== Word Endpoints ========
    path("create-word-view", WordView.CreateWordView, name="CreateWord"),
    path("get-all-words", WordView.GetAllWordsView, name="GetAllWords"),
    path("get-word-by-id", WordView.GeWordByIDView, name="GetWordById"),
    path("get-word", WordView.GetWordView, name="GetWord"),
]