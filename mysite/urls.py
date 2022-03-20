from django.contrib import admin
from django.urls import include, path
from rest_framework import routers                 
from myapp import views

router = routers.DefaultRouter()                   
router.register(r'Purchase', views.PurchaseView, 'Purchase')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
