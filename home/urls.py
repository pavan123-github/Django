
from django.urls import path,include
from .import views 
urlpatterns = [
    path('',views.index, name='index'),
    path('addtrainer',views.addtrainer, name='addtrainer'),
    path('addstudent', views.addstudent, name='addstudent'),
    path('updatetrainer', views.updatetrainer, name='updatetrainer'),
    path('updatestudent', views.updatestudent, name='updatestudent'),
    path('deletetr',views.deletetr, name='deletetr'),
    path('deletestudent', views.deletestudent, name='deletestudent')
]





