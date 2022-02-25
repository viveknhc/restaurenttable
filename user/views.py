from django.shortcuts import render

# Create your views here.
def tfn(request):
    return render(request,"test.html")
def mfn(request):
    return render(request,"master.html")
def hfn(request):
    return render(request,"home.html")
def aboutfn(request):
    return render(request,"about us.html")
def resfn(request):
    return render(request,"resto.html")
def paragonfn(request):
    return render(request,"r1.html")
def confn(request):
    return render(request,"contact.html")
def regfn(request):
    return render(request,"register.html")
def resregfn(request):
    return render(request,"resreg.html")

