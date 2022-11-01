from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Department)
admin.site.register(models.Score)
admin.site.register(models.DataBottle)
admin.site.register(models.HistoryEvaluate)
