
from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.health,name='health'),
    # path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail, name='post_detail'),
]
