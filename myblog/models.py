from django.db import models


# Create your models here.
class user(models.Model):
    name = models.TextField(max_length=20)
    psw = models.CharField(max_length=16)

    # 后台表显示的标题
    def __str__(self):
        return self.name
