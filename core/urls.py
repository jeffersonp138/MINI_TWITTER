from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from MINI_TWITTER import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include('MINI_TWITTER.urls')),
    #path('', views.UserRegisterView.as_view() , name='userRegister'),
    #path('', views.home, name='home')
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)