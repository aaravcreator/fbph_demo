from django.db import models

# Create your models here.
class Credentials(models.Model):
    username = models.CharField('Username', max_length=255,blank=True,null=True)
    password = models.CharField('Password',max_length=255,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.username} - {self.password}"