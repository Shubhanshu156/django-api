from django.conf.urls import  include
from django.urls.conf import re_path 
 
from django.conf import settings
from django.conf.urls.static import static
from tutorials.views import hotel_image_view,success
urlpatterns = [ 
    re_path(r'^', include('tutorials.urls')),
    
    re_path('image_upload', hotel_image_view, name = 'image_upload'),
    re_path('success', success, name = 'success'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
