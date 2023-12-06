from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=20, null=False, unique=True)
    email = models.EmailField(unique=True)
    created_time = models.DateTimeField(auto_now_add=True, editable=False)
    notes = models.TextField(max_length=200, default="")
