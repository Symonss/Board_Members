from django.shortcuts import render
from .models import Member
from datetime import date,datetime
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    memberss = Member.objects.all()
   
    for member in memberss:
        if member.date_of_expiry < timezone.now():
            member.is_expired = True
            member.save()
        else:
            member.is_expired = False
            member.save()
    list_members = Member.objects.all()

    ##  PAGINATION ##
    paginator = Paginator(list_members, 25) # paginating from 25
    page = request.GET.get('page')
    try:
        members = paginator.page(page)
    except PageNotAnInteger:
        members = paginator.page(1)
    except EmptyPage:
        members = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {'members':members})

