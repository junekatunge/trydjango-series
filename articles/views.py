from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Articles
from .forms import ArticlesForm

# Create your views here.

def articles_search_view( request):
    
 
    query_dict = request.GET # to extract the data in the query we use a dictonary
    query = query_dict.get("q")
    
    try:#only accept int values
        query=int(query_dict.get("q")) 
    except:#if not an int query show no results
        query = None
    
    articles_obj = None
    if query is not None:
        articles_obj=Articles.objects.get(id=query)
   
    context = {
        "object": articles_obj,
    }

    return render(request, "articles/search.html", context=context)

#@login_required
def articles_create_view(request):
    #print(request.POST)
    form= ArticlesForm()
    print(dir(form))#print out the directory of the form
    context = {
        "form" : form
    }
    if request.method == 'POST':
        title= request.POST.get('title')#get here helps to get the form so that data can be posted in db
        content= request.POST.get('content')
        print(title,content)
        articles_object = Articles.objects.create(title=title, content=content)
        context['object'] = articles_object
        context['created'] = True
    return render(request,"articles/create.html", context=context)



def articles_detail_view(request, id=None):
    articles_obj = None
    if id is not None:
        articles_obj=Articles.objects.get(id=id)
   
    context = {
        "object": articles_obj,
    }


    return render(request,"articles/detail.html", context={})