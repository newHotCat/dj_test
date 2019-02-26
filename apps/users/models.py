from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    """
    自定义系统用户 需要在 setting 中重新设置
    用户
    """
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")  # 姓名
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")  # 出生日期
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", "女")), default="female",
                              verbose_name="性别")  # gender 性别
    mobile = models.CharField(max_length=11, verbose_name="电话")  # 手机号
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name="邮箱")  # 邮箱

    class Meta:
        """
        内嵌类 给model 定义元数据
        """
        # verbose_name的意思很简单，就是给你的模型类起一个更可读的名字
        verbose_name = "用户"
        # 这个选项是指定模型的复数形式是什么
        verbose_name_plural = "用户"

    def __str__(self):
        """
        打印类的返回
        """
        return self.name


class VerifyCode(models.Model):
    """
    短信验证码
    """
    code = models.CharField(max_length=10, verbose_name="验证码")
    mobile = models.CharField(max_length=11, verbose_name="电话")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        # 详细名称
        verbose_name = "短信验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
