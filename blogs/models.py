from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# 文章标题
class Topic(models.Model):
	"""文章标题"""
	#存储文章标题的名称
	text = models.CharField(max_length=200)
	#存储标题创建的时间(自动获取创建时的系统时间)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User)

	def __str__(self):
		"""返回模型的字符串表示"""
		return self.text

# 文章内容
class Entry(models.Model):
	"""具体的文章内容"""
	#引用数据库的外键属性Topic赋值给topic
	topic = models.ForeignKey(Topic)
	#存储文章的具体内容
	text = models.TextField()
	#存储文章创建的时间(自动获取创建时的系统时间)
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		"""返回模型的字符串表示"""
		if len(self.text) >= 50:
			return self.text[:50] + "..." #只显示钱50个字符
		else:
			return self.text