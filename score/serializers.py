from rest_framework.serializers import ModelSerializer
from . import models

class DepartmentSerialze(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Department