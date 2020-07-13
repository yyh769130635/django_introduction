from django.db import models

# Create your models here.

class Article(models.Model):
    #ID：
    article_id = models.AutoField(primary_key=True)
    #标题
    title = models.TextField()
    #摘要
    brief_content = models.TextField()
    #文章内容
    content = models.TextField()
    #文章发布日期
    publish_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
