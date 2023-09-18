from django.db import models
from djmoney.models.fields import MoneyField
# from star_ratings.models import Rating


class Trainer(models.Model):
    trainer_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)


class Session(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    rating = models.IntegerField(default=0)
