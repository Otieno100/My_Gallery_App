from django.test import TestCase
from .models import User, Images, Location, Category

# Create your tests here.
class UserTestClass(TestCase):
    """
    defining testcase for User class

    """
    def setUp(self) :
        self.Halima = User(first_name = 'precious',last_name = 'Halima', email = 'precious@moringaschool.com')
        


    def test_instance(self):
        self.assertTrue(isinstance(self.Halima,User))



    def test_save_method(self):
        self.Halima.save_user()
        users = User.objects.all()
        self.assertTrue(len(users) > 0) 


class LocationTestClass(TestCase):
    """
     defining test for Location class
    """
    def setUp(self):
        """
        Creating a new instance of the Location class
        """
        self.place = Location(city = "Nairobi", country = "Kenya")
        self.place.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.place, Location))

    def test_save_method(self):
        places = Location.objects.all()
        self.assertTrue(len(places) > 0)


class CategoryTestClass(TestCase):
    """
    Testing the Category class
    """
    def setUp(self):
        """
        Creating a new instance of the Category class
        """
        self.category = Category(name = "Test")
        self.category.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_method(self):
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)    


class ImagesTestClass(TestCase):
    """
    Creating the initial instance of the images class
    """
    def setUp(self):
        self.place = Location(city = "Nairobi", country = "Kenya")
        self.place.save()

        self.category = Category(name = "Test")
        self.category.save()

        self.photo = Images(name = 'A random title', description = "A random description",
                           location = self.place)
        self.photo.save()        

        