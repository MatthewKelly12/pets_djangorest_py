from django.db import models

class Types(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Pets(models.Model):
    name = models.CharField(max_length=50)
    types = models.ForeignKey(Types, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Owners(models.Model):
    name = models.CharField(max_length=50)
    pets = models.ManyToManyField(Pets)

    def __str__(self):
        return self.name



