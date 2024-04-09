from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def print_log(request) :
  print('woekingggggggg')
  movies = {'movies':[{'title':'thor','year':2000,'img':'IMG-20240402-WA0007.jpg'},{'title':'love','year':2006,'img':'null-20240404-WA0000.jpg'}]}
  return render(request,'App1.html',movies)

def form(request):
  if request.POST:
    print('\n working \n')
    
  #  data = json.loads(request.body.decode())
    print(request.POST)
    movies={'movies':[{'title':request.POST.get('title'),'year':request.POST.get('year')}]}
    

    return render(request,'App1.html',movies)
    

    # TODO: missing a suitable `content-type` header check
    

  return render(request,'form.html')
  
'''def form_sub(request):
  
   # if request.post :
  print('hi')
  print(request.POST)
  
  return render(request,'App1.html',request.POST)
'''