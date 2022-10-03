from django.shortcuts import render,redirect
from .models import Grant
import pandas as pd
import datetime
from . forms import CreateProjectForm

from datetime import date

today = date.today()

# dd/mm/YY
d1 = today.strftime("%Y-%m-%d")
year=today.strftime("%Y")
month= today.strftime("%m")
year= float(year)
month= float(month)
current_year_month=round(month/12,3)+year

def progress(col):
    if col< current_year_month:
        return 'Completed'
    elif col == current_year_month:
        return 'To be completed this month'
    else:
        return 'In Progress'


def comp(col):
    if col >100:
        return 100
    else:
        return col
# Create your views here.def \

def home(request):

    return render(request,'home.html',{})

def grant(request):
    all_grants=Grant.objects.all()
    grants=Grant.objects.all().values()

    df= pd.DataFrame(grants)

    # working on years and months
   

    df['year_start']= df['project_start'].apply(lambda x: x.strftime('%Y-%m-%d')).str.extract(r'([0-9]{4})\S[0-9]{2}\S[0-9]{2}')
    df['month_start']= df['project_start'].apply(lambda x: x.strftime('%Y-%m-%d')).str.extract(r'[0-9]{4}\S([0-9]{2})\S[0-9]{2}')
    df['year_end']= df['project_end'].apply(lambda x: x.strftime('%Y-%m-%d')).str.extract(r'([0-9]{4})\S[0-9]{2}\S[0-9]{2}')
    df['month_end'] = df['project_end'].apply(lambda x: x.strftime('%Y-%m-%d')).str.extract(r'[0-9]{4}\S([0-9]{2})\S[0-9]{2}')

    df['year_start']=df['year_start'].astype(int)
    df['month_start']=df['month_start'].astype(float)
    df['year_end']=df['year_end'].astype(float)
    df['month_end']=df['month_end'].astype(float)
    df['year_month_start']=round(df['month_start']/12,3) + df['year_start']
    df['year_month_end']=round(df['month_end']/12,3) + df['year_end']


    df['Progress'] = df['year_month_end'].apply(progress)
    df['completion_todate'] = current_year_month-df['year_month_start']
    df['total_time'] = df['year_month_end']-df['year_month_start']
    df['completion'] = round((df['completion_todate']/df['total_time'])*100,2)

    df['completion'] = df['completion'].apply(comp)
    df['Duration(in months)'] = round(df['total_time']*12)

    return render(request,'grants/grant.html', {'df':df.to_html,'all_grants':all_grants })


def register_project(request):
    forms=CreateProjectForm
    if request.method== 'POST':
        forms=CreateProjectForm(request.POST,request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('home')
        
    else:

        forms=CreateProjectForm()
    context={
        'forms':forms,
        
    }
    return render(request,'grants/add_grants.html',context)

def update_grants(request,grant_id):
    grants=Grant.objects.get(pk=grant_id) 
    forms=CreateProjectForm(instance=grants)
    if request.method=='POST':
        forms=CreateProjectForm(request.POST,request.FILES,instance=grants)
        if forms.is_valid():
            forms.save()
            return redirect('submitted')  
    return render(request,'grants/update_grants.html',{'grants':grants,'forms':forms})

def submisionform(request):
    return render(request,'grants/submit.html',{})