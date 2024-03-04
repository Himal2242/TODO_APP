from django.urls import path
from .views import Task_List, Task_Detail

urlpatterns = [
    path('tasks/',Task_List.as_view(), name='task-list'),
    path('add-task/',Task_List.as_view(), name='add-task'),
    path('task-update/<int:task_id>', Task_Detail.as_view(), name='update the task')
]
