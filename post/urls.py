from django.urls import re_path,include
from . import views

urlpatterns=[
    # re_path('^$',views.index,name = 'welcome'),

    re_path(r'^$',views.post_of_day,name='postToday'),

]
