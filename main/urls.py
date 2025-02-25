from django.urls import path 
from .views import home_page 
from .import views 

urlpatterns = [
        path("",home_page,name="home"),
        path('/about',views.about_page,name="about"),
        path('/serv',views.serv_page,name="serv"),
        path("/blog",views.blog_page,name="blog"),
        path("/contract",views.contract,name="contact")
        ]
