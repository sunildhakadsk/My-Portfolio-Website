from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from .models import Project, ContactMessage, PersonalInfo


def home(request):
    """Homepage view"""
    personal_info = PersonalInfo.objects.first()
    featured_projects = Project.objects.filter(is_featured=True)[:6]
    all_projects = Project.objects.all()[:6]
    
    context = {
        'personal_info': personal_info,
        'featured_projects': featured_projects if featured_projects else all_projects,
    }
    return render(request, 'portfolio/home.html', context)


def projects(request):
    """All projects page"""
    projects_list = Project.objects.all()
    context = {
        'projects': projects_list,
    }
    return render(request, 'portfolio/projects.html', context)


def project_detail(request, pk):
    """Individual project detail page"""
    project = Project.objects.get(pk=pk)
    project_images = project.images.all()
    context = {
        'project': project,
        'project_images': project_images,
    }
    return render(request, 'portfolio/project_detail.html', context)


@require_http_methods(["GET", "POST"])
def contact(request):
    """Contact form view"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        if name and email and subject and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            messages.success(request, 'Thank you for your message! I will get back to you soon.')
            return redirect('contact')
        else:
            messages.error(request, 'Please fill in all fields.')
    
    personal_info = PersonalInfo.objects.first()
    context = {
        'personal_info': personal_info,
    }
    return render(request, 'portfolio/contact.html', context)

