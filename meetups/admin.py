from django.contrib import admin
from .models import Meetup,Location,Participant,About,Contact, User



# Register your models here.
class MeetupAdmin (admin.ModelAdmin):
   list_display=('title', 'slug', 'description', )
   list_filter=('title',)
   prepopulated_fields={'slug':('title',)}

class LocationAdmin (admin.ModelAdmin):
   list_display=('name', 'address', )
admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location, LocationAdmin )

admin.site.register(Participant)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(User)


