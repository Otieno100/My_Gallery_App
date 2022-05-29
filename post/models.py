from django.db import models
import datetime as dt



# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)

    def __str__(self):
      return self.first_name

    def save_user(self):
        self.save()




class Location(models.Model):
    """
    This class provies the location of the image where it was taken
    """
    city = models.CharField(max_length=244)
    country = models.CharField(max_length=244)




class Category(models.Model):
    """
    A class for the category the Images falls under
    """
    name = models.CharField(max_length=144)







class Images(models.Model):
    """
    A class thaat determines how photos will be saved into the database
    """
    name = models.CharField(max_length=344)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'images/',default = 'brian')
    def __str__(self):
        return self.name


    @classmethod
    def todays_post(cls):
        today = dt.date.today()
        post = cls.objects.filter(pub_date__date = today)
        return post

    @classmethod
    def search_by_name(cls,search_term):
        post = cls.objects.filter(name__icontains=search_term)
        return post       

    @classmethod
    def days_news(cls,date):
        post = cls.objects.filter(pub_date__date = date)
        return post  
