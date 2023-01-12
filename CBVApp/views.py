from django.shortcuts import render
from CBVApp.models import Course,CourseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import mixins,generics
# Create your views here.

# Below method same work but used Mixin and generics
class CourseListView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)    


class CourseDetailView(generics.GenericAPIView,mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,mixins.DestroyModelMixin):
        queryset = Course.objects.all()
        serializer_class = CourseSerializer

        def get(self,request,pk):
           return self.retrieve(request,pk)

        def put(self,request,pk):
           return self.update(request,pk)

        def delete(self,request,pk):
          return self.destroy(request,pk)    




# Below method same work but used Class based view
'''
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

class CourseDetailView(APIView):
    def get_course(Self,pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404  

    def get(self,pk):
        course = self.get_course(pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    def put(self,request,pk):
        course  = self.get_course(pk)
        courseSerializer = CourseSerializer(course,data = request.data)
        if courseSerializer.is_valid():
            courseSerializer.save()
            return Response(courseSerializer.data,status = status.HTTP_201_CREATED)
        return Response(courseSerializer.errors)        
    def delete(self,pk):
        course = self.get_course(pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   '''
