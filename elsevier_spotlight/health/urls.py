
from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.health,name='health'),
    # path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail, name='post_detail'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('dislike/<int:post_id>/', views.dislike_post, name='dislike_post'),
]
