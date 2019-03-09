from django.db import models
import datetime
from django.utils import timezone
class News(models.Model):
    Title = models.CharField(max_length=200) #<title>{% News.title%}</title>
    Link = models.CharField(max_length=2000, unique=True) #a href = {% News.link[]%}
    Comment = models.TextField(
        
        blank = True, 

        default = None)
    Published_date = models.DateField(default =timezone.now)

    Select = (
        ('A', '발전사 동향'), # 한전 #남동발전 #한국전력 #동서발전 #..... -- > 
        ('B', '전력산업/시장'), #전력 #이병준 #주병권
        ('C', '신재생에너지/기술'),
        ('D', '경제/에너지'),
    )
    
    Data_field = models.CharField(
        max_length = 1,
        choices = Select,
        blank = True,
        default = 'm',
    )
    class Meta:
        ordering = ['Data_field', 'Published_date' ]

class Report(models.Model):
	idx = models.AutoField(primary_key=True)
	site = models.CharField(max_length=50)
	title = models.TextField(default = None)
	link = models.TextField(default = None)
	published_date = models.DateField(default = None)