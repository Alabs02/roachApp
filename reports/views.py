from django.shortcuts import render
from .models import Report

def report_list(request):
    reports = Report.objects.all().order_by('date')
    return render(request, 'reports/report_lists.html', { 'reports': reports })
