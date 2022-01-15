from django.urls import path
from . import views

app_name = 'portal'

urlpatterns = [
    # /portal/
    path('', views.IndexView.as_view(), name='index'),
    # /portal/login/
    path('login/', views.LoginView.as_view(), name='login'),
]

