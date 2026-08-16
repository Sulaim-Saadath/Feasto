#!/bin/bash

# 🔍 Deployment Verification Script
# Run this to verify all deployment files are present

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🚀 Feasto Deployment Verification"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to check file
check_file() {
    if [ -f "$1" ]; then
        echo -e "${GREEN}✅${NC} $1"
        return 0
    else
        echo -e "${RED}❌${NC} $1 (MISSING)"
        return 1
    fi
}

# Check critical files
echo "📁 Checking Critical Deployment Files..."
echo ""

check_file "requirements.txt"
check_file "Procfile"
check_file ".env.example"
check_file "Feasto/settings.py"

echo ""
echo "📚 Checking Documentation Files..."
echo ""

check_file "QUICK_START.md"
check_file "RENDER_DEPLOYMENT.md"
check_file "DEPLOYMENT_CHECKLIST.md"
check_file "DEPLOYMENT_SUMMARY.md"

echo ""
echo "🔧 Checking Project Structure..."
echo ""

check_file "manage.py"
check_file "feastoApp/models.py"
check_file "feastoApp/views.py"
check_file "feastoApp/urls.py"

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Check requirements.txt content
echo "📦 Checking requirements.txt contents..."
echo ""

check_req() {
    if grep -q "$1" requirements.txt; then
        echo -e "${GREEN}✅${NC} $1"
    else
        echo -e "${RED}❌${NC} $1 (NOT FOUND in requirements.txt)"
    fi
}

check_req "Django"
check_req "gunicorn"
check_req "whitenoise"
check_req "python-decouple"
check_req "dj-database-url"
check_req "psycopg2"
check_req "razorpay"

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Check settings.py configuration
echo "⚙️  Checking settings.py configuration..."
echo ""

check_setting() {
    if grep -q "$1" Feasto/settings.py; then
        echo -e "${GREEN}✅${NC} $1"
    else
        echo -e "${YELLOW}⚠️${NC}  $1 (Not found)"
    fi
}

check_setting "config("
check_setting "whitenoise"
check_setting "dj_database_url"
check_setting "STATIC_ROOT"
check_setting "STATIC_URL"

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Git check
if [ -d ".git" ]; then
    echo -e "${GREEN}✅${NC} Git repository initialized"
    echo ""
    
    # Check git status
    if [ -z "$(git status -s)" ]; then
        echo -e "${YELLOW}⚠️${NC}  All changes should be committed before deployment"
        echo "   Run: git add ."
        echo "        git commit -m 'Add Render deployment'"
        echo "        git push origin main"
    else
        echo -e "${YELLOW}⚠️${NC}  Uncommitted changes found:"
        git status -s | head -5
    fi
else
    echo -e "${RED}❌${NC} Git repository not initialized"
    echo "   Run: git init"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📋 Next Steps:"
echo ""
echo "1. Read: QUICK_START.md (5 minutes)"
echo "2. Push to GitHub:"
echo "   git add ."
echo "   git commit -m 'Add Render deployment'"
echo "   git push origin main"
echo ""
echo "3. Visit: https://render.com"
echo "4. Create new Web Service"
echo "5. Connect your GitHub repository"
echo "6. Set environment variables"
echo "7. Deploy! 🚀"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
