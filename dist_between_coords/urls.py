from django.urls import path

from dist_between_coords import views


urlpatterns = [
    path('', views.DistBetweenCoords.as_view()),
]
