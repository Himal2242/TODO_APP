from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializer import Task_Serializer, Task_detail_serializer  # Create this serializer in serializers.py
from rest_framework.decorators import *


class Task_List(APIView):
    
    def get(self, request):
        try:
            try:
                task = Task.objects.all().order_by("-id")
            except Task.DoesNotExist :
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = Task_Serializer(task, many=True)
            return Response(serializer.data)
        except Exception as error :
            print(error)
            return Response({"Error":f"{error}"}, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request):
        try:
            serializer = Task_Serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)
        except Exception as error :
            print(error)
            return Response({"Error":f"{error}"}, status=status.HTTP_400_BAD_REQUEST)
        
class Task_Detail(APIView):
    
    # def get(self,request, task_id):
    #     try:
    #         try:
    #             task = Task.objects.get(id = task_id)
    #         except Task.DoesNotExist :
    #             return Response(status=status.HTTP_400_BAD_REQUEST)
    #         serializer = Task_Serializer(task, many=False)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     except Exception as error :
    #         return Response({"error":f"{error}"}, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, task_id):
        try:
            try:
                task = Task.objects.get(id=task_id)
            except Task.DoesNotExist :
                return Response(status=status.HTTP_400_BAD_REQUEST)
            serializer = Task_Serializer(task, data=request.data , partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'data':'success'}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
        except Exception as error :
            print(error)
            return Response({"Error":f"{error}"}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, task_id):
        try:
            try :
                task = Task.objects.get(id=task_id)
            except Task.DoesNotExist:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            task.delete()
            return Response({"success":"data successfully deleted"}, status=status.HTTP_200_OK)
        except Exception as error :
            print(error)
            return Response({"Error":f"{error}"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PATCH"])        
def task_done_undone(request, task_id):
    try:
        try:
            task = Task.objects.get(pk=task_id)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        print(task)
        task.completed = not task.completed
        task.save()
        return Response(status=status.HTTP_200_OK)
    except Exception as error :
        print(error)
        return Response(status=status.HTTP_400_BAD_REQUEST)