from django import forms
from .models import Subscriber

# ModelForm version
class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ["name", "email"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if Subscriber.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already subscribed!")
        return email

# Manual Form version
class ManualSubscriberForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get("email")
        from .models import Subscriber
        if Subscriber.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already subscribed!")
        return email
