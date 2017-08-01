"""定义blogs的URL模式"""

from django.conf.urls import url
from . import views

urlpatterns = [
	# 主页 
	url(r'^$', views.index, name='index'),
	url(r'^index$', views.index, name='index'),

	# 显示轨迹的所有主题
	url(r'^topics/$', views.topics, name='topics'),

	# 显示轨迹指定主题下的详细页面
	url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

	# 显示轨迹の关于页面
	url(r'^about/$', views.about, name='about'),

	# 用户增加新主题の页面
	url(r'^new_topic/$', views.new_topic, name='new_topic'),

	# 用户增加新内容の页面
	url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

	# 用于编辑条目の页面
	url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]