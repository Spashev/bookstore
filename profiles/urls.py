from django.urls import path
from profiles.views import IndexView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('', IndexView.as_view(), name='profile'),
]