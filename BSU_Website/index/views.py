from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage(request):
    return render(request,"index.html")
def actionpage(request):
    return render(request,"action.html")
def blmpage(request):
    return render(request,"blm.html")
def leaderspage(request):
    return render(request,"leaders.html")
def racismpage(request):
    return render(request,"racism.html")