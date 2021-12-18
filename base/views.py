from django.http.response import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import Task


class TaskList(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "base/tasks.html"


class TaskDetail(DetailView):
    model = Task
    context_object_name = "task"
    template_name = "base/task.html"


class CreateTask(CreateView):
    model = Task
    context_object_name = "createTask"
    template_name = "base/createTask.html"
    fields = "__all__"
    success_url = reverse_lazy("tasks")


class UpdateTask(UpdateView):
    model = Task
    context_object_name = "updateTask"
    template_name = "base/updateTask.html"
    fields = "__all__"
    success_url = reverse_lazy("tasks")


class DeleteTask(DeleteView):
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy("tasks")
