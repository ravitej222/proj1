from django import forms
from app1.models import course


class courseform(forms.ModelForm):
    class Meta:
        model = course
        fields = ['cname','fee','dur','trainer']

        
class courseform2(forms.Form):
    cname = forms.CharField(max_length=25,label='course',initial='python')
    fee = forms.IntegerField()    
    dur = forms.IntegerField(label='duration')
    trainer = forms.CharField(max_length=25,required=True)