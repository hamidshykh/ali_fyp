# Smart CV Submission System

A Django-based intelligent CV/Resume submission and analysis system with NLP capabilities for parsing and profiling job applications.

## System Requirements

- Python 3.10 or higher
- Windows OS (tested on Windows 10/11)
- 4GB RAM minimum
- Internet connection (for initial setup)

## Quick Setup Guide

### Step 1: Extract Project
```bash
# Extract the zip file to your desired location
# Example: D:\projects\smart_cv_submission_system
```

### Step 2: Install Microsoft Visual C++ Redistributable
Download and install from: https://aka.ms/vs/17/release/vc_redist.x64.exe
(Required for spaCy/thinc libraries)

### Step 3: Create Virtual Environment
```bash
cd smart_cv_sumbmission_system
python -m venv .venv
.venv\Scripts\activate
```

### Step 4: Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 5: Download spaCy Language Model
```bash
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.7.1/en_core_web_sm-3.7.1-py3-none-any.whl
```

### Step 6: Download NLTK Data
```bash
python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt'); nltk.download('averaged_perceptron_tagger'); nltk.download('maxent_ne_chunker'); nltk.download('words')"
```

### Step 7: Configure Django Settings
Edit `smart_cv_sumbmission_system/settings.py` and ensure these settings exist:

```python
# Static files configuration
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Crispy Forms configuration
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4"

# Make sure these are in INSTALLED_APPS
INSTALLED_APPS = [
    # ... other apps ...
    'crispy_forms',
    'crispy_bootstrap4',
    # ... other apps ...
]
```

### Step 8: Run Migrations
```bash
python manage.py migrate
```

### Step 9: Create Superuser
```bash
python manage.py createsuperuser
```
Follow the prompts to create admin credentials.

### Step 10: Run Development Server
```bash
python manage.py runserver
```

## Access the Application

- **Main Application**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/
- **Job Application Form**: http://127.0.0.1:8000/apply/
- **Job Listings**: http://127.0.0.1:8000/jobs/

## Important Notes

### File Paths
The project uses these important directories:
- `resumes/` - Uploaded CV/resume files
- `staticfiles/` - Collected static files
- `media/` - User uploaded media files

### Common Issues & Solutions

**Issue 1: DLL load failed error**
- Solution: Install Visual C++ Redistributable (Step 2)

**Issue 2: spaCy model not found**
- Solution: Run Step 5 to install the language model

**Issue 3: NLTK data not found**
- Solution: Run Step 6 to download NLTK data

**Issue 4: Template not found (bootstrap4)**
- Solution: Ensure `crispy-bootstrap4` is installed and configured in settings.py

**Issue 5: STATIC_ROOT not configured**
- Solution: Add `STATIC_ROOT = BASE_DIR / 'staticfiles'` in settings.py

## Project Structure

```
smart_cv_sumbmission_system/
├── manage.py
├── requirements.txt
├── README.md
├── smart_cv_sumbmission_system/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── system/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── application_profiler.py
│   └── templates/
├── resumes/
└── staticfiles/
```

## Features

- CV/Resume upload and parsing (PDF, DOCX)
- NLP-based text extraction and analysis
- Keyword extraction using RAKE
- Skills matching and profiling
- Job application management
- Admin dashboard for application review

## Technology Stack

- **Framework**: Django 4.2.7
- **NLP**: spaCy, NLTK, rake-nltk
- **ML**: scikit-learn
- **PDF Processing**: pdfminer.six
- **Document Processing**: python-docx, docx2txt
- **UI**: Bootstrap 4, Crispy Forms

## Development

To collect static files for production:
```bash
python manage.py collectstatic
```

To create new migrations after model changes:
```bash
python manage.py makemigrations
python manage.py migrate
```

## Troubleshooting

If you encounter any module import errors:
1. Make sure virtual environment is activated
2. Check that all requirements are installed: `pip list`
3. Reinstall the missing package: `pip install <package-name>`

For database issues:
1. Delete `db.sqlite3` file
2. Run `python manage.py migrate` again
3. Recreate superuser

## Support

For issues or questions:
1. Check the error message in terminal
2. Verify all setup steps were completed
3. Ensure virtual environment is activated
4. Check Django version compatibility

## License

[Your License Here]

## Contributors

[Your Name/Team]