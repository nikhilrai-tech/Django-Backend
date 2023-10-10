from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from . models import Student,School,User
class SchoolSignupView(APIView):
    def post(self, request):
        name = request.data['name']
        email = request.data['email']
        city = request.data['city']
        pin_code = request.data['pin_code']
        password = request.data['password']
        user = User.objects.create_user(username=email, email=email, password=password, user_type='SCH')
        school = School.objects.create(name=name, city=city, pin_code=pin_code)
        user.school = school
        user.save()
        return Response({'message': 'School created successfully.'})

class StudentBulkUploadView(APIView):
    def post(self, request):
        grade = request.data['grade']
        students = request.data['students']
        for student in students:
            name = student['name']
            username = student['username']
            password = student['password']
            Student.objects.create(name=name, username=username, grade=grade, school=request.user.school)
        return Response({'message': 'Students uploaded successfully.'})

class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.filter(school=request.user.school)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

class StudentFilterView(APIView):
    def get(self, request):
        grade = request.query_params.get('grade')
        students = Student.objects.filter(school=request.user.school, grade=grade)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

class StudentUpdateView(APIView):
    def put(self, request, pk):
        student = Student.objects.get(pk=pk)
        name = request.data['name']
        password = request.data['password']
        student.name = name
        student.password = password
        student.save()
        return Response({'message': 'Student updated successfully.'})