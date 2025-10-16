from django.urls import path
from api.views import student_function_based_view
from api.views import employee_function_based_view
from api.views import student_class_based_view

urlpatterns = [
    path('fbv-students/', student_function_based_view.studentView),
    path('fbv-students/<int:student_id>/', student_function_based_view.student),
    path('fbv-employees/', employee_function_based_view.employeeView),
    path('fbv-employees/<int:employee_id>/', employee_function_based_view.employee),

    #cbv part
    path('cbv-students/', student_class_based_view.Student.as_view()),
]
        