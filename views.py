from django.http import HttpResponse


def index(requeset):
	return HttpResponse('/index')
