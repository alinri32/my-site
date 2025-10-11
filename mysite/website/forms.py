from django.forms import ModelForm

from website.models import contact , newsletter

class contactform(ModelForm):
    class Meta:
        model = contact
        fields = '__all__'

class newsletterform(ModelForm):
    class Meta:
        model = newsletter
        fields = '__all__'
