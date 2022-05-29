from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from .models import  Images,Location

# Create your views here.

def index(request):
    return render(request, 'Gallery-images/index.html')



def post_of_day(request):
    date = dt.date.today()
    post = Images.todays_post()
    return render(request, 'Gallery-images/today-post.html', {"date": date,"post":post})



def search_results(request):

    if 'images' in request.GET and request.GET["images"]:
        search_term = request.GET.get("images")
        searched_images = Images.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'Gallery-images/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any image from the gallery"
        return render(request, 'Gallery-images/search.html',{"message":message})



    
def location_filter(request, id):
    images = Images.objects.filter(location__id = id)
    results = len(images)
    location = Location.objects.get(id = id)
    locations = Location.objects.all()

    return render(request, "gallery/location.html", context={"images":images,"results":results,"location":location,"locations":locations})
                                                             
                                                             
                                                             
