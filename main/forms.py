from django import forms
from .models import testData, users, positions, comments
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
            'user':selectPlusWidget.selectPlus(baseURL="/users"),
            'comment':selectPlusWidget.selectPlus(baseURL='/comment')
        }
  
class formBuildUser(forms.ModelForm):
    class Meta:
        model=users
        fields=(
           
            'name',
            'position',
        )
        position=forms.ModelChoiceField(queryset=positions.objects.all(),to_field_name='positions')
        widgets={
            'position':selectPlusWidget.selectPlus(baseURL="/positions")
        }
class formBuilderComment(forms.ModelForm):
    class Meta:
        model=comments
        fields=(
            'comment',
        )
        
class formBuilderPositions(forms.ModelForm):
    class Meta:
        model=positions
        fields=(
            'positions',
        )
