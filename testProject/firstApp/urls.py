from django.urls import path
from . import views # . means import from current directory

urlpatterns = [
    path("", views.index, name="index"),
    path("ab", views.ab, name="ab"),
    path("david", views.david, name="david"),
    path("<str:name>", views.greet, name="greet")

]