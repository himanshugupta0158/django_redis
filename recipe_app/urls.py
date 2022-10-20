from django.urls import path
from .views import *

urlpatterns = [
    
    path('',home, name="home"),
    path("<int:id>", show, name="shoe"),

]
