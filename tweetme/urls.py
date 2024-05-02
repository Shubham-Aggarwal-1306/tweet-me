"""tweetme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from tweets.views import tweets_list_view, tweets_detail_view, home_view
from django.conf import settings
from accounts.views import login_view, register_view, logout_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home_view'),
    path('login/', login_view, name='login_view'),
    path('register/', register_view, name='register_view'),
    path('logout/', logout_view, name='logout_view'),
    path('<int:tweet_id>', tweets_detail_view, name='tweets_detail_view'),
    path(r'profile/', include('profiles.urls')),
    path('api/profiles/', include('profiles.api.urls')),
    path('api/tweets/', include('tweets.api.urls'))                 
    
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)