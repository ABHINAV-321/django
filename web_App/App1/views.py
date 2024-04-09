from django.shortcuts import render
from django.http import HttpResponse
import json
from . models import movie
from . form import movie_form

# Create your views here.
def print_log(request) :
  if request.POST:
    frm=movie_form(request.POST)
    print('\n working \n')
    if frm.is_valid:
      frm.save()
    
  print('woekingggggggg')
  movies = movie.objects.all
  print(movie.objects.all)
  return render(request,'App1.html',{"movies":movies})
  #return HttpResponse('hi')

def form(request):
  frm=movie_form()
  
  #  data = json.loads(request.body.decode())
  ''' 
    print(request.POST)
    movies={'movies':[{'title':request.POST.get('title'),'year':request.POST.get('year')}]}
    movie_obj=movie(title=request.POST.get('title'),year=request.POST.get('year'))
    movie_obj.save()'''
  return render(request,'App1.html')
    

    # TODO: missing a suitable `content-type` header check
    

  return render(request,'form.html',{'frm':frm})
  
'''def form_sub(request):
  
   # if request.post :
  print('hi')
  print(request.POST)
  
  return render(request,'App1.html',request.POST)
'''