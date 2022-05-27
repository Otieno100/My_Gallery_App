from django.shortcuts import render
from django.http  import HttpResponse
# from .models import Image,Location,Category

# Create your views here.
def index(request):
    return render(request,'index.html')


# def locate_image(request,location):
#     photos = Image.filter_by_location(location)
#     return render(request,'album/location.html',{"located_images":photos})

    