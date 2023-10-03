from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request,'base.html')
def signup1(request):
    return render(request,'signup.html')
def login1(request):
    return render(request,'login.html')