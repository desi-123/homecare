from django.shortcuts import render
from .models import Question
def question(request):
 question = Question.objects.all()
 context = {
  'question': question
 }
 return render(request, 'pages/question.html', context)