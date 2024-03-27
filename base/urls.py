from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("blog/",views.blog,name="blog"),
     path("success/",views.success,name="success"),
    path("about/<str:pk>",views.about,name="about"),
    path("post/<str:pk>",views.post,name="post"),
    path("category/",views.category,name="category"),
    path("author/<str:pk>",views.author,name="author"),
]