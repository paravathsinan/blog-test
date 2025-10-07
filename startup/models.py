from django.db import models



class Blog(models.Model):
    heading = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.heading
    