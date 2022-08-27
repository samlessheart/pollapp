from asyncore import poll
from django.contrib import admin

from .models import Poll, Profile, Answers
# Register your models here.


admin.site.register(Poll)
admin.site.register(Profile)
admin.site.register(Answers)
