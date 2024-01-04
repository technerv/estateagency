from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse

#agent model
class Agent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="agentuser", null=True)
    name = models.CharField(max_length=60, verbose_name='Agent Name')
    description = models.TextField(verbose_name='Agent Description')
    email = models.EmailField(max_length=254, verbose_name='Email Address')
    phone = models.IntegerField(verbose_name='Phone Number')
    image = models.ImageField(upload_to="img", blank=False)

    def __str__(self):
       return str(self.user)

    class Meta:
        verbose_name_plural = "Agents"

#property model
class Property(models.Model):
    STATUS = (
            ('Rent', 'Rent'),
            ('Sale', 'Sale'),
            ('Open House', 'Open House'),

    )

    PROPERTY_TYPE = (
            ('Apartments', 'Apartments'),
            ('Bungalow', 'Bungalow'),
            ('Presidental', 'Presidental'),

    )

    property_title = models.CharField(max_length=60, verbose_name='Property Title')
    slug = models.SlugField(max_length=250, null=True, blank=True, unique=True)
    property_id = models.IntegerField(verbose_name='Property ID')
    location = models.CharField(max_length=60, verbose_name='Location')
    property_type = models.CharField(max_length=60, choices=PROPERTY_TYPE, verbose_name='Property Type')
    status = models.CharField(max_length=10, choices=STATUS, verbose_name='Status')
    area = models.IntegerField(verbose_name='Area')
    beds = models.IntegerField(verbose_name='Beds')
    baths = models.IntegerField(verbose_name='Baths')
    garage = models.IntegerField(verbose_name='Garage')
    property_description = models.TextField()
    amenities = models.TextField()
    amount = models.IntegerField(verbose_name ='Amount')
    image = models.ImageField(upload_to="img", blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    agent_id = models.ForeignKey(Agent, verbose_name='agent', on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="agent", null=True)


    def __str__(self):
        return str(self.property_id)

    def get_absolute_url(self):
        return reverse('estateapp:roperty_single', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        value = self.property_title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)



    class Meta:
        verbose_name_plural = "Properties"
