from django.shortcuts import render, redirect
from .forms import StudentRegistration
from .models import User

# def insert_print(request):
#     if request.method == 'POST':
#         fm = StudentRegistration(request.POST)
#         if fm.is_valid:
#             fm.save()
#             fm = StudentRegistration()
#     else:
#         fm = StudentRegistration()
        
#     return render(request, "enroll/insertandprint.html", {'form':fm})


def insert_print(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            aa = fm.cleaned_data['name']
            bb = fm.cleaned_data['email']
            cc = fm.cleaned_data['password']
            reg = User(name=aa,email=bb,password=cc)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, "enroll/insertandprint.html", {'form':fm, 'stu':stud})

def delete_record(request, id):
    if request.method == 'POST':
        result = User.objects.get(pk=id)
        result.delete()
    return redirect("insertprint")

def edit(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:  
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, "enroll/edit.html", {'form':fm})

