from django.urls import path
from . import views

app_name = "index"

urlpatterns = [
    path('', views.homepage, name = "homepage"),
    path('action/',views.actionpage, name = "actionpage"),
    path('blm/',views.blmpage, name = "blmpage"), 
    path('leaders/',views.leaderspage, name = "leaderspage"),
    path('racism/',views.racismpage, name = "racismpage"),
]