from django.db import models

class Orders(models.Model):
    __tablename__ = 'orders'
    order_name = models.CharField(max_length=30, verbose_name='订单名',default='')
    order_number = models.IntegerField(verbose_name='订单量',default=1)
    order_status = models.IntegerField(verbose_name='订单状态',default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='orders', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_time']

    def __str__(self):
        return self.order_name