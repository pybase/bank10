from django.shortcuts import render

from bank_app.models import Bank, Members



# Create your views here.
def index(request):
    bank=Bank.objects.all()
    members=Members.objects.all()
    return render(request,'index.html',{'bank':bank,'members':members})

def details(request):
    return render(request,'details.html')

def form(request):
    name="Application form"
    return render(request,'form.html',{'name':name})

