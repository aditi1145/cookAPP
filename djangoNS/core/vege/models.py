from django.db import models

# Create your models here.
class Receipe(models.Model):
    receipe_image=models.ImageField(upload_to="receipe")
    receipe_name=models.CharField(max_length=100)
    receipe_ingredients=models.TextField()
    steps_to_follow=models.TextField()
    
    