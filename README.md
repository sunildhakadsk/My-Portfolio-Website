# Personal Portfolio Website

A modern, responsive portfolio website built with Django, HTML, and CSS.

## Features

- **Modern Design**: Beautiful, clean UI with smooth animations
- **Responsive Layout**: Works perfectly on desktop, tablet, and mobile devices
- **Sections Included**:
  - Hero section with introduction
  - About me section
  - Skills showcase with progress bars
  - Projects portfolio
  - Contact form
- **Smooth Scrolling**: CSS-based smooth scrolling navigation
- **Mobile Menu**: Pure CSS hamburger menu (no JavaScript required)

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. **Activate your virtual environment** (if you're using one):
   ```bash
   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations** (if needed):
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser** (optional, for admin access):
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

6. **Open your browser** and navigate to:
   ```
   http://127.0.0.1:8000/
   ```

## Customization

### Update Personal Information

1. **Edit the HTML template** (`portfolio/templates/portfolio/index.html`):
   - Replace "Your Name" with your actual name
   - Update the email, phone, and location in the contact section
   - Modify the about me text
   - Update project information

2. **Update Skills**:
   - Edit the skills section in `index.html`
   - Adjust skill percentages as needed

3. **Update Projects**:
   - Replace project placeholders with your actual projects
   - Update project descriptions and technologies used
   - Add links to your live demos and GitHub repositories

4. **Update Social Links**:
   - Replace placeholder social media links with your actual profiles

### Styling

- Main CSS file: `static/portfolio/css/style.css`
- Color scheme can be customized using CSS variables in the `:root` selector
- Font: Currently using Poppins from Google Fonts

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
│   ├── apps.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── portfolio/
│           └── index.html
└── static/
    └── portfolio/
        └── css/
            └── style.css
```

## Technologies Used

- **Backend**: Django 4.2+
- **Frontend**: HTML5, CSS3 (No JavaScript required!)
- **Fonts**: Google Fonts (Poppins)

## Future Enhancements

- Add contact form backend functionality
- Integrate with email service for contact form
- Add blog section
- Add dark mode toggle
- Add animations library (AOS, Framer Motion, etc.)
- Add project filtering/categories

## Hosting on GitHub

To host this project on GitHub, follow these steps:

### 1. Initialize Git Repository

Open PowerShell or Command Prompt in the project directory and run:

```bash
git init
```

### 2. Add Files to Git

```bash
git add .
```

### 3. Create Initial Commit

```bash
git commit -m "Initial commit: Personal portfolio website"
```

### 4. Create GitHub Repository

1. Go to [GitHub](https://github.com) and sign in
2. Click the "+" icon in the top right corner
3. Select "New repository"
4. Enter a repository name (e.g., "personal-portfolio")
5. Choose public or private visibility
6. **DO NOT** initialize with README, .gitignore, or license (since you already have these)
7. Click "Create repository"

### 5. Connect Local Repository to GitHub

After creating the repository, GitHub will show you commands. Use these (replace `YOUR_USERNAME` and `REPO_NAME` with your actual values):

```bash
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
git branch -M main
git push -u origin main
```

### 6. Push Your Code

```bash
git push -u origin main
```

### Alternative: Using GitHub Desktop

1. Download and install [GitHub Desktop](https://desktop.github.com/)
2. Open GitHub Desktop
3. Click "File" → "Add Local Repository"
4. Select your project folder
5. Click "Publish repository" in GitHub Desktop
6. Enter repository name and description
7. Click "Publish repository"

### Note on Database

The `db.sqlite3` file is excluded from git (via `.gitignore`) as it contains local development data. If you need to deploy this project, you'll need to set up a production database separately.

## License

This project is open source and available for personal use.

## Contact

Feel free to customize this portfolio to match your personal brand and style!

