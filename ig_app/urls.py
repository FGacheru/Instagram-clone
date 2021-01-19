from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
# from django.contrib.auth import views 

urlpatterns = [
    path(r'',views.index,name='index'),
    path('search/', views.search_results, name='search_results'),
    path('post/', views.new_post, name='post'),
    path('profile/', views.profile, name='profile'),
    path('comment/<id>', views.comment, name='comments'),
    path('edit_profile/', views.editProfile,name = 'update_profile'), 
    path('new/post/', views.newPost, name='newPost'),
    
] 

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)