from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notebook/<int:notebook_id>/', views.notebook_detail, name='notebook_detail'),
    path('section/<int:section_id>/', views.section_detail, name='section_detail'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('thenumerixsocial/', views.thenumerixsocial, name='thenumerixsocial'),  # Add this line
]
