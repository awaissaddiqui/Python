from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie
# Create your views here.

def index(request):
     movies=Movie.objects.all()
     output=' , '.join([m.title for m in movies])
     """
     #SELECT * FROM movies_movie
     Movie.objects.filter(relase_year=2004)
     #SELECT * FROM movies_movie WHERE ....
     Movie.objects.get(id=1)
     """

     return HttpResponse(output)
