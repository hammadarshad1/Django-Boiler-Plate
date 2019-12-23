from django.http import HttpResponse
import datetime

def home(request):
    now = datetime.datetime.now()
    html = '<html><body>Hello World-Made By Hammad @github.com/hammadarshad1<br>It is now %s</body></html>' % now
    return HttpResponse(html)