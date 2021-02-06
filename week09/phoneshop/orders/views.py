from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, request
from .models import Orders
from .serializers import OrdersSerializer, UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework_simplejwt import authentication

class OrdersAPIViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    '''用户关联保存'''
    def perform_create(self, serializer):
        permission_classes = [permissions.IsAuthenticated]
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=['GET'])
    def cancel(self, request, pk, *args, **kwargs):
        st = Orders.objects.get(pk=pk)
        serializer = OrdersSerializer(st)
        if int(serializer.data['order_status']) != 0:
            order_cancel = Orders.objects.filter(pk=pk).update(order_status=0)
        result={"订单状态":"取消成功"}

        return Response(result, status=status.HTTP_200_OK)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET'])
def api_root(request, formate=None):
    return Response({
        'orders': reversed('order-list', request=request, formate=formate)
    })