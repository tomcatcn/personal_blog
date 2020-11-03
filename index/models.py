from django.db import models
from user.models import User

# Create your models here.
class Category(models.Model):
    category_name = models.CharField('类别',max_length=50)
    create_time = models.DateTimeField('创建时间',auto_now_add=True)
    mod_time = models.DateTimeField('修改时间', auto_now=True)


class Article(models.Model):
    title = models.CharField('标题', max_length=100)
    content = models.TextField('内容')
    images = models.ImageField('图片', upload_to='static/images')
    read_nums = models.IntegerField('阅读数', default=0)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    mod_time = models.DateTimeField('修改时间', auto_now=True)

    # 与用户表建立外键，一对多，主表删除，从表为null
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    # 与文章类别建立多对多关系
    categorys = models.ManyToManyField(Category)
