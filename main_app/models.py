from django.db import models
from django.urls import reverse


class Award(models.Model):
    name = models.CharField(max_length=50)
    img_path = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('awards_detail', kwargs={'pk': self.id})


class Character(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    starred_in = models.CharField(max_length=100)
    image_path = models.CharField(max_length=200)
    awards = models.ManyToManyField(Award)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'character_id': self.id})

class Token(models.Model):
    date = models.DateField('token date')
    character = models.ForeignKey(
        Character,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.date}'

    class Meta:
        ordering = ['-date']
        
    
