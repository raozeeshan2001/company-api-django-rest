from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from .views import Companyviewset
#DefaultRouter() automatically creates RESTful routes.
router=routers.DefaultRouter()
router.register(r'companies',Companyviewset)

urlpatterns = [
   path('',include(router.urls))#registers all generated URLs.
]