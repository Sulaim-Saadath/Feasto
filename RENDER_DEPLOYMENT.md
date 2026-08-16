# 🍕 Feasto - Render Deployment Guide

This guide will help you deploy the Feasto food delivery application to Render.

## Prerequisites

1. **GitHub Account** - Push your code to GitHub
2. **Render Account** - Sign up at https://render.com
3. **Razorpay Account** - For payment processing (already configured)

## Step-by-Step Deployment

### Step 1: Prepare Your Project

All necessary files have been created:
- ✅ `requirements.txt` - Python dependencies
- ✅ `Procfile` - Application startup configuration
- ✅ `render.yaml` - Render deployment configuration
- ✅ `settings.py` - Updated for production
- ✅ `.env.example` - Environment variables template

### Step 2: Push Code to GitHub

```bash
# Initialize git (if not already done)
cd your-project-directory
git init

# Add all files
git add .

# Commit changes
git commit -m "Prepare for Render deployment"

# Add remote repository (replace with your GitHub repo URL)
git remote add origin https://github.com/your-username/feasto.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 3: Create Render Account & Deploy

1. **Go to https://render.com and sign up**

2. **Connect your GitHub Account**
   - Click on your profile → Account Settings
   - Connect GitHub

3. **Create a New Web Service**
   - Click "New +" button
   - Select "Web Service"
   - Connect your GitHub repository
   - Select the `feasto` repository

4. **Configure the Web Service**
   - **Name**: `feasto` (or your preferred name)
   - **Environment**: `Python`
   - **Region**: Select closest to you (default: Oregon)
   - **Branch**: `main`
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
   - **Start Command**: `gunicorn Feasto.wsgi:application`
   - **Plan**: Free (recommended for testing)

### Step 4: Set Environment Variables

On the Render dashboard:

1. Go to your service → **Environment**
2. Add the following variables:

```
SECRET_KEY = <generate a new Django secret key>
DEBUG = False
ALLOWED_HOSTS = <your-service-name>.onrender.com,localhost,127.0.0.1
DATABASE_URL = <Render will provide this automatically if you create a PostgreSQL database>
RAZORPAY_KEY_ID = rzp_test_T6uwtR7zR6HuId
RAZORPAY_KEY_SECRET = JcN4tSDywGdeXZ7odZV3PC6O
CSRF_TRUSTED_ORIGINS = https://<your-service-name>.onrender.com
```

### Step 5: Create PostgreSQL Database (Optional but Recommended)

1. In Render Dashboard → Click "New +"
2. Select "PostgreSQL"
3. Configure:
   - **Name**: `feasto-db`
   - **Database**: `feasto_db`
   - **Region**: Same as web service
   - **Plan**: Free

4. Once created, copy the **Internal Database URL**
5. Add it to your web service environment variables as `DATABASE_URL`

### Step 6: Deploy

1. Click **Deploy** button on Render dashboard
2. Wait for the deployment to complete (2-5 minutes)
3. Once deployed, your app will be available at: `https://<your-service-name>.onrender.com`

---

## Testing Your Deployment

1. **Visit Your App**: `https://<your-service-name>.onrender.com`
2. **Test Sign Up**: Create a test account
3. **Test Sign In**: Log in with your test account
4. **Test Shopping Flow**: Browse restaurants → Add items → Checkout

## Troubleshooting

### Issue: "Page not found" errors

**Solution**: 
- Check that `ALLOWED_HOSTS` includes your domain
- Ensure static files are collected: `python manage.py collectstatic`

### Issue: Database errors

**Solution**:
- Verify `DATABASE_URL` is set correctly
- Run migrations: `python manage.py migrate`

### Issue: Static files not loading (CSS/JS broken)

**Solution**:
- Ensure `STATIC_ROOT` and `STATICFILES_DIRS` are configured
- Run: `python manage.py collectstatic --noinput`

### Issue: 502 Bad Gateway

**Solution**:
- Check application logs in Render Dashboard
- Verify Procfile is correct
- Ensure all dependencies are in requirements.txt

## Generate a New Secret Key

```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

Copy the output and use it as your `SECRET_KEY` environment variable.

## Important Notes

⚠️ **Security**:
- Never commit `.env` file to GitHub
- Always use different SECRET_KEY for production
- Keep RAZORPAY keys secure
- Enable HTTPS (Render does this automatically)

📝 **First Time Setup**:
- After first deployment, create a superuser:
  - Go to Render Dashboard → Shell
  - Run: `python manage.py createsuperuser`
  - Access admin at: `https://yourapp.onrender.com/admin`

🔄 **Auto-Deployment**:
- Any push to your `main` branch automatically triggers a new deployment
- Check deployment status in Render Dashboard

## Support

For Render-specific issues: https://render.com/docs
For Django issues: https://docs.djangoproject.com/

---

**Your Feasto app is now ready for the world! 🚀**
