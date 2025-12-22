from django.core.management.base import BaseCommand
from portfolio.models import Project


class Command(BaseCommand):
    help = 'Adds sample projects to the database'

    def handle(self, *args, **options):
        projects_data = [
            {
                'title': 'Weather Forecast App',
                'description': 'Developed a responsive weather application using Flask and REST APIs. Integrated the OpenWeatherMap API to fetch live weather data. Deployed the application on Render for public access.',
                'technologies': 'Flask, OpenWeatherMap API, Render, GitHub, Python, HTML, CSS',
                'github_url': 'https://github.com/sunildhakadsk',
                'live_url': 'https://your-weather-app.onrender.com',
                'is_featured': True,
                'order': 1,
            },
            {
                'title': 'Portfolio Website',
                'description': 'Designed and developed a personal portfolio website with a responsive frontend. Integrated a contact form with database storage and Django Admin for management. Deployed the website on Render and connected to GitHub for continuous updates.',
                'technologies': 'Django, HTML, CSS, JavaScript, SQLite, Render, GitHub',
                'github_url': 'https://github.com/sunildhakadsk',
                'live_url': 'https://your-portfolio.onrender.com',
                'is_featured': True,
                'order': 2,
            },
            {
                'title': 'Blog API with JWT Authentication',
                'description': 'Designed and implemented a backend REST API for a blogging platform. Added secure user authentication using JWT tokens. Created endpoints for user registration, login, creating, updating, and deleting posts. Used Postman for API testing and documentation.',
                'technologies': 'Django REST Framework, JWT Authentication, PostgreSQL, Postman, Python',
                'github_url': 'https://github.com/sunildhakadsk',
                'live_url': None,
                'is_featured': True,
                'order': 3,
            },
        ]

        created_count = 0
        for project_data in projects_data:
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults=project_data
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully created project: {project.title}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Project already exists: {project.title}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'\nCreated {created_count} new project(s).')
        )
        self.stdout.write(
            self.style.WARNING(
                '\nNote: You can add images to these projects through the Django admin panel:\n'
                '1. Go to http://127.0.0.1:8000/admin/\n'
                '2. Navigate to Portfolio > Projects\n'
                '3. Click on each project to add featured images'
            )
        )

