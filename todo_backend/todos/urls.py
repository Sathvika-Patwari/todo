from django.urls import path
from .views import TodoListCreate, TodoRetrieveUpdateDestroy, TodoUpdate

urlpatterns = [
    path('todos/', TodoListCreate.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', TodoRetrieveUpdateDestroy.as_view(), name='todo-retrieve-update-destroy'),
    path('todos/update/<int:pk>/', TodoUpdate.as_view(), name='todo-update'),
]
