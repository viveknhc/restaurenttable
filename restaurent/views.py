from django.shortcuts import render

# Create your views here.
def frfn(request):
    return render(request,"front.html")
def tabfn(request):
    return render(request,"addtable.html")
def masterfn(request):
    return render(request,"master2.html")
def menuefn(request):
    return render(request,"menue.html")
def commentfn(request):
    return render(request,"comment.html")
def paymentfn(request):
    return render(request,"payment.html")
def orderfn(request):
    return render(request,"order.html")