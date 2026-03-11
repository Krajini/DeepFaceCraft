from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("index.html", views.index, name="index"),

    
    path("TexttoImage", views.TexttoImage, name="TexttoImage"),
    path("TrainModel", views.TrainModel, name="TrainModel"),
    path("TexttoImageAction", views.TexttoImageAction, name="TexttoImageAction"),

    path("HumanFaces", views.HumanFaces, name="HumanFaces"),
    path("HumanFacesAction", views.HumanFacesAction, name="HumanFacesAction"),

    # ✅ ADD THESE
    path("Register", views.Register, name="Register"),
    path("Login", views.Login, name="Login"),
]