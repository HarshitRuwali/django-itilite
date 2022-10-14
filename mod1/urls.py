from django.urls import path
from . import views

urlpatterns = [
    path('mul/<a>/<b>/<c>', views.mul, name="mul"),
    path('hps/', views.hps, name="hps"),
    path('movie/', views.movie, name="movie"),
    path('register/', views.register, name="register")
]
