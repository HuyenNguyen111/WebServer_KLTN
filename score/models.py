from django.db import models
from django.utils import timezone
# Create your models here.


class Deparment(models.Model):
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
    deparment = models.ForeignKey(Deparment, on_delete=models.CASCADE)
    createAt = models.DateTimeField(default=timezone.now)
    updateAt = models.DateTimeField(default=timezone.now)
    note = models.TextField()
    score = models.FloatField()
    status = models.IntegerField()  # 0: chưa nhập điểm. 1: đã nhập
    endAt = models.DateField(null=True, blank=True)
