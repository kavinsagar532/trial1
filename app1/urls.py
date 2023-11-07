from django.urls import path
from . import views

urlpatterns = [
    path('first',views.resume,name="resume"),
    path('table',views.table,name='table'),
]
