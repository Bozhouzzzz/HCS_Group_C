from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'), # jump to second authentication page
    path('image-text/', views.image_text_view, name='image_text'), 
    path('image-text-options/', views.image_text_view_options, name='image_text_options'),
]
