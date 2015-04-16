from django.contrib import admin

# Register your models here.
from .models import Request

class RequestAdmin(admin.ModelAdmin):
	list_display = ('timestamp', 'full_url', 'is_good', 'param_map')
	list_filter = ['is_good'. 'full_url']

admin.site.register(Request, RequestAdmin)


