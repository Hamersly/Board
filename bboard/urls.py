from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index_url'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric_url'),
    path('add/', BbCreateView.as_view(), name='add_url')
]
