from django.urls import path
from .views import RegisterView, LoginView, ProfileView
from django.views.generic import TemplateView

urlpatterns = [

     path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),

    # Front-end templates
    path('register/', TemplateView.as_view(template_name='register.html'), name='register_page'),
    path('login/', TemplateView.as_view(template_name="login.html"), name="login_page"),
    path('profile/', TemplateView.as_view(template_name="profile.html"), name="profile_page"),
]
    