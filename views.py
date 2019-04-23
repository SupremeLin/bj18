from django.http import HttpResponse
from djando.shortcuts import redirects


def index(requeset):
	return HttpResponse('/index')


def login(request):
	return redirect('/index')
