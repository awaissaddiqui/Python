from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie


# Create your views here.
def index(request):
     movies=Movie.objects.all()
     return render(request,'movies/index.html', {'movies': movies})

def details(request, movie_id):
     movie = get_object_or_404(Movie,pk=movie_id)
     return render(request,'movies/details.html', {'movie':movie})
    
     """
     output=' , '.join([m.title for m in movies])
     #SELECT * FROM movies_movie
     Movie.objects.filter(relase_year=2004)
     #SELECT * FROM movies_movie WHERE ....
     Movie.objects.get(id=1)
     """

     # return HttpResponse(output)
