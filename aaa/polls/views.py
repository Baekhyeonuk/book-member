from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from polls.models import Question, Choice

def index(request):
	latest_question_list = Question.objects.all().order_by('-pub_date')
	# select * from question order by pub_date desc

	context = {'latest_question_list':
	latest_question_list}
	#return HttpResponse(html)
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	##select *from question where id=question_id    두 쿼리문 합한것=question
	##select *from choice where question_id=question_id

	#print(question.choice_set.all())
	return render(request, 'polls/detail.html', {'question': question})

def results(request):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html',{'question':question})

def vote(request):
	#question = get_object_or_404(Question, pk=question_id)
	#selected_choice = question.choice_set.get(pk=request.POST['choice'])
	selected_choice = Choice.objects.get(pk=request.POST['choice'])
	selected_choice.votes += 1
	## update from Choice set votes=votes+1 where id=request.POST['choice']
	selected_choice.save()
	return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

	


