from django.urls import path

from payment.apps import PaymentConfig
from payment.views import PaymentCreateAPIView, SubscribeListAPIView, SubscribeCreateAPIView, SubscribeDestroyAPIView, \
    PaymentAPIView, PaymentlogList, PaymentList

app_name = PaymentConfig.name

urlpatterns = [
    path('create/', PaymentCreateAPIView.as_view(), name='payment_create'),
    path('list/', SubscribeListAPIView.as_view(), name='subscribe_list'),
    path('subscribed/', SubscribeCreateAPIView.as_view(), name='subscribed'),
    path('unsubscribed/<int:pk>/', SubscribeDestroyAPIView.as_view(), name='unsubscribed'),
    path('course/buy/<int:pk>/', PaymentAPIView.as_view(), name='course_buy'),
    path('paymentlog/list/', PaymentlogList.as_view(), name='paymentlog_list'),
    path('payment/list/', PaymentList.as_view(), name='payment_list')
    ]