from django.contrib import admin
from .models import Question
# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    list_display = '__all__'

admin.site.register(Question,)