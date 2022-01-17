from django.urls import path
from . import views

app_name = 'portal'

urlpatterns = [
    # /portal/
    path('', views.IndexView.as_view(), name='index'),

    # /portal/login/
    path('login/', views.LoginView.as_view(), name='login'),

    # /portal/article/add/
    path('article/add/', views.ArticleCreate.as_view(), name='article-add'),

    # /portal/article/<pk>/
    path('article/<int:pk>/', views.ArticleUpdate.as_view(), name='article-update'),

    # /portal/article/<pk>/delete/
    path('article/<int:pk>/delete/', views.ArticleDelete.as_view(), name='article-delete'),
]

