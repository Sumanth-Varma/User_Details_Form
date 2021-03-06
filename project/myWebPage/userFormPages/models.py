from django.db import models

# Create your models here.
class UserDetails(models.Model):
    user_id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    user_email = models.EmailField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.name)