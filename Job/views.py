from django.http.response import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *

def add_circular(request): 
   circular_Form = CircularForm()
   if request.method == "POST":
         circular_Form = CircularForm(request.POST,  request.FILES)
         if circular_Form.is_valid():
               circular_Form.save() 
   return render(request, 'Add_circular.html',{"C_form": circular_Form})


def Circular(request): 
   Circular_Add = Circular.objects.all()
   context ={
      "Circular_add": Circular_Add
    }
   return render(request, 'View_circular.html')


def Add_Applyparticipent(request): 
   applyparticipent_Form = ApplyparticipentForm()
   if request.method == "POST":
         applyparticipent_Form = ApplyparticipentForm(request.POST,  request.FILES)
         if applyparticipent_Form.is_valid():
               applyparticipent_Form.save() 
   return render(request, 'Add_participant.html',{"A_form": applyparticipent_Form})


def Applyparticipent(request): 
   Applyparticipent_Add = Applyparticipent.objects.all()
   context ={
      "Applyparticipent_add": Applyparticipent_Add
    }
   return render(request, 'View_participant.html')





   