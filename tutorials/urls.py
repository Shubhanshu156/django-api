from tracemalloc import reset_peak
# from django.conf.urls import url
from django.urls import re_path
from sympy import re 
from tutorials import views 




 
urlpatterns = [ 
    re_path(r'^api/tutorials$', views.tutorial_list),
    re_path(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    re_path(r'^api/tutorials/published$', views.tutorial_list_published),
    re_path(r'^api/dimension/(?P<title>[a-zA-Z0-9_]+)$',views.get_title_tutorial),
    re_path(r'^api/upload$', views.upload_docs),
    re_path(r'^api/createuser$', views.user),
    re_path(r'^api/login$', views.login),
    # re_path('image_upload', views.hotel_image_view, name = 'image_upload')
]
