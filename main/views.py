from django.shortcuts import render
from .models import testData
from .forms import formSelectPlus,formBuildUser

def testPage(request):
    form=formSelectPlus()
    return render(request,'test.html',{'form':form})

def buildUserPage(request):
    form=formBuildUser()
    return render(request,'builderUser.html',{'form_user':form})