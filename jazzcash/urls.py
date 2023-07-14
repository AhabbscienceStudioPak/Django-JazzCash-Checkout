from django.urls import path
from jazzcash import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('success', views.success, name='success'),
]

