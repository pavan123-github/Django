from django.db import models

class Trainer(models.Model):
    name = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Student(models.Model):
    trainer = models.OneToOneField(Trainer, primary_key=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    branch = models.CharField(max_length=20)
    def __str__(self):
        return self.name
