from rest_framework import viewsets
from .models import Student,Trainer
from .Serializer import StudentSerializer,TrainerSerializer

class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TrainerViewset(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer