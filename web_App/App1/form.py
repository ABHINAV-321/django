from django.forms import ModelForm
from . models import movie

class movie_form(ModelForm):
    class Meta:
        model=movie
        fields = '__all__'