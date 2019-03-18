# from django.conf import settings
# from django.conf.urls.static import static

# from django.conf.urls import url
# from . import views

# urlpatterns=[
#     url('^$',views.welcome,name = 'welcome'),
#     url('^today/$',views.one_photo,name='photosToday'),
#     url(r'^search/', views.search_results, name='search_results')
# ]

# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.welcome,name = 'welcome'),
    url(r'^search/', views.search_results,name='search_results'),
    url(r'^location/(\d+)',views.display_location,name='displayLocation'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)