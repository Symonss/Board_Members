from django.contrib import admin
from .models import Member, Position, Institutional

class PositionAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Position, PositionAdmin)

class InstitutionalAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Institutional, InstitutionalAdmin)



class MemberAdmin(admin.ModelAdmin):
    list_display = ('name','institutional','position','status',
                    'appointment_schedule',
                    'date_of_appointment',
                    'date_of_expiry',
                    'gazetted_by'
                    )
    list_filter = ('status','date_of_expiry','institutional')

admin.site.register(Member, MemberAdmin)
