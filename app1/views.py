from django.shortcuts import render

# Create your views here.
def bgmi(request):
    return render(request,'bgmi.html')
def virtual(request):
    return render(request,'virtual.html')
