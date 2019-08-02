from django.contrib import admin
from .models import Team, UserProfile
# Register your models here.
class TeamAdmin(admin.ModelAdmin):
	search_fields = ['name', 'role']
	list_display = ['name', 'total_points']
	list_editable = ['total_points']
	list_filter = ['name']
	# readonly_fields = ['timestamp', 'updated']
	# prepopulated_fields = {'slug': ('title',)}
	class Meta:
		model = Team
admin.site.register(Team, TeamAdmin)
admin.site.register(UserProfile)