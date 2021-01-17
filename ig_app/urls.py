from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
# from django.contrib.auth import views 

urlpatterns = [
    path(r'',views.index,name='index'),
    path('search/', views.search_results, name='search_results'),
] 

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)