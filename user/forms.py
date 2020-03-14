from django.forms import ModelForm
from user.models import EventRegistration

class EventRegistrationForm(ModelForm):
    class Meta:
        model = EventRegistration
        fields = '__all__'