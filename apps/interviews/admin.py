from django.contrib import admin

from .models import Interview, Question, QuestionResult


admin.site.register(Interview)
admin.site.register(Question)
admin.site.register(QuestionResult)
