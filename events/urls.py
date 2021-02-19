from django.urls import path
from . import views

urlpatterns = [
    # Path Converters:
    # int: numbers
    # str: strings
    # path: whole urls /
    # slug: hyphens-and underscores_stuff
    # UUID: universally unique identifiers

    path('', views.home, name="home"),
    path('<int:year>/<str:month>/', views.home, name="home"),
    path('events', views.allEvents, name="events-list"),
]


