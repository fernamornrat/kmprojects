from django.db import models

class Event(models.Model):
    TYPES_CHOICES = (
                        ('การประชุม', 'Meeting'),
                        ('การฝึกอบรม', 'Training'),
                        ('การสัมมนา', 'Seminar'),
                        ('การเสวนา', 'Converse'),
    )
    types = models.CharField(max_length=50, choices=TYPES_CHOICES)
    name = models.CharField(max_length=500)
    detail = models.TextField()
    date = models.DateField()
    from_time = models.TimeField()
    to_time = models.TimeField()
    locality = models.CharField(max_length=500)
    link = models.URLField()

    def __str__(self): 
        return self.name


class Register(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    email = models.CharField(max_length=254)
    phone = models.CharField(max_length=10)

    def __str__(self): 
        return self.first_name