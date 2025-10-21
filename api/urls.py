from django.urls import path
from django.http import HttpResponse
from api.views import employee_class_based_view, student_function_based_view
from api.views import employee_function_based_view
from api.views import student_class_based_view, employee_class_based_view

urlpatterns = [
    path('fbv-students/', student_function_based_view.studentView),
    path('fbv-students/<int:student_id>/', student_function_based_view.student),
    path('fbv-employees/', employee_function_based_view.employeeView),
    path('fbv-employees/<int:employee_id>/', employee_function_based_view.employee),

    #cbv part
    path('cbv-students/', student_class_based_view.Student.as_view()),
    path('cbv-students/<int:pk>/', student_class_based_view.StudentDetail.as_view()),

    path('cbv-employees/', employee_class_based_view.Employees.as_view()),
    path('cbv-employees/<int:pk>/', employee_class_based_view.EmployeeDetail.as_view()),

]
        