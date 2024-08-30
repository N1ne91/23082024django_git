from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def op(request):
    return HttpResponse("<h1>Queda poco para el 18 oleee</h1>")


def op2(request):
    h2="""
      <h1 style="color:blue">When haces tus momos en python xdxdxd</h1>
      <h1 style="color:red">but te terminan reprovando :,v</h1>
      """
    return HttpResponse(h2)