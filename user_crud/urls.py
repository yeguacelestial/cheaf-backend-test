from django.urls import path, include
from rest_framework import routers

from user_crud import views


router = routers.DefaultRouter()
router.register('', views.UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework_urls'))
]