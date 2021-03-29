from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from .models import Fact, Service
# Create your views here.


def index(request):
	# return HttpResponse('It\'s working VaiBH')
	fact = Fact.objects.all()
	service, service_count = Service.objects.all(), Service.objects.all().count()
	return render(request, 'mrv/index.html', {'fact':fact, 'service':service, 'service_count':service_count})

def features(request):
	service, service_count = Service.objects.all(), Service.objects.all().count()
	return render(request, 'mrv/features.html', {'service':service, 'service_count':service_count})

def pricing(request):
	service, service_count = Service.objects.all(), Service.objects.all().count()
	return render(request, 'mrv/pricing.html', {'service':service, 'service_count':service_count})

def blog_list(request):
	service, service_count = Service.objects.all(), Service.objects.all().count()
	return render(request, 'mrv/blog-post-list.html', {'service':service, 'service_count':service_count})

def about(request):
	service, service_count = Service.objects.all(), Service.objects.all().count()
	return render(request, 'mrv/about-us.html', {'service':service, 'service_count':service_count})

def contact(request):
	service, service_count = Service.objects.all(), Service.objects.all().count()
	return render(request, 'mrv/contact-us.html', {'service':service, 'service_count':service_count})

def wiki(request):
	return render(request, 'mrv/wiki.html')

def vaibhav_shukla(request):
	return render(request, 'mrv/vaibhav-shukla.html')

def gen(request):
	return render(request, 'mrv/gen.html')
