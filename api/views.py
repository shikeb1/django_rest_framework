from django.shortcuts import render, get_object_or_404
from students.models import Student
from employees.models import Employee
from .serializer import StudentSerializer, EmployeesSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins, generics, viewsets
from blogs.models import Blog, Comments
from blogs.serializers import BlogSerializer, CommentsSerializer
from .pagination import CustomPagination

# =====================================================
# 🔹 STUDENTS — FBV
# =====================================================

@api_view(['GET', 'POST'])
def studentsView(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def studentDetailView(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# # =====================================================
# # 🔹 EMPLOYEES — APIView (CLASS BASED)
# # =====================================================

# class EmployeesAPIView(APIView):

#     def get(self, request):
#         employees = Employee.objects.all()
#         serializer = EmployeesSerializer(employees, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = EmployeesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class EmployeeDetailAPIView(APIView):

#     def get_object(self, pk):
#         try:
#             return Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             return None

#     def get(self, request, pk):
#         employee = self.get_object(pk)
#         if employee is None:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = EmployeesSerializer(employee)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         employee = self.get_object(pk)
#         if employee is None:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#         serializer = EmployeesSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

#     def delete(self, request, pk):
#         employee = self.get_object(pk)
#         if employee is None:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# # =====================================================
# # 🔹 EMPLOYEES — MIXINS
# # =====================================================

# class EmployeesMixinView(mixins.ListModelMixin,
#                          mixins.CreateModelMixin,
#                          generics.GenericAPIView):

#     queryset = Employee.objects.all()
#     serializer_class = EmployeesSerializer

#     def get(self, request):
#         return self.list(request)

#     def post(self, request):
#         return self.create(request)


# class EmployeeDetailMixinView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,
#                               mixins.DestroyModelMixin,
#                               generics.GenericAPIView):

#     queryset = Employee.objects.all()
#     serializer_class = EmployeesSerializer

#     def get(self, request, pk):
#         return self.retrieve(request, pk=pk)

#     def put(self, request, pk):
#         return self.update(request, pk=pk)

#     def delete(self, request, pk):
#         return self.destroy(request, pk=pk)


# =====================================================
# 🔹 EMPLOYEES — GENERIC CBV (🔥 FINAL PART 2:30)
# =====================================================

# class EmployeesView(generics.ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeesSerializer


# class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeesSerializer





class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeesSerializer
    pagination_class = CustomPagination
    filterset_fields = [ 'emp_name', 'emp_position' ]  # 🔥 Add this line to enable filtering by name and position


class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class CommentsView(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Blog.objects.all()
        serializer_class = BlogSerializer
        lookup_field = 'pk'  # 🔥 Ensure this matches the URL parameter name

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
     queryset = Comments.objects.all()
     serializer_class = CommentsSerializer