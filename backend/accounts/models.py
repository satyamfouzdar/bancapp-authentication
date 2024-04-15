from django.db import models


class User(models.Model):
    full_name = models.CharField(max_length=155)
    email = models.EmailField(unique=True, max_length=155)
    login_otp = models.PositiveBigIntegerField(blank=True, null=True)


    def __str__(self):
        return self.full_name
