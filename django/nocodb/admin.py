from django.contrib import admin

from .models import Question, Choice,Device,SpeedRecord


admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Device)
admin.site.register(SpeedRecord)