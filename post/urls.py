from django.urls import path
from .views import *

app_name = 'posts'
urlpatterns = [
    path("", PostView.as_view(), name="list"),
    path("create/", PostCreateView.as_view(), name="create"),
    path("<int:pk>/", PostDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", PostUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", PostDeleteView.as_view(), name="delete"),
]
