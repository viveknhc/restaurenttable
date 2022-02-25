from django.urls import path
from . import views
urlpatterns=[
    path('h',views.haafn,name='h'),
    path('master1',views.mast1fn,name='master1'),
    path('addrest',views.addrfn,name='addrest'),
    path('dashboard',views.dafn,name='dashboard'),
    path('viewrest',views.viewfn,name='viewrest'),
    path('viewuser',views.viewusfn,name='viewuser'),
    path('request',views.reqfn,name='request'),
    path('rating',views.rafn,name='rating'),
    path('goto',views.gotofn,name='goto'),

]