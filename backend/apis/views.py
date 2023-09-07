from .models import *
from .serializers import *
from rest_framework import viewsets

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Note instances.
    """
    serializer_class = StudentSerializer
    queryset = Student.objects.all()