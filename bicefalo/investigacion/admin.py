from django.contrib import admin
from models import Investigacion, LinkInvestigacion
class LinksInLine(admin.TabularInline):
    model = LinkInvestigacion
    extra = 1
    
class FeedAdmin(admin.ModelAdmin):
    inlines = (LinksInLine,)
admin.site.register([Investigacion],FeedAdmin)
