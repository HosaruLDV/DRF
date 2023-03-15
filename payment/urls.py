from django.urls import path

from payment.apps import PaymentConfig
from payment.views import PaymentCreateAPIView, SubscribeListAPIView, SubscribeCreateAPIView, SubscribeDestroyAPIView

app_name = PaymentConfig.name

urlpatterns = [
    path('create/', PaymentCreateAPIView.as_view(), name='payment_create'),
    path('list/', SubscribeListAPIView.as_view(), name='subscribe_list'),
    path('subscribed/', SubscribeCreateAPIView.as_view(), name='subscribed'),
    path('unsubscribed/<int:pk>/', SubscribeDestroyAPIView.as_view(), name='unsubscribed'),
    ]