from django.http import HttpResponse

from . import plotly_app

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")