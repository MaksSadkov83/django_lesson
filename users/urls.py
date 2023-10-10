
from django.urls import path

from users.views import login, reg

app_name = "users"

urlpatterns = [
    path("login/", login, name='login'),
    path("reg/", reg, name='reg'),
]
