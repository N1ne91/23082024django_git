from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Soy el index de la app1</h1>")

def presentacion(request):
    html="""
        <p>Soy el párrafo de la app1.</p>
        <h2>Soy un subtítulo</h2> 
    """
    return HttpResponse(html)