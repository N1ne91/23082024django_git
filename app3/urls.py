from django.urls import path
from . import views

urlpatterns = [
    path('18/', views.op),
    path('pagina3/', views.op2),

]