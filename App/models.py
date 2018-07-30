from django.db import models


# 创建帖子的库
class Card(models.Model):
    # 帖子标题
    card_title = models.CharField(max_length=128)
    # 帖子内容
    card_content = models.TextField()
    # 帖子的更新时间
    card_create_time = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'card_db'


class User(models.Model):

    user_name = models.CharField(max_length=64)

    class Meta:
        db_table = 'user_db'


