from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class ProfilePic(models.Model):
    avatar = models.ImageField(upload_to='avatars')
    thumbnail = ImageSpecField(
      source='avatar',
      processors=[ResizeToFill(100, 50)],
      format='JPEG',
      options={'quality': 80})
    
    #smart = ImageSpecField(source='avatar', processors=[SmartResize(50,50)], format='JPEG')


