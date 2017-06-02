from django import forms
from .models import Report, Feedback

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('contents','image')


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('title', 'contents')