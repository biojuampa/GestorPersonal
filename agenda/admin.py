from django.contrib import admin
from .models import (Country,
                     Province,
                     Town,
                     ZipCode,
                     Location,
                     Company,
                     Job,
                     PhoneJob,
                     Group,
                     Contact,
                     Phone,
                     )


class PhoneInline(admin.StackedInline):
    model = Phone
    extra = 1


class ContactAdmin(admin.ModelAdmin):
    filter_horizontal = ('jobs', 'groups',)
    
    inlines = [PhoneInline]

    actions_on_bottom = True
    
    ordering = []

    fieldsets = [
        ('Contacto', {'fields': ('names', 'last_name')}),
        
        ('Datos Personales', {'fields': ('nick_name', 'email', 'address',
                                         'location', 'zip_code', 'photo',
                                         'birthday',
                                         ),
                              'classes': ('collapse',)
                              }
         ),
        
        ('Datos Laborales', {'fields': ('jobs',), 'classes': ('collapse',)}),
        
        ('Redes Sociales', {'fields': ('web', 'linked_in', 'twitter',
                                       'facebook', 'instagram', 'whatsapp',
                                       ),
                            'classes': ('collapse',)
                            }
         ),
        
        ('Otros', {'fields': ('groups', 'note',), 'classes': ('collapse',)}),
        
    ]
    
    list_display = ('personal_photo', '__str__', 'nick_name', 'email', 'birthday')
    
    list_display_links = ('personal_photo', '__str__',)
    
    date_hierarchy = 'birthday'
    
    search_fields = ('names', 'last_name', 'nick_name')
    
    list_filter = ('groups', 'location__town')


class LocationAdmin(admin.ModelAdmin):
    list_filter = ['country', 'province']
    
    list_display = ['town', 'province', 'country']
    
    actions_on_bottom = True
    
    ordering = ['-town', '-country']
    

class CompanyAdmin(admin.ModelAdmin):
    list_filter = ['location__country',
                   'location__province',
                   'location__town'
                   ]
    
    list_display = ['__str__', 'address', 'location']
    
    actions_on_bottom = True


class PhoneJobInline(admin.StackedInline):
    model = PhoneJob
    extra = 1


class JobAdmin(admin.ModelAdmin):
    inlines = [PhoneJobInline]

    def get_model_perms(self, request):
        """
        Retorno un diccionario de permisos vacío para ocultar
        el modelo en el índice del panel de administración.
        """
        return {}
    

class CountryAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Retorno un diccionario de permisos vacío para ocultar
        el modelo en el índice del panel de administración.
        """
        return {}


class ProvinceAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Retorno un diccionario de permisos vacío para ocultar
        el modelo en el índice del panel de administración.
        """
        return {}


class TownAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Retorno un diccionario de permisos vacío para ocultar
        el modelo en el índice del panel de administración.
        """
        return {}


class ZipCodeAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Retorno un diccionario de permisos vacío para ocultar
        el modelo en el índice del panel de administración.
        """
        return {}


# class CountryAdmin(admin.ModelAdmin):
#     def get_model_perms(self, request):
#         """
#         Retorno un diccionario de permisos vacío para ocultar
#         el modelo en el índice del panel de administración.
#         """
#         return {}

    
admin.site.register(Contact, ContactAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Province, ProvinceAdmin)
admin.site.register(Town, TownAdmin)
admin.site.register(ZipCode, ZipCodeAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Group)
