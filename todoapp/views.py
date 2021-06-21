from django.shortcuts import render,redirect
from todoapp.forms import TodoCreateForm
from todoapp.models import Todos
from .forms import UserRegistrationForm,LoginForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    return render(request,"index.html")
def create_todo(request):

    if request.method=="GET":

        form=TodoCreateForm()
        context={}
        context["form"]=form
        return render(request, 'createtodo.html',context)
    elif request.method=="POST":
        form=TodoCreateForm(request.POST)
        if form.is_valid():
            taskname=form.cleaned_data.get("task_name")
            user=form.cleaned_data.get("user")
            status=form.cleaned_data.get("status")
            todo=Todos(task_name=taskname,status=status,user=user)
            todo.save()
            return render(request, 'index.html')
def list_all_todos(request):
    todos=Todos.objects.all()
    context={}
    context["todos"]=todos
    return render(request,"listalltodos.html",context)
def update_todo(request,id):
    todo=Todos.objects.get(id=id)
    instance={
        "task_name":todo.task_name,
        "user":todo.user,
        "status":todo.status
    }
    form=TodoCreateForm(initial=instance)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=TodoCreateForm(request.POST)
        if form.is_valid():
            task_name=form.cleaned_data.get("task_name")
            user=form.cleaned_data.get("user")
            status=form.cleaned_data.get("status")
            todo.task_name=task_name
            todo.user=user
            todo.status=status
            todo.save()
            return redirect("home")



    return render(request,"edittodo.html",context)


def delete_todo(request,id):
    todo=Todos.objects.get(id=id)
    todo.delete()
    return redirect("listalltodos")
def registration(request,*args,**kwargs):
    form=UserRegistrationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            context["form"]=form

    return render(request,"registration.html",context)
def login_view(request,*args,**kwargs):
    form=LoginForm
    context={}
    context["form"]=form
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                print("login success")
                login(request,user)
                return render(request,"index.html")
            else:
                print("failed")
                context["form"]=form
    return render(request,"login.html",context)
def signout(request,*args,**kwargs):
    logout(request)
    return redirect("login")