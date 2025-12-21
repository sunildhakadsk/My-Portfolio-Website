from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Contact

def home(request):
    """Render the portfolio homepage"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Validate that all fields are provided
        if name and email and subject and message:
            # Create and save contact submission
            Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            
            messages.success(request, 'Thank you for your message! I will get back to you soon.')
            # Redirect to home with contact fragment
            return HttpResponseRedirect(reverse('home') + '#contact')
        else:
            messages.error(request, 'Please fill in all fields.')
    
    return render(request, 'portfolio/index.html')

