from django.urls import path
from . import views # . means import from current directory

app_name = "tasks" # in order to avoid name collision
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add")
] 