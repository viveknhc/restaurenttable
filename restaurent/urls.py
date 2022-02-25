from django.urls import path
from . import views
urlpatterns=[
    path('master2',views.masterfn,name='master2'),
    path('front',views.frfn,name='front'),
    path('table',views.tabfn,name='table'),
    path('menue',views.menuefn,name='menue'),
    path('comment',views.commentfn,name='comment'),
    path('payment',views.paymentfn,name='payment'),
    path('order',views.orderfn,name='order'),
    path('newmenu',views.newmenufn,name='newmenu'),
    path('updatetable',views.updatetablefn,name='updatetable'),
    path('viewtable',views.viewtablefn,name='viewtable'),
    path('profile',views.profilefn,name='profile'),
    
    
]