from django.contrib import admin
from .models import Question, Choice  # Import the models you want to register

# Register your models here
admin.site.register(Question)
admin.site.register(Choice)
