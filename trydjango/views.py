"""
to render html web pages

"""
from articles.models import Articles
from django.http import HttpResponse
import random
from django.template.loader import render_to_string #for string substitution




def home_view(request, *args, **kwargs ):

    """
    take in a request 
    return html as a response
    """
  
    name= 'june'
    random_id=random.randint(1,2)

    #from database
    articles_obj=Articles.objects.get(id=random_id)#getting a single object from database
    articles_queryset=Articles.objects.all()#geting a list of objects in the database, this is also a queryset
    context={
        "object_list": articles_queryset,#if you wnt to render out list
        "title": articles_obj.title,
        "id":articles_obj.id,
        "content":articles_obj.content
    }

    HTML_STRING = render_to_string("home_view.html",context=context)
   
    return HttpResponse(HTML_STRING)