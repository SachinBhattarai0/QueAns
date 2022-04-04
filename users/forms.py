from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import profiles
from django.forms import ModelForm


class customUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username','password1','password2']
        

    def __init__(self, *args, **kwargs):
        super(customUserCreationForm,self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class':'input','placeholder':'Enter Username'})
        self.fields['password1'].widget.attrs.update({'class':'input','placeholder':'Enter password'})
        self.fields['password2'].widget.attrs.update({'class':'input','placeholder':'Confirm password'})


class profileForm(ModelForm):
    class Meta:
        model=profiles
        fields =['name','email','short_intro','bio','profile_pic','facebook_link','linkedin_link','twitter_link']
    def __init__(self,*args,**kwargs):
        super(profileForm,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})
