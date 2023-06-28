from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.functions import Length

# Create your views here.
from app.models import *
from django.db.models import Q
def display_topics(request):
    topics=Topic.objects.all()
    #topics=Topic.objects.all().order_by('topic_name')
    #topics=Topic.objects.all().order_by(Length('topic_name'))
    #topics=Topic.objects.all()[4::]
    #topics=Topic.objects.filter(topic_name='Cricket')
    #topics=Topic.objects.exclude(topic_name='Cricket')
    
    d={'topics':topics}
    return render(request,'display_topics.html',d)
     

def display_webpage(request):
    webpage=Webpage.objects.all()
    #webpage=Webpage.objects.all().order_by('name')
    #webpage=Webpage.objects.all().order_by(Length('name').desc())
    #webpage=Webpage.objects.filter(url__startswith='http')
    #webpage=Webpage.objects.filter(name__endswith='l')
    #webpage=Webpage.objects.filter(Topic_name__contains='f')
    #webpage=Webpage.objects.all()[::2]
    #webpage=Webpage.objects.filter(name='Dhoni')
    #webpage=Webpage.objects.exclude(topic_name='Rummy')
    #webpage=Webpage.objects.filter(name__in=['sunil','suneel'])
    #webpage=Webpage.objects.filter(Q(name='sunil') & Q(url__startswith='http'))
    #webpage=Webpage.objects.filter(Q(name='mani') | Q(url__startswith='https'))



    d={'webpage':webpage}
    return render(request,'display_webpage.html',d)
    
     

def display_accessrecords(request):
   
    accessrecords=AccessRecords.objects.all()
    #accessrecords=AccessRecords.objects.all().order_by(Length('authour'))
    #accessrecords=AccessRecords.objects.all().order_by('authour')
    #accessrecords=AccessRecords.objects.all()[::-1]
    #accessrecords=AccessRecords.objects.filter(date__gte='2023-06-23')
    #accessrecords=AccessRecords.objects.filter(date__day='23')
    #accessrecords=AccessRecords.objects.filter(date__year__gt='1999')
    #accessrecords=AccessRecords.objects.filter(authour='gani')
    #accessrecords=AccessRecords.objects.exclude(authour='csk')

    
    d={'accessrecords':accessrecords}
    return render(request,'display_accessrecords.html',d)



def update_webpage(request):
    #Webpage.objects.filter(name='suneel').update(url='http://msd.com')
    #Webpage.objects.filter(topic_name='Rummy').update(url='http://rummy.com')
    #Webpage.objects.filter(name='suneel').update(toipc_name='Rummy')
    Webpage.objects.update_or_create(topic_name='football',defaults={'url':'http://ronaldo.com'})
    #Webpage.objects.update_or_create(name='vineeth',defaults={'url':'http://vinni.com'})
    #Webpage.objects.update_or_create(topic_name='hardik')

    #CTO=Topic.objects.get(topic_name='Cricket')
    #Webpage.objects.update_or_create(name='Dhoni',defaults={'topic_name':CTO})
    #Webpage.objects.update_or_create(name='Pandya',defaults={'topic_name':CTO,'url':'http://pandya.com'})
    
    webpage=Webpage.objects.all()
    d={'webpage':webpage}
    return render(request,'display_webpage.html',d)
    

def delete_webpage(request):
    Webpage.objects.filter(name='Pandya').delete()
    Webpage.objects.filter(name='suneel').delete()

    webpage=Webpage.objects.all()
    d={'webpage':webpage}
    return render(request,'display_webpage.html',d)