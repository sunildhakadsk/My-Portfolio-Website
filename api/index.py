"""
Vercel serverless function handler for Django
This adapts Django WSGI application to work with Vercel's serverless functions
"""
import os
import sys
from pathlib import Path

# Add project root to Python path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
os.environ.setdefault('VERCEL', '1')

# Initialize Django
import django
django.setup()

from django.core.wsgi import get_wsgi_application
from django.core.handlers.wsgi import WSGIHandler

application = get_wsgi_application()

def handler(request):
    """
    Vercel serverless function handler
    Converts Vercel request to Django WSGI format
    """
    from io import BytesIO
    from django.test import RequestFactory
    
    factory = RequestFactory()
    
    # Extract request data
    method = getattr(request, 'method', 'GET')
    path = getattr(request, 'path', '/')
    query_string = getattr(request, 'query_string', '') or ''
    body = getattr(request, 'body', b'') or b''
    headers = getattr(request, 'headers', {}) or {}
    
    # Create Django request
    if method == 'GET':
        django_request = factory.get(path, QUERY_STRING=query_string)
    elif method == 'POST':
        django_request = factory.post(path, data=body, QUERY_STRING=query_string, content_type=headers.get('content-type', 'application/x-www-form-urlencoded'))
    elif method == 'PUT':
        django_request = factory.put(path, data=body, QUERY_STRING=query_string, content_type=headers.get('content-type', ''))
    elif method == 'DELETE':
        django_request = factory.delete(path, QUERY_STRING=query_string)
    else:
        django_request = factory.request(REQUEST_METHOD=method, PATH_INFO=path, QUERY_STRING=query_string)
        if body:
            django_request._body = body
            django_request._stream = BytesIO(body)
    
    # Add headers to META
    for key, value in headers.items():
        key_upper = key.upper().replace('-', '_')
        if key_upper not in ('CONTENT_TYPE', 'CONTENT_LENGTH'):
            django_request.META[f'HTTP_{key_upper}'] = value
    
    # Set important headers
    django_request.META['HTTP_HOST'] = headers.get('host', 'localhost')
    django_request.META['SERVER_NAME'] = headers.get('host', 'localhost').split(':')[0]
    django_request.META['SERVER_PORT'] = headers.get('host', 'localhost').split(':')[1] if ':' in headers.get('host', 'localhost') else '80'
    
    # Process request through Django
    response = application.get_response(django_request)
    
    # Convert to Vercel response format
    response_headers = {}
    for key, value in response.items():
        response_headers[key] = value
    
    # Handle CORS if needed
    if 'Access-Control-Allow-Origin' not in response_headers:
        response_headers['Access-Control-Allow-Origin'] = '*'
    
    return {
        'statusCode': response.status_code,
        'headers': response_headers,
        'body': response.content.decode('utf-8') if isinstance(response.content, bytes) else str(response.content)
    }
