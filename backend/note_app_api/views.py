from rest_framework.views import APIView
from . import serializer
from . import models
from rest_framework.response import Response


class todo_api_view(APIView):
    try:
        def get(self, request, format=None):
            tasks = models.Task.objects.all()
            task_serializer = serializer.Task_Serializer(tasks, many=True)
            return Response(task_serializer.data)
    except Exception as error :
        print(error)