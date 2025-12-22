from django.shortcuts import render, redirect


def home(request):
    return render(request, "portfolio/home.html")


def about(request):
    # Single-page layout: send About URL to home
    return redirect("portfolio:home")


def skills(request):
    # Single-page layout: send Skills URL to home
    return redirect("portfolio:home")


def projects(request):
    # Single-page layout: send Projects URL to home
    return redirect("portfolio:home")


def contact(request):
    # Single-page layout: send Contact URL to home
    return redirect("portfolio:home")
