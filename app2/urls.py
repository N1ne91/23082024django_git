from django.urls import path
from . import views

urlpatterns = [
    path('18/', views.op),
    path('xd/', views.op2),

]