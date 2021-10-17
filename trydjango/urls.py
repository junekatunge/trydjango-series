"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth import logout
from django.urls import path


from accounts.views import (
    login_view,
    logout_view
) 
from articles.views import (
    articles_detail_view,
    articles_create_view,
    articles_search_view
)
from .views import home_view

urlpatterns = [
    path('',home_view ),#homepage
    path('articles/', articles_search_view),#URL for search.html
    path('articles/create/', articles_create_view),
    path('articles/<int:id>/', articles_detail_view),#dynamic URL
    path('admin/', admin.site.urls),
    path('login/',login_view),
    path('logout/',logout_view)
]
