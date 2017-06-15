from django import forms
from map.models import Map
class HomeForm(forms.ModelForm):
    title = forms.CharField()
    post = forms.CharField()
    longitude = forms.FloatField()
    latitude = forms.FloatField()
    width = forms.IntegerField(required=False)
    height = forms.IntegerField(required=False)
   


    class Meta:
        model = Map
        fields = ('post','title','longitude','latitude','width','height')

