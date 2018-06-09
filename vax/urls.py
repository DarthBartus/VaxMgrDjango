"""vax URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
import vaxmgr.views

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', vaxmgr.views.index, name='index'),
    path('', vaxmgr.views.index, name='index'),
    path('connection/', vaxmgr.views.connection_view,),
    path(u'search/', vaxmgr.views.search, name='search'),
    path('success/', vaxmgr.views.success, name='success'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('update/', vaxmgr.views.db_update, name='db-update'),
    path('select2/', include('django_select2.urls')),
]

handler403 = 'vaxmgr.views.error403'
