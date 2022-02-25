from django.shortcuts import render

# Create your views here.

def haafn(request):
    return render(request,"h.html")
def mast1fn(request):
    return render(request,"master1.html")
def addrfn(request):
    return render(request,"addrest.html")
def dafn(request):
    return render(request,"dashboard.html")
def viewfn(request):
    return render(request,"viewrest.html")
def viewusfn(request):
    return render(request,"viewuser.html")
def reqfn(request):
    return render(request,"request.html")
def rafn(request):
    return render(request,"reviewrating.html")
def gotofn(request):
    return render(request,"goto.html")