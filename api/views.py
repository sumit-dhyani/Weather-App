
from django.http import HttpResponse
from django.shortcuts import render,redirect
import requests,json

# Create your views here.
def home(request):
    context={
            'name':'',
            'weather':'',
            'flag':'',
        }
    if request.method=='POST':
        
        city_name=request.POST.get('city',False)
        APIKey="7dd468783d617aafcdb27e1e39db2ea6"
        url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={APIKey}'
        try:
            response=requests.get(url)
            data=response.json()
            
            context={
            'country':data['sys']['country'],
            'temp':int((data['main']['temp'])-272.15),
            'weather':data['weather'][0]['main'],
            'city':city_name}
        except: 
            context['flag']='what'
    
        
    return render(request,'index.html',context)
    
def redirect1(request):
    return (redirect,'https://www.github.com/sumit-dhyani')
def weather(request):
    
    return HttpResponse("ok")