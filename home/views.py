from django.shortcuts import render,redirect
from .models import Trainer,Student
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    trainers = Trainer.objects.all()
    students = Student.objects.all()
    return render(request, 'index.html',{'trainers':trainers,'students':students})

def addtrainer(request):
    if request.method=="POST":
        name = request.POST['tname']
        language = request.POST['lang']
        t = Trainer()
        t.name = name
        t.language = language
        t.save()
        send_email(request,'Trainer created',f'{name} Added successfully!',f'{name}')
        messages.success(request,'Trainer Saved Successfully')
        return redirect('/')
    else:
        return redirect('/')

def addstudent(request):
    if request.method=="POST":
        trainer_id = request.POST['trainer']
        name = request.POST['sname']
        branch = request.POST['branch']
        s = Student()
        s.name = name
        s.branch = branch
        student = Student.objects.filter(trainer_id=trainer_id).exists()
        if student == True:
            messages.info(request,'Trainer already exists')
            return redirect('/')
        else:
            s.trainer = Trainer.objects.get(id=trainer_id)
            s.save()
            messages.info(request,'Student saved successfully!')
            return redirect('/')
    else:
        return redirect('/')


def updatetrainer(request):
    if request.method=='POST':
        id = request.POST['id']
        name = request.POST['tname']
        language = request.POST['lang']
        t = Trainer.objects.get(id=id)
        t.name = name
        t.language = language
        t.save()
        messages.success(request,'Trainer update successfully!')
        return redirect('/')
    else:
        return redirect('/')

def updatestudent(request):
    if request.method=="POST":
        tid = request.POST['tid']
        name = request.POST['sname']
        branch = request.POST['branch']
        s = Student.objects.get(trainer_id=tid)
        s.name = name
        s.branch = branch
        s.save()
        messages.success(request,'Student updated successfully!')
        return redirect('/')
    else:
        return redirect('/')

def deletetr(request):
    if request.method=="GET":
        id = request.GET['id']
        t = Trainer.objects.get(id=id)
        t.delete()
        messages.success(request,'Trainer Deleted.')
        return redirect('/')
    else:
        return redirect('/')

def deletestudent(request):
    if request.method:
        tid = request.GET['tid']
        student = Student.objects.get(trainer_id=tid)
        student.delete()
        messages.success(request,'Student Deleted.')
        return redirect('/')
    else:
        return redirect('/')

def send_email(request,subject,message,name):
    email = f'{name}@yopmail.com'
    subject = subject
    message = message
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject,message, email_from, recipient_list)