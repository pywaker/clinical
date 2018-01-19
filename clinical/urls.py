"""clinical URL Configuration

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
from django.urls import path, include, re_path
from webapp import views as web_views

import debug_toolbar


urlpatterns = [
    re_path(r'^__debug__/', include(debug_toolbar.urls)),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('entry/', web_views.create_ticket, name='add_ticket'),
    path('doctors/list/', web_views.list_doctors, name='list_doctors'),
    path('patients/', web_views.list_patients, name='list_patients'),
    path('api/patients/', web_views.patient_list),
    path('api/patients/<int:patient_id>', web_views.get_patient)
]
