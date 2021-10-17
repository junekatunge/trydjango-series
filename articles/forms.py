from django import forms

class ArticlesForm(forms.Form):
    content =  forms.CharField()
    title = forms.CharField()
    
     