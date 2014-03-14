from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from revisionmodels.models import Course,Lecture,Tutorial,TutorialQuestion, Exam

def dev(request):
    context = RequestContext(request)
    courses = Course.objects.all();
    context_dict={'courses':courses}
    return render_to_response('dev.html', context_dict, context)