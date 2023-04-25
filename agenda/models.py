from django.db import models
from django.conf import settings
from django.utils.html import format_html


class Country(models.Model):
    name = models.CharField(max_length=30, unique=True, null=False, blank=False)
    flag = models.ImageField(upload_to='agenda/flags/countries/', null=True, blank=True)
    coat = models.ImageField(upload_to='agenda/coats/countries/', null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Countries'
    
    def __str__(self):
        return self.name
        
    
class Province(models.Model):
    name = models.CharField(max_length=30, unique=True, null=False, blank=False)
    flag = models.ImageField(upload_to='agenda/flags/provinces/', null=True, blank=True)
    coat = models.ImageField(upload_to='agenda/coats/provinces/', null=True, blank=True)
    
    def __str__(self):
        return self.name
    

class Town(models.Model):
    name = models.CharField(max_length=30, unique=True, null=False, blank=False)
    flag = models.ImageField(upload_to='agenda/flags/towns/', null=True, blank=True)
    coat = models.ImageField(upload_to='agenda/coats/towns/', null=True, blank=True)
    
    def __str__(self):
        return self.name


class ZipCode(models.Model):
    zip_code = models.CharField(max_length=10, unique=True)
    
    def __str__(self):
        return self.zip_code


class Location(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, blank=True, null=True)
    town = models.ForeignKey(Town, on_delete=models.CASCADE, blank=True, null=True)
#     zip_code = models.ForeignKey(ZipCode, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.town.name} - {self.province.name}, {self.country.name}'


class Company(models.Model):
    name = models.CharField(max_length=30, unique=True, null=False, blank=False)
    description = models.TextField(max_length=500, blank=True)
    address = models.CharField(max_length=100, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    zip_code = models.ForeignKey(ZipCode, on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Companies'
    
    def __str__(self):
        return self.name


class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500, blank=True)
    address = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return f'{self.title} en {self.company}'


class PhoneJob(models.Model):
    number = models.PositiveIntegerField()
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.number)


class Group(models.Model):
    name = models.CharField(max_length=15, unique=True, blank=False, null=False)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name


class Contact(models.Model):
    names = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    nick_name = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    zip_code = models.ForeignKey(ZipCode, on_delete=models.CASCADE, blank=True, null=True)
    photo = models.ImageField(upload_to='agenda/contact/photo/', default='agenda/contact/photo/nobody.png', blank=True, null=True)

    def personal_photo(self):
        return format_html(f'<img src="{settings.MEDIA_URL}/{self.photo}" width=50px>')    

    birthday = models.DateField(blank=True, null=True)
    
    jobs = models.ManyToManyField(Job, blank=True)
    groups = models.ManyToManyField(Group, blank=True)
    web = models.URLField(max_length=100, blank=True, null=True)
    linked_in = models.URLField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=30, blank=True, null=True)
    facebook = models.URLField(max_length=100, blank=True, null=True)
    instagram = models.CharField(max_length=30, blank=True, null=True)
    whatsapp = models.PositiveIntegerField(blank=True, null=True)    
    note = models.TextField(max_length=500, blank=True, null=True)
    
    def __str__(self):
        return f'{self.last_name}, {self.names}'
    

class Phone(models.Model):
    number = models.PositiveIntegerField()
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.number)
