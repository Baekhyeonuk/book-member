from django.shortcuts import render, redirect, get_object_or_404
from member.models import Mem
from django.contrib import messages

def mem_check(request):

    try:
        request.session['Mem_id']
    except KeyError:        
        return messages.warning(request, "로그인 후 이용하세요")
    else:
        return get_object_or_404(Mem, Mem_id=request.session['Mem_id'])
    
