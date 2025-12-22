# Step-by-Step Guide: Deploy Django Portfolio to Render

This guide will walk you through deploying your Django portfolio website to Render.

## Prerequisites

- ✅ GitHub account
- ✅ Render account (free tier available)
- ✅ Your code pushed to a GitHub repository

---

## Step 1: Prepare Your Code for GitHub

### 1.1 Initialize Git Repository (if not already done)

Open your terminal in the project directory and run:

```bash
git init
git add .
git commit -m "Initial commit - Ready for Render deployment"
```

### 1.2 Create GitHub Repository

1. Go to [GitHub.com](https://github.com) and sign in
2. Click the **"+"** icon in the top right → **"New repository"**
3. Name your repository (e.g., `portfolio-django`)
4. Choose **Public** or **Private**
5. **DO NOT** initialize with README, .gitignore, or license (you already have these)
6. Click **"Create repository"**

### 1.3 Push Your Code to GitHub

GitHub will show you commands. Run these in your terminal:

```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` and `YOUR_REPO_NAME` with your actual GitHub username and repository name.

---

## Step 2: Create Render Account

1. Go to [render.com](https://render.com)
2. Click **"Get Started for Free"**
3. Sign up using:
   - **GitHub** (recommended - easiest integration)
   - Email
   - Google account
4. Verify your email if required

---

## Step 3: Deploy Using Blueprint (Easiest Method)

### 3.1 Create New Blueprint

1. In Render Dashboard, click **"New +"** button (top right)
2. Select **"Blueprint"** from the dropdown

### 3.2 Connect GitHub Repository

1. Render will ask you to connect your GitHub account (if not already connected)
2. Click **"Connect GitHub"** and authorize Render
3. Select your repository from the list
4. Click **"Connect"**

### 3.3 Review Configuration

Render will automatically detect your `render.yaml` file and show:
- ✅ **Web Service**: `portfolio-django`
- ✅ **PostgreSQL Database**: `portfolio-db`

**Review the settings:**
- **Name**: `portfolio-django` (or your preferred name)
- **Region**: Choose closest to your users
- **Branch**: `main` (or your default branch)
- **Root Directory**: Leave empty (or `.` if needed)

### 3.4 Apply Blueprint

1. Click **"Apply"** button
2. Render will start creating:
   - PostgreSQL database
   - Web service
   - Environment variables

**Wait 5-10 minutes** for the initial deployment to complete.

---

## Step 4: Configure Environment Variables

### 4.1 Access Your Service

1. After deployment starts, click on your **Web Service** (`portfolio-django`)
2. Go to **"Environment"** tab

### 4.2 Verify Auto-Generated Variables

Render automatically sets:
- ✅ `DATABASE_URL` (from PostgreSQL database)
- ✅ `SECRET_KEY` (auto-generated)
- ✅ `DEBUG` (set to `False`)
- ✅ `PYTHON_VERSION` (set to `3.11.0`)

### 4.3 Add Custom Domain (Optional)

If you have a custom domain:
1. Go to **"Settings"** tab
2. Scroll to **"Custom Domains"**
3. Add your domain
4. Update DNS records as instructed

---

## Step 5: Create Superuser Account

### 5.1 Open Render Shell

1. In your Web Service dashboard, go to **"Shell"** tab
2. Click **"Open Shell"**

### 5.2 Run Createsuperuser Command

In the shell, run:

```bash
python manage.py createsuperuser
```

Follow the prompts:
- **Username**: (enter your admin username)
- **Email**: (enter your email)
- **Password**: (enter a strong password)

### 5.3 Verify Admin Access

1. Go to your deployed site URL (shown in Render dashboard)
2. Visit: `https://your-app.onrender.com/admin/`
3. Log in with your superuser credentials

---

## Step 6: Add Content to Your Portfolio

### 6.1 Add Personal Information

1. Log into Django Admin: `https://your-app.onrender.com/admin/`
2. Go to **Portfolio → Personal Info**
3. Click **"Add Personal Info"**
4. Fill in:
   - Full Name
   - Title
   - Email, Phone, Location
   - Social Media Links
   - Profile Image (upload)
   - Professional Summary
   - Resume File (optional)
5. Click **"Save"**

### 6.2 Add Projects

1. Go to **Portfolio → Projects**
2. Click **"Add Project"**
3. Fill in project details:
   - Title
   - Description
   - Technologies (comma-separated)
   - GitHub URL (optional)
   - Live URL (optional)
   - **Featured Image** (upload - required)
   - Check **"Is Featured"** if you want it on homepage
   - Display Order (lower = appears first)
4. Click **"Save"**

### 6.3 Add Project Images (Optional)

1. After saving a project, scroll to **"Project Images"**
2. Click **"Add another Project Image"**
3. Upload images with optional captions
4. Click **"Save"**

---

## Step 7: Verify Deployment

### 7.1 Check Your Live Site

Visit your Render URL:
- **Homepage**: `https://your-app.onrender.com/`
- **Projects**: `https://your-app.onrender.com/projects/`
- **Contact**: `https://your-app.onrender.com/contact/`
- **Admin**: `https://your-app.onrender.com/admin/`

### 7.2 Test Functionality

- ✅ Homepage displays correctly
- ✅ Projects page shows all projects
- ✅ Project detail pages work
- ✅ Contact form submits successfully
- ✅ Static files (CSS, JS) load properly
- ✅ Images display correctly

---

## Step 8: Monitor and Maintain

### 8.1 View Logs

1. In Render Dashboard → Your Web Service
2. Go to **"Logs"** tab
3. Monitor for any errors or warnings

### 8.2 Check Health Status

- Green status = Service is running
- Yellow status = Service is starting/restarting
- Red status = Service has errors (check logs)

### 8.3 Update Your Site

To update your site:
1. Make changes locally
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Update portfolio"
   git push origin main
   ```
3. Render will automatically detect changes and redeploy

---

## Troubleshooting

### Issue: Build Fails

**Solution:**
- Check **"Logs"** tab for error messages
- Verify `requirements.txt` has all dependencies
- Ensure Python version matches (3.11.0)

### Issue: Static Files Not Loading

**Solution:**
- Verify `collectstatic` runs in build command
- Check `STATIC_ROOT` in settings.py
- Ensure WhiteNoise middleware is enabled

### Issue: Database Connection Error

**Solution:**
- Verify `DATABASE_URL` is set in Environment variables
- Check database is created and running
- Ensure `dj-database-url` is in requirements.txt

### Issue: 500 Internal Server Error

**Solution:**
- Check logs for specific error
- Verify `DEBUG=False` in production
- Check `ALLOWED_HOSTS` includes your Render domain
- Ensure `SECRET_KEY` is set

### Issue: Migrations Not Running

**Solution:**
- Manually run migrations in Shell:
  ```bash
  python manage.py migrate
  ```

### Issue: Images Not Uploading

**Solution:**
- Render has ephemeral filesystem (files reset on restart)
- Consider using cloud storage (AWS S3, Cloudinary) for media files
- For now, images will work but may reset on redeploy

---

## Important Notes

### ⚠️ Free Tier Limitations

- **Spins down after 15 minutes** of inactivity
- First request after spin-down takes ~30 seconds
- **Database**: 90-day retention on free tier
- **Bandwidth**: Limited on free tier

### 💡 Upgrade Options

For production use, consider:
- **Starter Plan** ($7/month): Always-on service
- **Professional Plan**: More resources, better performance

### 📁 Media Files Storage

Render's filesystem is **ephemeral** (resets on restart). For production:
- Use **AWS S3** for media storage
- Use **Cloudinary** for image hosting
- Use **Render Disk** (paid feature) for persistent storage

---

## Quick Reference

### Render Dashboard URLs
- **Dashboard**: https://dashboard.render.com
- **Your Service**: https://dashboard.render.com/web/YOUR_SERVICE_ID
- **Logs**: Available in service dashboard

### Your Site URLs
- **Homepage**: `https://your-app.onrender.com/`
- **Admin**: `https://your-app.onrender.com/admin/`

### Useful Commands (Run in Render Shell)

```bash
# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput

# Check Django version
python -c "import django; print(django.get_version())"
```

---

## Success Checklist

- [ ] Code pushed to GitHub
- [ ] Render account created
- [ ] Blueprint deployed successfully
- [ ] Database created and connected
- [ ] Superuser account created
- [ ] Personal info added
- [ ] Projects added with images
- [ ] Site accessible and working
- [ ] Contact form tested
- [ ] Admin panel accessible

---

## Need Help?

- **Render Docs**: https://render.com/docs
- **Django Deployment**: https://docs.djangoproject.com/en/stable/howto/deployment/
- **Render Support**: Available in dashboard

---

**Congratulations! Your portfolio is now live on Render! 🎉**

