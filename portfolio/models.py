from django.db import models
from django.utils import timezone


class Project(models.Model):
    """Model for portfolio projects"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=500, help_text="Comma-separated list of technologies")
    github_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    featured_image = models.ImageField(upload_to='projects/', help_text="Main project image", blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    is_featured = models.BooleanField(default=False, help_text="Display on homepage")
    order = models.IntegerField(default=0, help_text="Display order (lower numbers first)")

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    def get_technologies_list(self):
        """Return technologies as a list"""
        return [tech.strip() for tech in self.technologies.split(',')]


class ProjectImage(models.Model):
    """Additional images for projects"""
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/gallery/')
    caption = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.project.title} - Image {self.order}"


class ContactMessage(models.Model):
    """Model for contact form submissions"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"


class PersonalInfo(models.Model):
    """Model for personal information displayed on the site"""
    full_name = models.CharField(max_length=100)
    title = models.CharField(max_length=200, help_text="e.g., Python Backend Developer")
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=200)
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    summary = models.TextField(help_text="Professional summary")
    resume_file = models.FileField(upload_to='resume/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Personal Info"

    def __str__(self):
        return self.full_name

