from django.urls import path

from .views import HomePageView, AboutPageView, register_tutor_view, user_profile_view

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('profile/', user_profile_view),
    path('register_tutor/', register_tutor_view),
]
