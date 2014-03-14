from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def dev(request):
    context = RequestContext(request)
    balance=0
    context_dict={'balance':balance}
    return render_to_response('dev.html', context_dict, context)