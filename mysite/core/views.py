from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse

# def home(request):
#     name="sahad"
#     return HttpResponse(f"Hello, {name}! You're viewing your first page.")
def home(request):
    return render(request, 'core/home.html')