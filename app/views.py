from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):

    if request.method=="POST":
        topics=request.POST['topic']
        to=Topic.objects.get_or_create(topic_name=topics)[0]
        to.save()
        return HttpResponse('topic data inserted successfully')
    return render(request,'insert_topic.html')


def insert_webpage(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    
    if request.method=='POST':
        topic=request.POST['topic']
        na=request.POST['na']
        ur=request.POST['ur']
        T=Topic.objects.get_or_create(topic_name=topic)[0]
        T.save()
        W=Webpage.objects.get_or_create(topic_name=T,name=na,url=ur)[0]
        W.save()
        return HttpResponse('data inserted to webpage successfully')
    return render(request,'insert_webpage.html',d)

def insert_access(request):
    topics=Topic.objects.all()
    d={'topics':topics}

    if request.method=='POST':
        topic=request.POST['topic']
        na=request.POST['name']
        ur=request.POST['ur']
        da=request.POST['da']
        T=Topic.objects.get_or_create(topic_name=topic)[0]
        T.save()
        W=Webpage.objects.get_or_create(topic_name=T,name=na,url=ur)[0]
        W.save()
        A=AccessRecords.objects.get_or_create(name=W,date=da)[0]
        A.save()
        return HttpResponse('inserted data into accesss successfully')
    return render(request,'insert_access.html',d)

def select_topics(request):
    Topics=Topic.objects.all()
    d={'Topics':Topics}
    if request.method=='POST':
        tn=request.POST.getlist('topic')
        print(tn)
        webpages=Webpage.objects.none()
        for i in tn:
            webpages=webpages|Webpage.objects.filter(topic_name=i)
            data={'webpages':webpages}
            return render(request,'display_webpage.html',data)
    return render(request,'select_topics.html',d)

def checkbox(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    
    return render(request,'checkbox.html',d)