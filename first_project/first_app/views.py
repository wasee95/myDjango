from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord

# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    my_dict = {"index1":webpages_list}
    my_dict = {'insert_me':"Now im coming from first_app/index.html!"}
    return render(request,'first_app/index.html',context=date_dict)
    
def index1(request):
    return render(request,'first_app/index1.html')

def audio(request):
    return render(request,'first_app/audio.html')
