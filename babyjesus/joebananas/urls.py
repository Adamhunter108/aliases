from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    # path('add/', views.add_name.as_view(), name='add'),  # trying class based views
    path('add/', views.add_name, name='add_name'),
    path("login/", views.login_view, name="login"),
    path("logout/", views.log_out, name="logout"),
]
