from .models import PersonalInfo


def personal_info(request):
    """Make personal info available to all templates"""
    return {
        'personal_info': PersonalInfo.objects.first()
    }

