from django import forms
from django.core.exceptions import ValidationError


class Userform(forms.Form):
    email = forms.EmailField()
    user_id = forms.CharField(max_length=10)
    user_name = forms.CharField(max_length=64)
    password = forms.CharField(max_length=64)

    user_qd = forms.IntegerField()
    user_class = forms.IntegerField()
    dorm_num = forms.CharField(max_length=3)
