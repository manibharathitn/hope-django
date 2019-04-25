from django.http import HttpResponse

def hello(request):
    return HttpResponse("<h1>Hello World, This is Mani from Webapplication</h1>")

