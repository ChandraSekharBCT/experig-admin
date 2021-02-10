"""Experig URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url 
from testapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('project_detail_preview/<int:id>', views.project_detail_preview),
    url(r'^$',views.company_landing_page),
    url(r'^signin/',views.signin),
    url(r'^company_register/',views.company_register),
    url(r'^multistepform_save/',views.multistepform_save),
    url(r'^dashboard_menu/',views.dashboard_menu),
    url(r'^logout/',views.logout),
    url(r'^new_project_screen/',views.new_project_screen),
    url(r'^project_skill/',views.project_skill),
    url(r'^incentives/',views.incentives),
    url(r'^project_optimization/',views.project_optimization),
    url(r'^project_detail/',views.project_detail),
    url(r'^create_project/',views.create_project),
    url(r'^explore_virtual_teams_screen/',views.explore_virtual_teams_screen),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
