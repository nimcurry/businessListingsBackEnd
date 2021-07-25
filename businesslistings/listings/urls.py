
from django.urls import path,include
#from django.urls.conf import include
from . import views
from rest_framework import routers 

router = routers.DefaultRouter()
router.register('Listings',views.Listings)
urlpatterns = [
    path('',include(router.urls)),
]
