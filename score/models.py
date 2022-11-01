from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class Department(models.Model):
    """
        Bảng lưu thông tin khoa/viện
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Score(models.Model):
    """
        Bảng lưu điểm số
    """
    numItem = models.IntegerField()
    score = models.FloatField()


class DataBottle(models.Model):
    """
        Bảng lưu thông tin sinh viên, số lượng chai, điểm
        - xuất excel từ bảng này
    """
    name = models.CharField(max_length=500, blank=False)
    studentID = models.CharField(max_length=10, blank=False)
    quantity = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    createAt = models.DateTimeField(default=timezone.now)
    updateAt = models.DateTimeField(default=timezone.now)
    note = models.TextField(blank = True)
    score = models.FloatField()
    status = models.IntegerField()  # 0: chưa nhập điểm. 1: đã nhập
    endAt = models.DateField(null=True, blank=True)


class HistoryEvaluate(models.Model):
    createAt = models.DateTimeField(default=timezone.now)
    quantityStudent = models.IntegerField()
    evaluator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    dataBottle = ArrayField(models.BigIntegerField(), size=200)
