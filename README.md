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

## Deploy to Vercel

This Django portfolio can be deployed to Vercel as a serverless function. Follow these steps:

### Prerequisites

1. A GitHub account (your code should be pushed to GitHub)
2. A Vercel account (sign up at [vercel.com](https://vercel.com))

### Deployment Steps

#### Option 1: Deploy via Vercel Dashboard (Recommended)

1. **Push your code to GitHub** (see GitHub hosting section above)

2. **Go to Vercel Dashboard**
   - Visit [vercel.com](https://vercel.com) and sign in
   - Click "Add New..." → "Project"

3. **Import your GitHub repository**
   - Select your portfolio repository
   - Click "Import"

4. **Configure Project Settings**
   - **Framework Preset**: Other
   - **Root Directory**: `./` (leave as default)
   - **Build Command**: Leave empty (or use `python manage.py collectstatic --noinput` if needed)
   - **Output Directory**: Leave empty
   - **Install Command**: `pip install -r requirements.txt` (or `pip install --no-warn-script-location -r requirements.txt` to suppress warnings)

5. **Set Environment Variables** (Important!)
   Click "Environment Variables" and add:
   - `SECRET_KEY`: Generate a secure secret key (you can use: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`)
   - `DEBUG`: Set to `False` for production
   - `VERCEL`: Set to `1`

6. **Deploy**
   - Click "Deploy"
   - Wait for deployment to complete
   - Your site will be live at `your-project-name.vercel.app`

#### Option 2: Deploy via Vercel CLI

1. **Install Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel**
   ```bash
   vercel login
   ```

3. **Deploy**
   ```bash
   vercel
   ```

4. **Set Environment Variables**
   ```bash
   vercel env add SECRET_KEY
   vercel env add DEBUG
   vercel env add VERCEL
   ```

5. **Deploy to Production**
   ```bash
   vercel --prod
   ```

### Important Notes for Vercel Deployment

⚠️ **Database Limitations**: 
- SQLite databases don't work well on Vercel's serverless functions (they're read-only and ephemeral)
- The contact form will not save submissions unless you:
  - Use an external database (PostgreSQL, MongoDB, etc.)
  - Use a service like Vercel Postgres, Supabase, or MongoDB Atlas
  - Or disable the database functionality and use a form service like Formspree

**To use an external database:**
1. Set up a PostgreSQL database (Vercel Postgres, Supabase, or Railway)
2. Update `settings.py` to use the production database
3. Update `DATABASES` setting with your database credentials
4. Run migrations: `python manage.py migrate`

ℹ️ **Pip Warning**: 
- You may see a warning about running pip as root user during deployment
- This is **normal and safe to ignore** in Vercel's isolated serverless environment
- Vercel uses isolated containers, so this warning doesn't affect your deployment
- To suppress the warning, you can add `--no-warn-script-location` to your install command in Vercel settings

### Troubleshooting

- **Static files not loading**: Ensure `STATIC_URL` is set to `/static/` in settings.py
- **500 errors**: Check Vercel function logs in the dashboard
- **Database errors**: Consider using an external database or disabling database features
- **Import errors**: Ensure all dependencies are in `requirements.txt`

### Alternative: Static Site Deployment

If you want a simpler deployment without serverless functions, consider:
- Converting Django templates to static HTML
- Using GitHub Pages
- Using Netlify Drop
- Using Vercel's static site hosting

## License

This project is open source and available for personal use.

## Contact

Feel free to customize this portfolio to match your personal brand and style!

