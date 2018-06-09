# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required, permission_required
from django_currentuser.middleware import get_current_authenticated_user as curr_logged
from .forms import ConnectionForm, VaccineSearch
from .models import Connection, Vaccine, Branch



def index(request):
    return render(request, 'base.html')


@login_required
@permission_required('vaxmgr.can_change_connection', raise_exception=True)
def connection_view(request):
    if request.method == 'POST':
        form = ConnectionForm(request.POST)
        if form.is_valid():
            try:
                conn = Connection.objects.get(vaccine_id=form.cleaned_data['vaccine'],
                                              branch_id=form.cleaned_data['branch'])
                conn.amount = form.cleaned_data['amount']
                conn.modified_by = curr_logged()
                conn.save()
            except ObjectDoesNotExist:
                form.save()
        return HttpResponseRedirect(reverse('success'))
    else:
        form = ConnectionForm()
    return render(request, 'connection.html', {'form': form})

@login_required
def search(request):
    request.encoding = 'utf-8'
    if request.method == 'GET':
        form = VaccineSearch(request.GET)
        vacc = Connection.objects.none()
        if form.is_valid() and (form.cleaned_data['name'] 
                                or form.cleaned_data['branch']
                                or form.cleaned_data['illness']):
            if form.cleaned_data['branch'] == None:
                form.cleaned_data['branch'] = ''
            vacc = Connection.objects.filter(vaccine__name__contains=form.cleaned_data['name'],
                                             branch__name__contains=form.cleaned_data['branch'],
                                             vaccine__illness__contains=form.cleaned_data['illness'])
            form = VaccineSearch()
    return render(request, 'search.html', {'form': form, 'vacc': vacc.order_by('vaccine__name')})


def success(request):
    return render(request, 'success.html')


def error403(request, exception):
    return HttpResponseForbidden(render(request, 'errors/403.html'))


@login_required
@permission_required('vaxmgr.can_change_connection', raise_exception=True)
def db_update(request):
    for vacc in Vaccine.objects.all():
        for branch in Branch.objects.all():
            conn = Connection(vaccine=vacc, branch=branch, amount=100)
            conn.save()
    return redirect('index')
