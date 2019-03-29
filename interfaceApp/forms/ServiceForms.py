from django import forms

class ServiceForm(forms.Form):
    parent = forms.IntegerField(required=True, )
    name=forms.CharField(
        required=True,
        max_length=200,
        min_length=1,
        error_messages={
            'required': '请输入服务名',
        })
    description=forms.CharField(
        required=False,
        min_length=1,)
    parent = forms.IntegerField(required=True, )
