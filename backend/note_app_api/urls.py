from django.urls import path
from .views import Task_List, Task_Detail, task_done_undone


urlpatterns = [
    path('tasks/',Task_List.as_view(), name='task-list'),
    path('add-task/',Task_List.as_view(), name='add-task'),
    path('task-update/<int:task_id>', Task_Detail.as_view(), name='task-update'),
    path('delete-task/<int:task_id>', Task_Detail.as_view(), name="delete-task"),
    path('task-done-undone/<int:task_id>', task_done_undone, name='task-done-undone'),
    # path('get-task/<int:task_id>', Task_Detail.as_view(), name="get-task"),
    
]
