from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone

from school.models import Student, Subject

def index(request):

	if request.method == "GET" and request.GET.get('search'):
		print(request.GET)
		latest_student_list = Student.objects.filter(student_name_contains=request.GET.get('search'))
	else:
		latest_student_list = Student.objects.all().order_by('id')

	context = {'latest_student_list':latest_student_list}
	return render(request, 'school/index.html', context)

def detail(request, student_id):
	student = get_object_or_404(Student, pk=student_id)
	return render(request, 'school/detail.html', {'student': student})

def add(request):
	if request.method == "POST":
		
		qry = Student(student_name=request.POST['student_name'], student_tel=request.POST['student_tel'], student_age=request.POST['student_age'])
		qry.save()
		return HttpResponseRedirect(reverse('school:index'))
	else:
		return render(request, 'school/add.html')

def update(request, student_id):
	if request.method == "POST":
		selected_qry = Student.objects.get(pk=student_id)
		selected_qry.student_name=request.POST['student_name']
		selected_qry.student_tel=request.POST['student_tel']
		selected_qry.student_age=request.POST['student_age']
		selected_qry.student_addr=request.POST['student_addr']
		selected_qry.save()
		return HttpResponseRedirect(reverse('school:index'))
	else:
		student = get_object_or_404(Student, pk=student_id)
		return render(request, 'school/update.html', {'student':student})

def remove(request, student_id):
	Student.objects.get(pk=student_id).delete()

	return	HttpResponseRedirect(reverse('school:index'))	

def upda(request, subject_id):

    if request.method == "POST":

        selected_qry = Subject.objects.get(pk=subject_id)
        selected_qry.subject_text=request.POST['subject_text']
        selected_qry.save()

        return HttpResponseRedirect(reverse('school:index'))

        #print(selected_qry)

    else:
        subject = get_object_or_404(Subject, pk=subject_id)
        return render(request, 'school/upda.html', {'subject': subject})



def sub_add(request):
    if request.method == "POST":
        #print(timezone.now())
        qry = Subject(subject_text=request.POST['subject_text'],\
                      student_id=request.POST['student_id'], subject_ovew=request.POST['subject_ovew'])
        qry.save()

        #print(type(request.POST['subject_date']))
        return HttpResponseRedirect(reverse('school:detail', args=(request.POST['student_id'],)))

    else:
        student_list = Student.objects.all()
        #student = Student.objects.get(pk=student_id)
        return render(request, 'school/sub_add2.html', {'student_list': student_list })

def sub_del(request, subject_id):
	student = Subject.objects.get(pk=subject_id)
	Subject.objects.get(pk=subject_id).delete()
	return HttpResponseRedirect(reverse('school:detail', args=(student.student_id,)))	



