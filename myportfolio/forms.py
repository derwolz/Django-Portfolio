from django import forms
from .models import CSTag
    
class ProjectFilterForm(forms.Form):
    csobjects = CSTag.objects.all()
    _list = []
    for item in csobjects:
        _list.append((item, item))
    _list = tuple(_list)
    
    filters = forms.MultipleChoiceField(choices=_list, 
        widget=forms.CheckboxSelectMultiple(attrs={'placeholder': 'Filters', 
            'class': 'form-grid my-auto mx-1 '}), label='')
    fields = 'filters'
    
class ProspectForm(forms.Form):
    Name = forms.CharField(required=True,
        max_length=128, initial='Name', label='')
    Sender = forms.EmailField(label='', initial='Email')
    Company = forms.CharField(required=False, max_length=128, initial='Company', label='')
    Message = forms.CharField(required=True,
        min_length=30,
        widget=forms.Textarea,
        max_length=2048, label='', initial='ShortMessage')
    