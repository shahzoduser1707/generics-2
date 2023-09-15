from django.urls import path 
from .views import getWorker,DetailDestroyUpdateView 
urlpatterns = [
    path('getWorker/', getWorker.as_view()),
    path('<int:pk>/', DetailDestroyUpdateView.as_view())
]