from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from .models import  Images

# Create your views here.
def index(request):
    return render(request,'index.html')


def post_of_day(request):
    date = dt.date.today()
    post = Images.todays_post()
    return render(request, 'Gallery-images/today-post.html', {"date": date,"post":post})



def search_results(request):

    if 'images' in request.GET and request.GET["images"]:
        search_term = request.GET.get("images")
        searched_images = Images.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'Gallery-images/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any image from the gallery"
        return render(request, 'Gallery-images/search.html',{"message":message})




# def locate_image(request,location):
#     photos = Image.filter_by_location(location)
#     return render(request,'album/location.html',{"located_images":photos})

    