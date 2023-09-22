from django.contrib import admin
from polls.models import Question, Choice

# Register your models here.

class choiceInline(admin.TabularInline):
    model = Choice
    extra = 3 # default: 3


class QuestionAdmin(admin.ModelAdmin):
    inlines = [choiceInline]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
