"""
URL configuration for core project.

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
from home.views import *
from veg.views import *
from django.conf.urls.static import static


from django.conf import settings


urlpatterns = [
    path("",home,name="home"),
    path("receipes/",receipes,name="receipes"),
    path('delete-receipe/<id>/',delete_recepie,name="delete_receipe"),
    path('update-receipe/<id>/',update_recepie,name="update_receipe"),
    path('login/',login_page,name='login'),
    path('logout/',logout_page,name='logout'),

    path('register/',register_page,name='register'),
    path('student/',student_get,name='student_get'),
    path('admin/', admin.site.urls),
] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
