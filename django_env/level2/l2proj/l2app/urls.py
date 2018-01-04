from django.urls import path
from l2app import views


urlpatterns = [
    path('', views.users,name='users')
]
