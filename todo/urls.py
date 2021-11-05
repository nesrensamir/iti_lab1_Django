from django.contrib import admin
from django.urls import path, include
from .views import index, todo_list, todo_update, todo_delete
urlpatterns = [
    path('', index, name='todo-index'),
    path('list', todo_list, name='todo-list'),
    path('task/<int:task_id>/update', todo_update, name='todo-update'),
    path('task/<int:task_id>/delete', todo_delete, name='todo-delete'),
]