
from django.urls import path
from .views import blog_index, show_article

urlpatterns = [
    path('', blog_index),
    path('article/<int:numero>/', show_article, name="show_article")
]
