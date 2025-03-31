from django.db import models


class Question(models.Model):
    # ...
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    # ...
    def __str__(self):
        return self.choice_text


# Модель устройства
class Device(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Модель записи скорости и точности
class SpeedRecord(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    speed = models.IntegerField()
    accuracy = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.device.name}: {self.speed} WPM ({self.accuracy:.2f}%)"