from django.shortcuts import render
from CBVApp.models import Course,CourseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response



# Create your views here.







class CourseListView(APIView):
    def get(self,request):
        courses =  Course.objects.all()
        serializers = CourseSerializer(courses,many=True)
        
        return Response(serializers.data)



