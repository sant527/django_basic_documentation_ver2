from django.urls import path
from . import views

app_name='login_register_password_app_name'

urlpatterns = [
    path('user_login_via_otp_form_email',views.user_login_via_otp_form_email, name='user_login_via_otp_form_email'),
    path('user_login_via_otp_form_otp',views.user_login_via_otp_form_otp, name='user_login_via_otp_form_otp'),
    path('logout',views.logout_view, name='logout_view'),
    path('api_user_login_via_otp_form_email_django_forms_example',views.api_user_login_via_otp_form_email_django_forms_example,name='api_user_login_via_otp_form_email_django_forms_example')
]