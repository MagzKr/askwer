from account.views import signup_view
from django.urls import path
urlpatterns = [
    path('signup/',signup_view, name='signup'),
    path('profile/', profile_view, name='profile')]