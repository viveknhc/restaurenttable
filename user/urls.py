from django.urls import path
from . import views
urlpatterns=[
    path('master',views.mfn,name='master'),
    path('home',views.hfn,name='home'),
    path('aboutus',views.aboutfn,name='aboutus'),
    path('resto',views.resfn,name='resto'),
    path('paragon',views.paragonfn,name='paragon'),
    path('register',views.regfn,name='register'),
    
]