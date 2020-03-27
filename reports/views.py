from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Report
from django.contrib.auth.decorators import login_required
from . import forms

def report_list(request):
    reports = Report.objects.all().order_by('date')
    return render(request, 'reports/report_lists.html', { 'reports': reports })

def report_detail(request, slug):
    report = Report.objects.get(slug=slug)
    return render(request, 'reports/report_detail.html', { 'report': report})

@login_required(login_url="/accounts/login/")
def report_create(request):
    form = forms.CreateReport()
    if request.method == 'POST':
        form = forms.CreateReport(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save
            return redirect('reports:list')
    else:
        form = forms.CreateReport()
    return render(request, 'reports/report_create.html', { 'form': form })
