"""
URL configuration for SocialButterfly project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from socialapp import views
from socialapp.forms import edit_event
from socialapp.views import rsvp_event, event_list, create_event, register, user_login, delete_event

urlpatterns = [
    path('admin/', admin.site.urls),
path('create/', create_event, name='create_event'),
    path('event/', event_list, name='event_list'),
    path('rsvp/<int:event_id>/', rsvp_event, name='rsvp_event'),
    path('register/', register, name='register'),  # Registration URL
    path('login/', user_login, name='login'),
    path('', views.index, name='index'),
    path('events/delete_event/<int:event_id>/', delete_event, name='delete_event'),
    path('home/', views.home, name='home'),

    path('children/', views.children, name='children'),
path('contact/', views.contact, name='contact'),
path('corporate/', views.corporate, name='corporate'),
path('entertainment/', views.entertainment, name='entertainment'),
path('peer/', views.peer, name='peer'),
path('teen/', views.teen, name='teen'),
path('event/edit/<int:event_id>/', views.event_list_view, name='edit_event'),

    # Add other URL patterns as needed

]
