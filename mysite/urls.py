"""mysite URL Configuration

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
from django.contrib.auth.views import login, logout  # 追加
from accounts import views  # 追加
from django.contrib import admin  # 追加
from django.conf.urls import url  # 追加
from django.contrib import admin
from django.urls import path  # ,   include  # include を追記

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create_account, name='create_account'),
    url(r'^logout/$', logout, {'template_name': 'index.html'}, name='logout'),
    path('login/', views.loginView.as_view(), name="login"),
]
