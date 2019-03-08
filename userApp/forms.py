from django import forms

class UserForm(forms.Form):
    username=forms.CharField(
        required=True,
        max_length=20,
        min_length=3,
        error_messages={
            'required': '请输入用户名',
            'max_length': '超出字符长度',
            'min_length':'没达到字符长度'
        })
    password=forms.CharField(
        required=True,
        max_length=20,
        min_length=3,
        error_messages={
            'required':'请输入用户密码',
            'max_length': '超出字符长度',
            'min_length':'没达到字符长度'
        })
