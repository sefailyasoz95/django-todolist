from django.urls import path
from .views import RegisterPage, TaskList, TaskDetail, CreateTask, UpdateTask, DeleteTask, CustomLogin
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path("login/", CustomLogin.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", RegisterPage.as_view(), name="register"),
    path("", TaskList.as_view(), name="tasks"),
    path("task/<int:pk>/", TaskDetail.as_view(), name="taskDetail"),
    path("create-task/", CreateTask.as_view(), name="createTask"),
    path("update-task/<int:pk>", UpdateTask.as_view(), name="updateTask"),
    path("delete-task/<int:pk>", DeleteTask.as_view(), name="deleteTask"),
]
