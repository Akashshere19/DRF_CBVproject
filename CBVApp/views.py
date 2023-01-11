from django.shortcuts import render
from CBVApp.models import Course,CourseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class CourseListView(APIView):
    def get(self,request):
        courses =  Course.objects.all()
        serializers = CourseSerializer(courses,many=True)
        return Response(serializers.data)


    def post(self,request):
        CourseSerializers = CourseSerializer(data = request.data)
        if CourseSerializers.is_valid():
            CourseSerializers.save()
            return Response(CourseSerializers.data,status = status.HTTP_201_CREATED)

        return Response(CourseSerializers.errors)    

