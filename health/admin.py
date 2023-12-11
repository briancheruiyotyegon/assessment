from django.contrib import admin
from .models import CustomUser, Category, Data

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'location', 'address', 'phone', 'role')
    list_filter=('email', 'username', 'location', 'address', 'phone', 'role')
    search_fields=('email', 'username', 'location', 'address', 'phone', 'role')
    ordering=('username', 'location', 'role')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'description', 'additional_info', 'date_register')
    list_filter=('user', 'name', 'description', 'additional_info', 'date_register')
    search_fields=('user', 'name', 'description', 'additional_info', 'date_register')
    ordering=('user', 'name', 'description', 'additional_info', 'date_register')
class DataAdmin(admin.ModelAdmin):
    list_display=('name','first_name','last_name','gender','email','phone_number','specialization','institution_name','institution_type','institution_email','institution_phone_number','institution_address','specialties','facilities','operating_hours','eventName','eventDescription','eventDate','eventTime','eventLocation','eventDuration','eventOrganizer','eventOrganizerEmail','eventOrganizerPhone')
    list_filter=('name','first_name','last_name','gender','email','phone_number','specialization','institution_name','institution_type','institution_email','institution_phone_number','institution_address','specialties','facilities','operating_hours','eventName','eventDescription','eventDate','eventTime','eventLocation','eventDuration','eventOrganizer','eventOrganizerEmail','eventOrganizerPhone')
    search_fields=('name','first_name','last_name','gender','email','phone_number','specialization','institution_name','institution_type','institution_email','institution_phone_number','institution_address','specialties','facilities','operating_hours','eventName','eventDescription','eventDate','eventTime','eventLocation','eventDuration','eventOrganizer','eventOrganizerEmail','eventOrganizerPhone')
    ordering=('first_name','institution_name','eventDate','eventTime','date_register')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Data, DataAdmin)