from django.urls import path
from . import views

urlpatterns = [
    path('api/dresses', views.DressList.as_view(), name='dress_list'),
    path('api/dresses/<int:pk>', views.DressDetail.as_view(), name='dress_detail'),
]
