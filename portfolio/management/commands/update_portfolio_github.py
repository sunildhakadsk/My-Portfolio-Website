from django.core.management.base import BaseCommand
from portfolio.models import Project


class Command(BaseCommand):
    help = 'Updates the GitHub URL for the Portfolio Website project'

    def handle(self, *args, **options):
        github_url = 'https://github.com/sunildhakadsk/Portfolio-Website.git'
        
        try:
            project = Project.objects.get(title='Portfolio Website')
            project.github_url = github_url
            project.save()
            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully updated GitHub URL for "{project.title}" to {github_url}'
                )
            )
        except Project.DoesNotExist:
            self.stdout.write(
                self.style.ERROR(
                    'Project "Portfolio Website" not found. Please create it first through Django admin.'
                )
            )
        except Project.MultipleObjectsReturned:
            projects = Project.objects.filter(title='Portfolio Website')
            for project in projects:
                project.github_url = github_url
                project.save()
            self.stdout.write(
                self.style.WARNING(
                    f'Found multiple projects with title "Portfolio Website". Updated all of them.'
                )
            )

