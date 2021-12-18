from django.urls import path
from .views import TaskList, TaskDetail, CreateTask, UpdateTask, DeleteTask

urlpatterns = [
    path("", TaskList.as_view(), name="tasks"),
    path("task/<int:pk>/", TaskDetail.as_view(), name="taskDetail"),
    path("create-task/", CreateTask.as_view(), name="createTask"),
    path("update-task/<int:pk>", UpdateTask.as_view(), name="updateTask"),
    path("delete-task/<int:pk>", DeleteTask.as_view(), name="deleteTask"),
]
