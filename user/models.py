from django.db import models

# Create your models here.
class EventCategory(models.Model):
    category_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False) 
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.category_name
    

class EventVenue(models.Model):
    venue_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False) 
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.venue_name
    

class EventRegistration(models.Model):
    host_name = models.CharField(max_length=50)
    contact_number = models.IntegerField()
    host_email_id = models.EmailField(max_length=100)
    event_category = models.ForeignKey(EventCategory, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    select_vanue_1 = models.ForeignKey(EventVenue, on_delete=models.CASCADE, related_name='select_vanue_1')
    select_vanue_2 = models.ForeignKey(EventVenue, on_delete=models.CASCADE, related_name='select_vanue_2')
    select_vanue_3 = models.ForeignKey(EventVenue, on_delete=models.CASCADE, related_name='select_vanue_3')
    budget = models.CharField(max_length=30)
    special_requirements = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False) 
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def __str__(self):
        return self.host_name 
    
