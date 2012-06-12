# Create your views here.
from django.http import HttpResponse
from django.conf import settings
import os
from array import *
from django.template import Context, loader
from django.http import HttpResponse

def index(request):
    t = loader.get_template('ma_shop/index.html')
    c = Context({
        })
    return HttpResponse(t.render(c))