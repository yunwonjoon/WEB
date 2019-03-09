from django.conf.urls import url
from MorningBriefing import views
app_name = 'MorningBriefing'
urlpatterns = [
	url(r'^$',views.index, name = 'home'),
	url(r'^발전사동향/',views.a, name='발전사동향'),
	url(r'^파워인사이트/',views.Powerinsight, name='파워인사이트'),
	url(r'^전력산업/시장/',views.b, name='전력산업/시장'),
	url(r'^신재생에너지/기술/',views.c, name='신재생에너지/기술'),
	url(r'^경제/에너지/',views.d ,name='경제/에너지'),
	url(r'^(?P<pk>\d+)/add_comment_to_post/$',views.add_comment_to_post, name='add_comment_to_post'),
	url(r'^(?P<pk>\d+)/delete/$',views.delete,name='delete_news'),
	url(r'^(?P<pk>\d+)/delete/$',views.delete_news,name='delete'),
	url(r'^보고서/',views.report ,name='보고서'),
	url(r'^보고서초기화/',views.reportinitialize ,name='보고서초기화'),
	url(r'^(?P<pk>\d+)/modify_title/$',views.modify_title, name='modify_title'),
	
]