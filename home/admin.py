from django.contrib import admin
from home.models import Contact
from home.models import Student
from home.models import Faculty

# from django.urls import path
# from django.http import HttpResponseRedirect
# from django.utils.html import format_html


# Register your models here.
admin.site.register(Contact)
admin.site.register(Student)
admin.site.register(Faculty)


# #admin action Function to update all gender to mail

# def update_gender_all(modeladmin, request , queryset):
#     queryset.update(genral='Male')

# #action descrption 
# update_gender_all.short.description = "Mark selected gender as Male"



# class ContactAdmin(admin.ModelAdmin):
#     exclude = ('created at',)
#     sortable_by = 'Id'
#     date_hierarchy = 'created at'
#     search_fields =['name','email']
#     list_display = ('name', 'email', 'city', 'desc')
#     list_display_links= ('name','address')
#     list_filter=('type')
#     list_editable =('email')
#     filter_vertical=('city')
    # actions = (update_gender_all)
