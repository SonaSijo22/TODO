from django.shortcuts import render, redirect

from .models import Task

from .forms import TaskForm

from django.views import View

from task.forms import RegistrationForm,LoginForm,TaskForm

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate,login,logout

# Create your views here.

# Registration view
# -----------------------
class SignUpView(View):

  def get(self,request,*args, **kwargs):

    form=RegistrationForm()

    return render(request,'register.html',{'form':form})

  def post(self,request,*args, **kwargs):

    form=RegistrationForm(request.POST)

    if form.is_valid():

      form.save()

      return redirect('signin')

    return render(request,'register.html',{'form':form})

# Login View
# -----------
class SignInView(View):

  def get(self,request,*args, **kwargs):

    form=LoginForm()

    return render(request,'login.html',{'form':form})

  def post(self,request,*args, **kwargs):

    form=LoginForm(request.POST)

    if form.is_valid():

      uname=form.cleaned_data.get('username')

      pwd=form.cleaned_data.get('password')

      user_object=authenticate(request,username=uname,password=pwd)

      if user_object:

        login(request,user_object)

        return redirect('task-list')

    return render(request,'login.html',{'form':form})

# list and add
# ----------

class TaskcreateView(View):

    def get(self,request,*args, **kwargs):

        qs=Task.objects.filter(user_object=request.user)

        form = TaskForm()

        return render(request, "task_list.html", {'form':form,'data':qs})

    def post(self,request,*args, **kwargs):

        form = TaskForm(request.POST)
   
        if form.is_valid():

            form.instance.user_object=request.user

            form.save()
            
            return redirect("task-list")
    
        return render(request, "task_list.html", {'form':form})

# update
# ---------

class TaskupdateView(View):
    
    def get(self,request,*args, **kwargs):

        id=kwargs.get('pk')

        task = Task.objects.get(id=id)

        form = TaskForm(instance=task)

        return render(request, "task_list.html", {'form':form})

    def post(self,request,*args, **kwargs):

        id=kwargs.get('pk')

        task = Task.objects.get(id=id)

        form = TaskForm(request.POST,instance=task)

        if form.is_valid():

            form.save()

            return redirect("task-list")
            
        return render(request, "task_list.html", {'form':form})

# delete
# ----------

class TaskdeleteView(View):

    def get(self,request,*args, **kwargs):

        id=kwargs.get('pk')

        qs= Task.objects.get(id=id).delete()

        return redirect("task-list")
