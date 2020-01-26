
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from .models import Member, Position, Institutional
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
# from ..forms import TicketUpdateForm




class TickeCreateView(CreateView):
    model = Member
    fields = ('name','institutional','position','status','appointment_schedule','date_of_appointment','date_of_expiry','gazetted_by')
    template_name = 'member_add_form.html'

    def form_valid(self, form):
        member = form.save(commit=False)
        member.save()
      
        return redirect('home')
class PosCreateView(CreateView):
    model=Position
    fields=('name',)
    template_name='position.html'
    def form_valid(self, form): 
        position = form.save(commit=False)
        position.save()
      
        return redirect('home')

class InsCreateView(CreateView):
    model=Institutional
    fields=('name',)
    template_name='institutional.html'
    def form_valid(self, form): 
        position = form.save(commit=False)
        position.save()
       
        return redirect('home')

def member_detail(request, pk):
    ticket = get_object_or_404(Member, pk=pk)
    return render(request, 'member_detail.html', {'member': member})
