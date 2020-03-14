from django.contrib import admin
from user.models import EventVenue, EventRegistration, EventCategory
# Register your models here.
admin.site.register(EventCategory)
admin.site.register(EventRegistration)
admin.site.register(EventVenue)
