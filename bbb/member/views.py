#from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from member.models import Mem
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.core.files.storage import FileSystemStorage
try:
    from django.utils import simplejson as json
except ImportError:
    import json
# from django.conf import settings
# import os

class MemListView(ListView):
    model = Mem
    ## 모델명(소문자)_list.html
    template_name = 'member/list.html'
    ## object_list 로 객체 반환
    

class MemAddView(CreateView):
    model = Mem
    fields = ['Mem_id','Mem_name', 'Mem_pwd', 'Mem_img']
    success_url = reverse_lazy('product:list')
    template_name = 'member/add.html'

# def add(request):
#     form=Mem()    
#     if request.method == "POST":
#         
#         if request.FILES:
#             form.Mem_img = request.FILES['upload_files']
#         else:
#            form.Mem_img = ''
# 
#         form.Mem_id=request.POST['mem_id']
#         form.Mem_name=request.POST['mem_name']
#         form.Mem_pwd=request.POST['mem_pwd']
#         form.save()
#         return HttpResponseRedirect(reverse('member:list'))
# 
#     else:
#         return render(request, 'member/add2.html')
# 
# def edit(request, pk):
# 
#     if request.method == "POST":
# 
#         form = Mem.objects.get(pk=pk)
#         if request.FILES:
#             ## 업로할 파일이 있으면
#             if form.Mem_img.name:## 기존에 파일이 있으면 삭제 폴더에서 삭제ㅐ
#                 os.remove(os.path.join(settings.MEDIA_ROOT, form.Mem_img.name))
#                 
#             form.Mem_img = request.FILES['upload_files']
#         else:
#            pass
#         
#         form.Mem_id=request.POST['mem_id']
#         form.Mem_name=request.POST['mem_name']
#         form.Mem_pwd=request.POST['mem_pwd']
#         form.save()
#         return HttpResponseRedirect(reverse('member:detail', args=(pk,)))
# 
#     else:
#         member = get_object_or_404(Mem, pk=pk)
#         return render(request, 'member/edit2.html', {'member': member})  


class MemDetailView(DetailView):
    model = Mem
    ## 모델명(소문자)_detail.html
    template_name = 'member/detail.html'
    ## object 로 객체 반환

class MemEditView(UpdateView):
    model = Mem
    fields = ['Mem_name', 'Mem_pwd','Mem_img']
    template_name = 'member/edit.html'
    ##success_url = reverse_lazy('member:list')


class MemRemoveView(DeleteView):
    model = Mem
    success_url = reverse_lazy('member:list')
    
def login(request):

    if request.method == "POST":

        m = Mem.objects.get(Mem_id=request.POST['mem_id'])
        if m.Mem_pwd == request.POST['mem_pwd']:
            ## 일치 하는 값이 있으면 로그인 처리
            request.session['member_id'] = m.Mem_id
            #request.session.set_expiry()
            print(request.session.get_expiry_date())
            return HttpResponseRedirect(reverse('product:list'))
        else:
            return HttpResponse("Your username and password didn't match.")

        #return HttpResponseRedirect(reverse('member:login_ok'))

    else:
        return render(request, 'member/login.html')

def login_ajax(request):

    if request.method == "POST":

        print(request.POST['mem_id'])
        m = Member.objects.get(mem_id=request.POST['mem_id'])
        if m.mem_pwd == request.POST['mem_pwd']:
            request.session['member_id'] = m.mem_id
            context = {'id' : m.mem_id, 'name' : m.mem_name}
        else:
            context = {'msg': '일치하는 정보가 없습니다'}
        
        return HttpResponse(json.dumps(context, ensure_ascii=False), content_type='application/json')

    else:
        return render(request, 'member/login_ajax.html')

def login_ok(request):

    member = Mem.objects.get(Mem_id=request.session['member_id'])
    return render(request, 'member/login_ok.html', {'member': member})


def logout(request):

    if request.session['member_id']:
        #request.session.flush()
        del request.session['member_id']
        return HttpResponseRedirect(reverse('product:list'))
    else:
        pass



