from django.contrib import admin
from .models import testData,users,comments, positions

admin.site.register(testData)
admin.site.register(users)
admin.site.register(comments)
admin.site.register(positions)
