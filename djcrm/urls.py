from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from leads.views import LandingPageView, SignupView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', LandingPageView.as_view(), name='landing-page'),

    path('leads/', include('leads.urls', namespace='leads')),

    path('agents/', include('agents.urls', namespace='agents')),

    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('signup/', SignupView.as_view(template_name='accounts/signup.html'), name='signup'),
  
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'accounts/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name = 'accounts/password_reset_complete.html'), name='password_reset_complete'),


    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/login.html'), name='logout'),
]
