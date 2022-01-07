from django.contrib import admin
from django.urls import path, include
from home import views



#django admin header customization

admin.site.site_header = "Welcome to student mangement system"
admin.site.site_title="Welcome to student's Dashboard"
admin.site.index_title="Welcome to student portal"

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('student', views.student, name='student'),
    path('contact', views.contact, name='contact'),
    path('faq', views.faq, name='faq'),
    path('faculty', views.faculty, name='faculty'),
    
]
