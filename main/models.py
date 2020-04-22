from django.db import models
class positions(models.Model):
    positions=models.CharField(max_length=128)
class users(models.Model):
    name=models.CharField(max_length=128,name='name')
    position=models.ForeignKey(positions,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.name

class comments(models.Model):
    comment=models.CharField(max_length=128)
    def __str__(self):
        return self.comment

class testData(models.Model):
    date=models.DateTimeField()
    value=models.IntegerField()
    template=models.CharField(max_length=128)
    user=models.ForeignKey(users,on_delete=models.SET_NULL,null=True)
    comment=models.ForeignKey(comments,on_delete=models.SET_NULL,null=True)

