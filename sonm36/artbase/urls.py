from django.urls import path
from . import views


app_name = "artbase"

urlpatterns = [
    path('', views.add_artists, name="add"),
    path('artists_list/', views.ArtistsListView.as_view(), name="show"),
]
