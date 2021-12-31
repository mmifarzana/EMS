from django.contrib.auth import models
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
# Create your views here.

def index(request):
    circular_form = Circular.objects.all().order_by ("-date")
    return render(request, "jobs/job.html", {"Cr_form":circular_form})

def view_circular(request):
    circulars = Circular.objects.first()
    return render(request, "jobs/job_circular.html", {"C":circulars})


def participent_report(request):
    participent_form = Applyparticipent.objects.all()
    return render(request, "jobs/participent_report.html", {"Pr_form":participent_form })


def addreq(request):
    cir_form = CircularForm()
       
    if request.method == "POST":
            cir_form = CircularForm(request.POST)
            if cir_form.is_valid():
                cir_form.save()
                messages.success(request, "New Circular has been created successfully.")
                return redirect('JOBs:Jobs')
    return render(request, "jobs/add_req.html", {"C_form":cir_form})


def edit_job(request, id):
    J = Circular.objects.get(pk=id)
    cir_form = CircularForm(request.POST or None, instance=J)

    if request.method == "POST":
        if cir_form.is_valid():
            cir_form.save()
            messages.success(request, "Hi, your leave updated successfully!")
            redirect('JOBs:Jobs')
    return render(request, "jobs/add_req.html", {"C_form": cir_form})

def delete_job(request, id):
    if request.method == "POST":
        job = Circular.objects.get(pk=id)
        print(job)
        job.delete()
        messages.success(request, "Circular has been deleted successfully.")
        return redirect('JOBs:Jobs')

def addparticipent(request):
    par_form = ApplyparticipentForm()
    if request.method == "POST":
        par_form = ApplyparticipentForm(request.POST, request.FILES)   
        if par_form.is_valid():
            par_form.save()
            messages.success(request, "participent added successfully.")
           # return redirect('JOBs:Jobs')
    return render(request, "jobs/add_participent.html", {"P_form":par_form})
