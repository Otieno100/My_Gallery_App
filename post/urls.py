from django.urls import re_path,include
from . import views

urlpatterns=[
    # re_path('^$',views.index,name = 'welcome'),

    re_path(r'^$',views.post_of_day,name='postToday'),
    re_path(r'^search/', views.search_results, name='search_results')

]
