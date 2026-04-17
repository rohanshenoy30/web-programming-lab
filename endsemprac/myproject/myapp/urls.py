from django.urls import path,include
from . import views
urlpatterns=[

path("",views.index,name="index"),
path("second/",views.second,name="second"),
path("third/",views.third,name="third"),
path("fourth/",views.fourth,name="fourth")
]