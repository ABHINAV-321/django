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
  return render(request,'form.html',{'frm':frm})
    

    # TODO: missing a suitable `content-type` header check
    

  return render(request,'form.html',{'frm':frm})
  
'''def form_sub(request):

  
   # if request.post :
  print('hi')
  print(request.POST)
  
  return render(request,'App1.html',request.POST)
'''

def edit(request,pk):
  instance =movie.objects.get(id=pk)
  frm=movie_form(instance=instance)
  if request.POST:
    title=request.POST.get('title')
    year=request.POST.get('year')
    
   
    movie.objects.filter(id=pk).update(title=title,year=year)
    
    return print_log(request)
  return render(request,'form.html',{'frm':frm})



def delete(request,pk):
  print('delete')
  instance =movie.objects.get(id=pk)
  instance.delete()
  return print_log(request)
 # movies = movie.objects.all
 # return render(request,'App1.html',{"movies":movies})