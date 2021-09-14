from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('search_results/', views.search_view, name="search"),
]
