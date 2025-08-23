# students/forms.py
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll_no', 'grade', 'is_active']

    def clean_roll_no(self):
        roll_no = self.cleaned_data['roll_no']
        if not roll_no.isdigit():
            raise forms.ValidationError("Roll number must be numeric.")
        return roll_no
