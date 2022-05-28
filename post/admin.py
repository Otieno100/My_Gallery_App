from django.contrib import admin
from .models import Images, User, Category, Location


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('categorys',)
admin.site.register(User)
admin.site.register(Images)
admin.site.register(Location)
admin.site.register(Category)
