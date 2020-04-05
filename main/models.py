from django.db import models
class positions(models.Model):
    positions=models.CharField(max_length=128)
class users(models.Model):
    name=models.CharField(max_length=128)
    position=models.ForeignKey(positions,on_delete=models.SET_NULL,null=True)

class comments(models.Model):
    comment=models.CharField(max_length=128)

class testData(models.Model):
    date=models.DateTimeField()
    value=models.IntegerField()
    template=models.CharField(max_length=128)
    user=models.ForeignKey(users,on_delete=models.SET_NULL,null=True)
    comment=models.ForeignKey(comments,on_delete=models.SET_NULL,null=True)

