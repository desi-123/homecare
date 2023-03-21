from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
 list_display = ('id', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'ans1', 'ans2', 'ans3', 'ans4', 'ans5', 'ans6', 'ans7', 'ans8')
 list_display_links = ('id', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'ans1', 'ans2', 'ans3', 'ans4', 'ans5', 'ans6', 'ans7', 'ans8')
 list_filter = ('id', )
 list_per_page = 20
admin.site.register(Question, QuestionAdmin)