from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    # path('add/', views.add_name.as_view(), name='add'),  # trying class based views
    path('add/', views.get_add_name, name='get_add_name'),
    path('add/post_add', views.post_add_name, name='post_add_name'),
    path("login/", views.login_view, name="login"),
    path("logout/", views.log_out, name="logout"),
    path("signup/", views.SignUp.as_view(), name="signup"),
]
