# 🚀 Quick Start: Deploy Feasto to Render

## 5-Minute Setup Guide

### Step 1: GitHub Setup (2 minutes)

```bash
cd your-project-directory

# Add all deployment files
git add .

# Commit
git commit -m "Add Render deployment configuration"

# Push to GitHub
git push origin main
```

### Step 2: Render Account (1 minute)

1. Go to https://render.com
2. Click "Sign Up"
3. Choose "Sign up with GitHub"
4. Authorize GitHub access

### Step 3: Connect & Deploy (2 minutes)

1. Click **"New +"** → **"Web Service"**
2. Select your `feasto` repository
3. Fill in:
   - **Name**: `feasto`
   - **Environment**: `Python 3`
   - **Region**: Closest to you
   - **Build Command**: 
     ```
     pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
     ```
   - **Start Command**: 
     ```
     gunicorn Feasto.wsgi:application
     ```
   - **Plan**: Free

4. Click **Create Web Service**

### Step 4: Environment Variables (2 minutes)

On the service page, go to **Environment** tab and add:

```
SECRET_KEY = (run this locally:)
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

DEBUG = False
ALLOWED_HOSTS = feasto.onrender.com,localhost,127.0.0.1
RAZORPAY_KEY_ID = rzp_test_T6uwtR7zR6HuId
RAZORPAY_KEY_SECRET = JcN4tSDywGdeXZ7odZV3PC6O
CSRF_TRUSTED_ORIGINS = https://feasto.onrender.com
```

⚠️ **Replace `feasto` with your actual service name!**

### Step 5: Deploy

1. Click the **Deploy** button
2. Wait 2-5 minutes
3. Visit your app: `https://your-service-name.onrender.com`

---

## ✅ That's It!

Your Feasto app is now live! 🍕

### Test Your App:
- Homepage: `https://your-service-name.onrender.com`
- Sign Up: `https://your-service-name.onrender.com/open_signup`
- Sign In: `https://your-service-name.onrender.com/open_signin`

### Troubleshooting

**App won't load?**
- Check Render Dashboard → Logs
- Verify environment variables are set
- Ensure all secrets are correct

**CSS/Images broken?**
- Static files might be collecting
- Wait 1-2 minutes and refresh
- Check `STATIC_ROOT` is configured ✅ (Already done)

**Database errors?**
- You might need to create a PostgreSQL database
- See `RENDER_DEPLOYMENT.md` for database setup

---

## Next Steps (Optional)

1. **Create Admin Account**
   - Visit: `https://your-service-name.onrender.com/admin`
   - Use Render Shell to run: `python manage.py createsuperuser`

2. **Custom Domain**
   - Go to Settings → Custom Domains
   - Follow Render instructions

3. **Upgrade to Paid**
   - More reliable than free tier
   - No sleep timeouts
   - Better performance

---

**Questions?** See `RENDER_DEPLOYMENT.md` for complete guide!

Happy hosting! 🚀🍕
