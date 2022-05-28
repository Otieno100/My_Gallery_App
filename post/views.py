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



# def locate_image(request,location):
#     photos = Image.filter_by_location(location)
#     return render(request,'album/location.html',{"located_images":photos})

    