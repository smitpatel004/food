from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):

    people=[
        {'name':'smit','age':20},
         {'name':'smit','age':20},
          {'name':'smit','age':20},
           {'name':'smit','age':20},
    ]
    return render(request,"index.html",context={"people":people})
