# Personal Portfolio Website

A modern, responsive portfolio website built with Django, HTML, and CSS. This website showcases projects, skills, and includes a contact form with image handling capabilities.

## Features

- **Responsive Design**: Mobile-friendly layout that works on all devices
- **Project Showcase**: Display projects with featured images and additional gallery images
- **Image Management**: Full support for uploading and displaying images through Django admin
- **Contact Form**: Functional contact form with database storage
- **Django Admin**: Easy content management through Django admin interface
- **Modern UI**: Clean, professional design with smooth animations

## Technologies Used

- **Backend**: Django 4.2+
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite (default, can be changed to PostgreSQL/MySQL)
- **Image Processing**: Pillow
- **Icons**: Font Awesome

## Installation

1. **Clone the repository** (if applicable) or navigate to the project directory:
   ```bash
   cd "personal portfolio"
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser** (to access Django admin):
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

8. **Access the website**:
   - Website: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## Setup Instructions

### 1. Add Personal Information

1. Go to Django Admin: http://127.0.0.1:8000/admin/
2. Navigate to **Portfolio > Personal Info**
3. Click **Add Personal Info** and fill in your details:
   - Full Name
   - Title (e.g., "Python Backend Developer")
   - Email, Phone, Location
   - LinkedIn and GitHub URLs
   - Profile Image (optional)
   - Professional Summary
   - Resume File (optional)

### 2. Add Projects

1. Go to **Portfolio > Projects** in Django Admin
2. Click **Add Project** and fill in:
   - Title
   - Description
   - Technologies (comma-separated, e.g., "Python, Django, MySQL")
   - GitHub URL (optional)
   - Live URL (optional)
   - **Featured Image** (required - main project image)
   - Mark as "Featured" if you want it on the homepage
   - Set display order (lower numbers appear first)

3. **Add Additional Images** (optional):
   - After saving a project, you can add multiple gallery images
   - Click on the project, scroll down to "Project Images"
   - Add images with optional captions

### 3. View Contact Messages

- Contact form submissions are stored in **Portfolio > Contact Messages**
- You can mark messages as read/unread
- All messages include name, email, subject, message, and timestamp

## Project Structure

```
personal portfolio/
├── manage.py
├── requirements.txt
├── README.md
├── portfolio_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── portfolio/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── migrations/
│   ├── templates/
│   │   └── portfolio/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── projects.html
│   │       ├── project_detail.html
│   │       └── contact.html
│   └── static/
│       └── portfolio/
│           ├── css/
│           │   └── style.css
│           └── js/
│               └── main.js
└── media/
    ├── projects/
    ├── profile/
    └── resume/
```

## Models

### Project
- Stores project information with featured image
- Supports multiple additional images through ProjectImage model
- Can be marked as featured for homepage display

### ProjectImage
- Additional images for projects
- Supports captions and ordering

### ContactMessage
- Stores contact form submissions
- Tracks read/unread status

### PersonalInfo
- Stores personal information displayed on the site
- Supports profile image and resume file uploads

## Deployment

### For Production Deployment:

1. **Update settings.py**:
   - Set `DEBUG = False`
   - Update `ALLOWED_HOSTS` with your domain
   - Change `SECRET_KEY` to a secure random value
   - Configure a production database (PostgreSQL recommended)

2. **Collect static files**:
   ```bash
   python manage.py collectstatic
   ```

3. **Set up media file serving** (for production):
   - Configure your web server (Nginx/Apache) to serve media files
   - Or use cloud storage (AWS S3, Cloudinary, etc.)

### Recommended Platforms:
- **Render**: Easy deployment with PostgreSQL
- **Heroku**: Popular platform with good Django support
- **AWS EC2**: Full control over server configuration
- **DigitalOcean**: Simple VPS deployment

## Features in Detail

### Image Handling
- Images are automatically resized and optimized
- Featured images for projects
- Gallery images with captions
- Profile image support
- Resume file uploads

### Responsive Design
- Mobile-first approach
- Hamburger menu for mobile devices
- Flexible grid layouts
- Touch-friendly buttons and links

### Contact Form
- CSRF protection
- Form validation
- Success/error messages
- Database storage
- Admin interface for viewing messages

## Customization

### Colors
Edit CSS variables in `portfolio/static/portfolio/css/style.css`:
```css
:root {
    --primary-color: #2563eb;
    --secondary-color: #1e40af;
    /* ... */
}
```

### Styling
All styles are in `portfolio/static/portfolio/css/style.css`. Modify as needed for your brand.

## License

This project is open source and available for personal use.

## Author

**Sunil Dhakad**
- Email: sunildhakadsk2255@gmail.com
- LinkedIn: [sunil-dhakad-110913316](https://linkedin.com/in/sunil-dhakad-110913316)
- GitHub: [sunildhakadsk](https://github.com/sunildhakadsk)

## Support

For issues or questions, please contact through the contact form on the website or via email.

