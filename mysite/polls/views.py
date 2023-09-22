from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from django.http import HttpRequest
from django.shortcuts import get_object_or_404,render,redirect
from django.urls import reverse
from django.views import generic
from .models import Choice, Question
from django.core.cache import cache

# Create your views here.
class Indexview(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        # return thr last five published questions.
        cached = cache.get("latest_question_list")
        if cached:
            return cached
        
        cached = Question.objects.order_by("pub_date")[:5]
        cache.set("latest_question_list", cached)

        return cached
    
class DetailView(generic.DetailView):
    template_name = "polls/detail.html"
    model = Question

    
class ResultsView(generic.DetailView):
    template_name = "polls/results.html"
    model = Question


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',{
            'question': question,
            'error_message': "you didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect("polls:results", question_id)
