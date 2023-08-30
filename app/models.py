from django.db import models

# Create your models here.
class Xusers(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Role = models.CharField(max_length=100)
    class Meta:
        db_table = 'Users'