from django.contrib import admin

from .models import Question, Choice

# add nossas tabelas no admin

admin.site.register(Question)
admin.site.register(Choice)
