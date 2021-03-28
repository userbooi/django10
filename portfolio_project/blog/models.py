from django.db import models

# Create your models here.
class Topic(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if len(self.title) > 40:
            return f'{self.title[:40]}...'
        else:
            return self.title
