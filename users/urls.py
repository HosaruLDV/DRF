from django.contrib.auth.views import LogoutView
from django.urls import path
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    #path('', CustomLoginView.as_view(), name='login'),
    ]