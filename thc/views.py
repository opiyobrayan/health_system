from django.shortcuts import render

from .models import Workplan,Partner
from django.shortcuts import render, get_object_or_404
from django.http import FileResponse
# Create your views here.
def home(request):

    return render(request,'home.html',{})

def workplan(request):
    workplans = Workplan.objects.all()
    return render(request, 'workplan.html', {'workplans': workplans})
def view_pdf(request, pk):
    workplan = get_object_or_404(Workplan, pk=pk)
    response = FileResponse(workplan.pdf.open(), content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="%s"' % (workplan.pdf.name)
    return response

# views.py
from django.shortcuts import render
import openpyxl

def display_excel(request):
    workplan = Workplan.objects.get(pk=1)
    wb = openpyxl.load_workbook(workplan.pdf.path)
    sheet = wb.active
    data = []
    for row in sheet.iter_rows():
        data_row = []
        for cell in row:
            data_row.append(cell.value)
        data.append(data_row)
    return render(request, 'display_excel.html', {'data': data})
def activity(request):
    return render(request, 'activity.html', {})
def add_activity(request):
    return render(request, 'add_activity.html', {})

def partners(request):
    all_partners=Partner.objects.all()
    return render(request,'partners.html',{'all_partners':all_partners})
