from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    uname = models.CharField("用户名", max_length=128)
    upwd = models.CharField('用户密码', max_length=128)
    uemail = models.EmailField("电子邮箱")
    nickname = models.CharField("用户昵称",max_length=128)