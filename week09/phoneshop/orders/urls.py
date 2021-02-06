from rest_framework import routers
from . import views
from django.conf.urls import include
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

order_list = views.OrdersAPIViewSet.as_view({
    'post': 'create'
})

router = routers.DefaultRouter()
router.register(r'orders', views.OrdersAPIViewSet, 'order-list')
router.register(r'users', views.UserViewSet, )

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_frameapi_rootwork')),
    path('orders/create', order_list, name='order-list'),
    path('orders/<int:pk>/cancel', views.OrdersAPIViewSet),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]