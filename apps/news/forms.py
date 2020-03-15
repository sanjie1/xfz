from django import forms
from apps.forms import FormMixin
from .models import Banner

class PublicCommentForm(forms.Form,FormMixin):
    content = forms.CharField()
    news_id = forms.IntegerField()

