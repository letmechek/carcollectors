from django.db import models
from django.urls import reverse

SIZE =(
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large')
)

class Rim(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('rims_detail', kwargs={'pk': self.id})


class Car(models.Model):
    model = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()
    rims = models.ManyToManyField(Rim)

    def __str__(self):
        return self.model

    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})

    def supplied_for_today(self):
        return self.tire_set.filter(date=date.today().count() >= len(SIZE))
        
class Tire(models.Model):
    date = models.DateField(' date')
    size = models.CharField(
        max_length=1,
        choices=SIZE,
        default=SIZE[0][0]
    )

    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.get_size_display()} on {self.date}'

    class Meta:
        ordering = ['-date']
