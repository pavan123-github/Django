from .models import Student,Trainer
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Student
class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name','id']
        model = Trainer
    