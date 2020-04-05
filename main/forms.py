from django import forms
from .models import testData, users
from .testLab.SelectPlus import selectPlusWidget

class formSelectPlus(forms.ModelForm):
    class Meta:
        model=testData
        method="POST"
        fields=(
            'date',
            'value',
            'template',
            'user',
            'comment',
        )
        
        widgets={
            'user':selectPlusWidget.selectPlus(baseURL="users")
        }
class formBuildUser(forms.ModelForm):
    class Meta:
        model=users
        fields=(
            'name',
            'position'
        )
        widgets={
            'position':selectPlusWidget.selectPlus(baseURL="positions")
        }