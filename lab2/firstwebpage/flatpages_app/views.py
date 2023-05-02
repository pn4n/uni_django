from django.shortcuts import render
from django.http import HttpResponse

# answer without render page
# def home(request):
# 	# text = u'Привет, Мир!ja'.encode('utf8')
# 	text = "hello, world!"
# 	return HttpResponse(text) #, content_type="text/plain"

def home(request):
    return render(request, 'static_handler.html')
