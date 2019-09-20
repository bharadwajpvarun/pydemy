from django.urls import path
from django.contrib.auth import views as authenticate_view
from django.conf import settings
from django.conf.urls.static import static
from project_1_app import views as signup_view

urlpatterns=[path("",authenticate_view.LoginView.as_view(template_name="login.html"), name='login'),
              path("signup/",signup_view.signup, name='signup'),
              path('login/', authenticate_view.LoginView.as_view(template_name="login.html"), name='login'),
              path("pydemy/",signup_view.pydemy,name="pydemy"),]