from ..serializers import EmployeeSerializer
from rest_framework import mixins, generics
from employees.models import Employee


from ..serializers import EmployeeSerializer       # Import the serializer for Employee
from rest_framework import mixins, generics        # Import DRF mixins and base class
from employees.models import Employee              # Import the Employee model


# This view handles listing all employees (GET)
# and creating a new employee (POST)
class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    
    queryset = Employee.objects.all()              # Get all employee records
    serializer_class = EmployeeSerializer          # Use this serializer for data conversion

    # Handle GET request → return all employees
    def get(self, request):
        return self.list(request)                  # Call list() from ListModelMixin

    # Handle POST request → create a new employee
    def put(self, request):
        return self.create(request)                # Call create() from CreateModelMixin

class EmployeeDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView, ):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def post (self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(self, request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)