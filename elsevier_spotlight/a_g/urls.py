
from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.a_g,name='a_g'),
    path('<slug:slug>/', views.PostDetail, name='post_detail_ag'),
    
]
