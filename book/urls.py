from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views
from .views import logout_view

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include(('authentication.urls', 'authentication'), namespace='authentication')),
    
    path('', include(('bookstore.urls', 'bookstore'), namespace='bookstore')),
    
    path('profile', include(('profiles.urls', 'profiles'), namespace='profiless')),
    
    path('login/', views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('accounts/', include('allauth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
