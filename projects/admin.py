from django.contrib import admin
from .models import Project, Issue
# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
	date_hierarchy = 'startdate'
	search_fields = ['title', 'role']
	list_display = ['title', 'point']
	list_filter = ['title']
	# readonly_fields = ['timestamp', 'updated']
	# prepopulated_fields = {'slug': ('title',)}
	class Meta:
		model = Project

admin.site.register(Project, ProjectAdmin)
admin.site.register(Issue)