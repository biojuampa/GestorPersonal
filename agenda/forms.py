from django import forms
from django.urls import reverse_lazy
from django.utils.html import format_html
from .models import Contact, Phone, PhoneJob, Job, Company, Location, Country, Province, Town, Group, ZipCode


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
#        labels = {'zip_code': format_html('<a href="/agenda/zipcode/new/">Zip Code</a>'),
#                  'location': format_html('<a href="/agenda/location/new/">Location</a>'),
#                  'jobs': format_html('<a href="/agenda/job/new/">Jobs</a>'),
#                  'groups': format_html('<a href="/agenda/groups/new/">Groups</a>'),
#                  }


class ContactDetailForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        exclude = ('photo',)


class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ('number',)


class PhoneJobForm(forms.ModelForm):
    class Meta:
        model = PhoneJob
        fields = '__all__'


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'


class ProvinceForm(forms.ModelForm):
    class Meta:
        model = Province
        fields = '__all__'


class TownForm(forms.ModelForm):
    class Meta:
        model = Town
        fields = '__all__'


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'


class ZipCodeForm(forms.ModelForm):
    class Meta:
        model = ZipCode
        fields = '__all__'

