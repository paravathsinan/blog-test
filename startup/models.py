from django.db import models
from user.models import User


class Blog(models.Model):
    heading = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering =['-id']
    
    def __str__(self):
        return self.heading
    