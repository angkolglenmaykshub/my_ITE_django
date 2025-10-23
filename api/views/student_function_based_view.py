from django.shortcuts import render
from students.models import Students
from api.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# =====================================
# Main student view handling all students
# Supports GET, POST, PUT, DELETE requests
# =====================================

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def studentView(request):
    # ---------- GET: Retrieve all student records ----------
    if request.method == 'GET':
        # Fetch all student records from the database
        students = Students.objects.all()
        # Serialize the data into JSON format
        serializer = StudentSerializer(students, many=True)
        # Print for debugging (optional)
        print(students, serializer.data)
        # Return serialized data with HTTP 200 (OK)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # ---------- POST: Create a new student record ----------
    if request.method == 'POST':
        # Deserialize request data
        serializer = StudentSerializer(data=request.data)
        # Validate incoming data
        if serializer.is_valid():
            # Save the new student record to the database
            serializer.save()
            # Return created student data with HTTP 201 (Created)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # If invalid, print and return errors with HTTP 400 (Bad Request)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # ---------- PUT: Update an existing student ----------
    if request.method == 'PUT':
        # Extract the student's ID from request data
        id = request.data.get('id')
        try:
            # Find the student by ID
            student = Students.objects.get(id=id)
        except Students.DoesNotExist:
            # Return 404 if student not found
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # Serialize the existing student with new data
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            # Save the updated student
            serializer.save()
            # Return updated data with HTTP 200 (OK)
            return Response(serializer.data, status=status.HTTP_200_OK)
        # If validation fails, print and return errors
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # ---------- DELETE: Remove a student record ----------
    if request.method == 'DELETE':
        # Extract ID from request data
        id = request.data.get('id')
        try:
            # Find the student by ID
            student = Students.objects.get(id=id)
        except Students.DoesNotExist:
            # Return 404 if not found
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # Delete the student record
        student.delete()
        # Return confirmation message with HTTP 204 (No Content)
        return Response({'message': 'Student deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


# =====================================
# Single student view
# Handles operations for a specific student
# Supports GET, PUT, DELETE requests
# =====================================

@api_view(['GET', 'PUT', 'DELETE'])
def student(request, student_id):
    # Try to fetch the student by the given ID (from URL)
    try:
        student = Students.objects.get(id=student_id)
    except Students.DoesNotExist:
        # Return 404 if student not found
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # ---------- GET: Retrieve specific student ----------
    if request.method == 'GET':
        # Serialize the single student object
        serializer = StudentSerializer(student)
        # Return the serialized data
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # ---------- PUT: Update specific student ----------
    elif request.method == 'PUT':
        # Deserialize and validate incoming data
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            # Save updated student
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # Return validation errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # ---------- DELETE: Delete specific student ----------
    elif request.method == 'DELETE':
        # Delete the student record
        student.delete()
        # Return HTTP 204 (No Content)
        return Response(status=status.HTTP_204_NO_CONTENT)
