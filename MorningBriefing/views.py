from django.shortcuts import render, redirect,get_object_or_404
from .models import News, Report
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from .forms import CommentForm, NewTitleForm
from django.views.decorators.csrf import csrf_exempt
import json
from django.template import loader
from datetime import timedelta
import datetime
from django.db.models import Q


def index(request):
	news = News.objects.all()
	context = {'news' :news}
	return render(request, 'MorningBriefing/index.html',context)


def Powerinsight(request):
	report = Report.objects.all()
	context = {'report' :report}
	return render(request, 'MorningBriefing/Powerinsight.html',context)


@csrf_exempt
def a(request):
	today=datetime.date.today()
	one_day_ago = today-datetime.timedelta(days=1)
	try:
		start_date=request.POST["start_date"]
	except:
		start_date="2019-01-01"
	try:
		end_date=request.POST["end_date"]
	except:
		end_date=today
	try:
		search=request.POST["search"]
	except:
		search=""
	start_date=start_date if start_date else one_day_ago
	end_date=end_date if end_date else today
	news = News.objects.filter(Q(Published_date__gte=start_date, Published_date__lte=end_date)&Q(Title__contains=search))
	context = {'news':news,}
	return render(request, 'MorningBriefing/a.html',context)

def b(request):
	today=datetime.date.today()
	one_day_ago = today-datetime.timedelta(days=1)
	try:
		start_date=request.POST["start_date"]
	except:
		start_date="2019-01-01"
	try:
		end_date=request.POST["end_date"]
	except:
		end_date=today
	try:
		search=request.POST["search"]
	except:
		search=""
	start_date=start_date if start_date else one_day_ago
	end_date=end_date if end_date else today
	news = News.objects.filter(Q(Published_date__gte=start_date, Published_date__lte=end_date)&Q(Title__contains=search))
	context = {'news':news,}
	return render(request, 'MorningBriefing/b.html',context)

def c(request):
	today=datetime.date.today()
	one_day_ago = today-datetime.timedelta(days=1)
	try:
		start_date=request.POST["start_date"]
	except:
		start_date="2019-01-01"
	try:
		end_date=request.POST["end_date"]
	except:
		end_date=today
	try:
		search=request.POST["search"]
	except:
		search=""
	start_date=start_date if start_date else one_day_ago
	end_date=end_date if end_date else today
	news = News.objects.filter(Q(Published_date__gte=start_date, Published_date__lte=end_date)&Q(Title__contains=search))
	context = {'news':news,}
	return render(request, 'MorningBriefing/c.html',context)

def d(request):
	today=datetime.date.today()
	one_day_ago = today-datetime.timedelta(days=1)
	try:
		start_date=request.POST["start_date"]
	except:
		start_date="2019-01-01"
	try:
		end_date=request.POST["end_date"]
	except:
		end_date=today
	try:
		search=request.POST["search"]
	except:
		search=""
	start_date=start_date if start_date else one_day_ago
	end_date=end_date if end_date else today
	news = News.objects.filter(Q(Published_date__gte=start_date, Published_date__lte=end_date)&Q(Title__contains=search))
	context = {'news':news,}
	return render(request, 'MorningBriefing/d.html',context)

def report(request):
	news = News.objects.all()
	context = {'news':news,}
	return render(request, 'MorningBriefing/report.html',context)

def reportinitialize(request):
	news = News.objects.filter(Comment__isnull=False)
	for news in news:
		news.Comment=''
		news.save()
	return HttpResponseRedirect("/")
	

def comment_detail(request,pk):
	news = get_object_or_404(News,pk=pk)
	return render(request, 'MorningBriefing/comment_detail.html',{'news':news})


def add_comment_to_post(request,pk):
	news = get_object_or_404(News,pk=pk)

	if request.method == "POST":
		comment_form = CommentForm(request.POST)

		if CommentForm(request.POST).is_valid():
			news = News.objects.get(pk=pk)
			comment_form = CommentForm(request.POST, instance = news)
			comment_form.save()

			if news.Data_field == 'A':
				return HttpResponseRedirect("/발전사동향")
			if news.Data_field == 'B':
				return HttpResponseRedirect("/전력산업/시장")
			if news.Data_field == 'C':
				return HttpResponseRedirect("/신재생에너지/기술")
			if news.Data_field == 'D':
				return HttpResponseRedirect("/경제/에너지")
	else:
		form = CommentForm()
	return render(request, 'MorningBriefing/add_comment_to_post.html',{'news':news, 'form':form})


def delete(request,pk):
	news = get_object_or_404(News,pk=pk)
	news.Comment = ''
	news.save()
	if news.Data_field == 'A':		
		return redirect("/발전사동향")
	if news.Data_field == 'B':
		return redirect("/전력산업/시장")
	if news.Data_field == 'C':
		return redirect("/신재생에너지/기술")
	if news.Data_field == 'D':
		return redirect("/경제/에너지")

def delete_news(request,pk):
	news = get_object_or_404(News,pk=pk)
	news.delete()
	if news.Data_field == 'A':		
		return redirect("/발전사동향")
	if news.Data_field == 'B':
		return redirect("/전력산업/시장")
	if news.Data_field == 'C':
		return redirect("/신재생에너지/기술")
	if news.Data_field == 'D':
		return redirect("/경제/에너지")

def modify_title(request,pk):
	news = get_object_or_404(News,pk=pk)

	if request.method == "POST":
		new_title = NewTitleForm(request.POST)

		if NewTitleForm(request.POST).is_valid():
			news = News.objects.get(pk=pk)
			new_title = NewTitleForm(request.POST, instance = news)
			new_title.save()

			if news.Data_field == 'A':
				return HttpResponseRedirect("/발전사동향")
			if news.Data_field == 'B':
				return HttpResponseRedirect("/전력산업/시장")
			if news.Data_field == 'C':
				return HttpResponseRedirect("/신재생에너지/기술")
			if news.Data_field == 'D':
				return HttpResponseRedirect("/경제/에너지")
	else:
		form = NewTitleForm()
	return render(request, 'MorningBriefing/modify_title.html',{'news':news, 'form':form})

