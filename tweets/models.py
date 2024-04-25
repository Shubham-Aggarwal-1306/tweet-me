from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL

class Tweet(models.Model):
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # def __str__(self):
    #     return self.content
    class Meta:
        ordering = ['-id']
    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "likes": 12
        }