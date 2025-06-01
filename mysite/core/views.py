from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
# from django.http import HttpResponse

# def home(request):
#     name="sahad"
#     return HttpResponse(f"Hello, {name}! You're viewing your first page.")
def home_view(request):
    return render(request, 'core/home.html')

def register_view(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request,'core/register.html',{'form':form})

def login_view(request):
    return render(request, 'core/login.html')

