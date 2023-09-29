from django.urls import path
from .views import CustomerRegistration, CustomerLogin
from . import views
urlpatterns = [
    path('register/', CustomerRegistration.as_view(), name='customer-registration'),
    path('login/', CustomerLogin.as_view(), name='customer-login'),
]
