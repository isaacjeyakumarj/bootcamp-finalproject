
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('categories/',views.categories,name='categories'),
    path('topblog/',views.topblog,name='topblog'),
    
   
]
