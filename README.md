

# 《Django 项目之个人博客》

## 目录

[TOC]

## 网络云笔记项目

- 功能:
  1. 注册
  1. 登陆
  1. 退出登陆
  1. 查看发表的文章
  1. 发布新的文章
  1. 修改文章
  1. 删除文章
  1. 上传图片
  1. 查看相册
  1. 留言

### 版本
Django 1.11.8
python 3.6.9


### 数据库设计

- 模型类

  1. 用户模型类

     ```python
     class User(models.Model):
         username = models.CharField("用户名", max_length=30, unique=True)
         password = models.CharField("密码", max_length=30)
         create_time = models.DateTimeField('创建时间', auto_now_add=True)
         isActived =BooleanField(default=True)
     
         def __str__(self):
             return "用户" + self.username
     ```

  2. 文章模型类

  ~~~python
  class Topic(models.Model):
      title = models.CharField('标题', max_length=100)
      content = models.TextField('内容')
      images = models.ImageField('图片',upload_to = 'static/images')
      read_nums = models.IntegerField('阅读数',default=0)
      create_time = models.DateTimeField('创建时间', auto_now_add=True)
      mod_time = models.DateTimeField('修改时间', auto_now=True)
      
      #与用户表建立外键，一对多，主表删除，从表为null
      user = models.ForeignKey(User,on_delete=SET_NULL,null=True)
      
      #与文章类别建立多对多关系
      categorys = models.ManyToManyField(Category)
  
  ```
  ~~~

​    3.文章类别模型类

```python
class Category(models.Model):
    category_name = models.CharField('类别',max_length=50)
    create_time = models.DateTimeFiled('创建时间',auto_now_add=True)
    mod_time = models.DateTimeField('修改时间', auto_now=True)
    
 
```

4.留言模型类

    #待完善





### 设计规范



主页设计规范(在index应用中写代码)

| 路由正则 | 视图函数                 | 模板位置                   | 说明 |
| -------- | ------------------------ | -------------------------- | ---- |
| /        | def index_view(request): | templates/index/index.html | 主页 |

登陆设计规范(在user应用中写代码)

| 路由正则     | 视图函数                  | 模板位置           | 说明         |
| ------------ | ------------------------- | ------------------ | ------------ |
| /user/login  | def login_view(request):  | user/login.html    | 用户登陆     |
| /user/reg    | def reg_view(request):    | user/register.html | 用户注册     |
| /user/logout | def logout_view(request): | user/logout.html   | 退出用户登陆 |

文章设计规范

| 路由正则             | 视图函数                             | 模板位置             | 说明                 |
| -------------------- | ------------------------------------ | -------------------- | -------------------- |
| /article/list        | def list_view(request):              | article/list.html    | 显示文章列表         |
| /article/list/(\d+)  | def page_view(request,page)          | article/page.html    | 显示分页内容         |
| /article/(\d+)       | def content_view(request,article_id) | article/content.html | 显示文章内容         |
| /article/write       | def no_write_view(request)           | 无                   | 没有写权力，返回主页 |
| /article/write/(\d+) | def write_view(request,u_id)         | article/write.html   | 显示写页面           |

相册设计规范

| 路由正则          | 视图函数                     | 模板位置         | 说明         |
| ----------------- | ---------------------------- | ---------------- | ------------ |
| /album/list       | def list_view(request):      | album/list.html  | 显示相册列表 |
| /album/list/(\d+) | def album_view(request,name) | album/album.html | 显示相册内容 |