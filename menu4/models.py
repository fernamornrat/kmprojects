from django.db import models

class Comment(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    comment = models.TextField()

    def __str__(self): 
        return self.username