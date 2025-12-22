from django.contrib import admin
from .models import Project, ProjectImage, ContactMessage, PersonalInfo


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_featured', 'order', 'created_at']
    list_filter = ['is_featured', 'created_at']
    search_fields = ['title', 'description']
    inlines = [ProjectImageInline]
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'technologies')
        }),
        ('Links', {
            'fields': ('github_url', 'live_url')
        }),
        ('Media', {
            'fields': ('featured_image',)
        }),
        ('Display Settings', {
            'fields': ('is_featured', 'order')
        }),
    )


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ['project', 'caption', 'order']
    list_filter = ['project']
    ordering = ['project', 'order']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['created_at']
    list_editable = ['is_read']


@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'title', 'email', 'phone']
    fieldsets = (
        ('Personal Information', {
            'fields': ('full_name', 'title', 'summary', 'profile_image')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'location')
        }),
        ('Social Links', {
            'fields': ('linkedin_url', 'github_url')
        }),
        ('Resume', {
            'fields': ('resume_file',)
        }),
    )

