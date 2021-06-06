from django.db import models


class Testdb1(models.Model):
    node = models.CharField(max_length=250)
    volume = models.IntegerField()

    def __str__(self) -> str:
        return self.node


class Testdb2(models.Model):
    node = models.CharField(max_length=250)
    isOn = models.BooleanField()

    def __str__(self) -> str:
        return self.node