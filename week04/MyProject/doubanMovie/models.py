from django.db import models

# Create your models here.

class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    m_star = models.IntegerField()
    short = models.CharField(max_length=400)
    sentiment = models.DateTimeField()