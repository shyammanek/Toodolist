from django.shortcuts import render, redirect
from todo_app.models import *
from .form import todoform, CreateUserForm,DocumentForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
#from django.contrib.admin import ModelAdmin
#from django.core.files.storage import FileSystemStorage
#from django.conf import settings



@login_required(login_url='login')
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('views')
    else:
        form = DocumentForm()
    return render(request, 'uplodIMG.html', {
        'form': form
    })


def regPage(request):
    if request.user.is_authenticated:
        return redirect('views')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account Was Created for'+user)

                return redirect('login')

        context = {'form':form}
        return render(request,'register.html',context)

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('views')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)

            if user is not None:
                #email = request.POST.get('email')
                login(request,user)
                return redirect('views')
            else:
                messages.info(request,"Username OR Password incorrect")
                return render(request,'login.html')

        context ={}
        return render(request,'login.html',context)

def logoutuser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def tododata(request):
    if request.method == "POST":
        form = todoform(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ("New Task Added !"))
        return redirect('views')
    else:
        all_task = todolist.objects.all
        return render(request, 'view.html', {'all_task': all_task})

@login_required(login_url='login')
def delete_task(request, task_id):
    task = todolist.objects.get(pk=task_id)
    task.delete()
    return redirect('views')

@login_required(login_url='login')
def pending_task(request, task_id):
    task = todolist.objects.get(pk=task_id)
    task.done = False
    task.save()
    return redirect('views')

@login_required(login_url='login')
def complate_task(request, task_id):
    task = todolist.objects.get(pk=task_id)
    task.done = True
    task.save()
    return redirect('views')

@login_required(login_url='login')
def edit_task(request,task_id):
    if request.method == "POST":
        task_update = todolist.objects.get(pk=task_id)
        form = todoform(request.POST or None, instance = task_update)
        if form.is_valid():
            form.save()
        messages.success(request, ("Task Edited !"))
        return redirect('views')
    else:
        task_ed = todolist.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_ed': task_ed})
