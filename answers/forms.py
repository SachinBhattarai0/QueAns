from django.forms import ModelForm
from .models import questions

class questionForm(ModelForm):
    class Meta:
        model = questions
        fields = '__all__'
        exclude = ['answered','questioner']

    def __init__(self,*args,**kwargs):
        super(questionForm,self).__init__(*args,**kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})