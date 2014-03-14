from django.contrib import admin
from revisionmodels.models import Course, Tutorial, TutorialQuestion, Exam, Lecture

admin.site.register(Course)
admin.site.register(Lecture)
admin.site.register(Tutorial)
admin.site.register(TutorialQuestion)
admin.site.register(Exam)
