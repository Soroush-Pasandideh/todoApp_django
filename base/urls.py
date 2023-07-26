from django.urls import path
from .views import TaskListView, TaskDetailView, TaskCreateView

urlpatterns = [
    path('', TaskListView.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task'),
    path('task-create/', TaskCreateView.as_view(), name='task-create'),
]
