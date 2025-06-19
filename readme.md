# Task Management App

A full-stack task management application built with Django (backend) and React (frontend), featuring project organization, task tracking, and user collaboration.

## 🚀 Features

- **Task Management**: Create, edit, delete, and organize tasks
- **Project Organization**: Group tasks into projects with team collaboration
- **Priority System**: Set task priorities (Low, Medium, High, Urgent)
- **Status Tracking**: Track task progress (To Do, In Progress, In Review, Done)
- **User Authentication**: Secure user registration and login
- **Comments**: Add comments and collaborate on tasks
- **Responsive Design**: Works on desktop and mobile devices

## 🛠️ Tech Stack

### Backend
- **Django** - Python web framework
- **Django REST Framework** - API development
- **PostgreSQL** - Database (via Supabase)
- **Django CORS Headers** - Cross-origin resource sharing

### Frontend
- **React** - JavaScript library for UI
- **Axios** - HTTP client for API calls
- **CSS3** - Styling and responsive design

### Database
- **PostgreSQL** - Relational database hosted on Supabase

## 📋 Prerequisites

- Python 3.8+
- Node.js 14+
- npm or yarn
- Git

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/task-management-app.git
cd task-management-app
```

### 2. Backend Setup

#### Create Virtual Environment
```bash
python -m venv django_env
source django_env/bin/activate  # On Windows: django_env\Scripts\activate
```

#### Install Backend Dependencies
```bash
pip install django djangorestframework django-cors-headers psycopg2-binary
```

#### Database Configuration
1. Sign up for a free account at [Supabase](https://supabase.com)
2. Create a new project
3. Get your database connection details
4. Update `settings.py` with your database credentials:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'your-supabase-password',
        'HOST': 'db.your-project.supabase.co',
        'PORT': '5432',
    }
}
```

#### Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

#### Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

#### Start Backend Server
```bash
python manage.py runserver
```
Backend will run on `http://localhost:8000`

### 3. Frontend Setup

#### Navigate to Frontend Directory
```bash
cd task-frontend  # or wherever your React app is located
```

#### Install Frontend Dependencies
```bash
npm install
# or
yarn install
```

#### Start Frontend Server
```bash
npm start
# or
yarn start
```
Frontend will run on `http://localhost:3000`

## 🗂️ Project Structure

```
task-management-app/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── tasks/                    # Django app
│   ├── models.py            # Database models
│   ├── views.py             # API views
│   ├── serializers.py       # DRF serializers
│   ├── urls.py              # URL patterns
│   └── migrations/          # Database migrations
├── task-frontend/           # React frontend
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── App.js           # Main App component
│   │   └── index.js         # Entry point
│   ├── public/              # Static files
│   └── package.json         # Node.js dependencies
└── README.md               # This file
```

## 🗄️ Database Schema

### Models

**Project**
- name, description, owner, members
- created_at, updated_at, is_active
- Relationships: One-to-many with Tasks

**Task**
- title, description, status, priority
- due_date, created_at, updated_at, completed_at
- Relationships: Many-to-one with Project and User

**Comment**
- content, created_at, updated_at
- Relationships: Many-to-one with Task and User

## 🔌 API Endpoints

### Tasks
- `GET /api/tasks/` - List all tasks
- `POST /api/tasks/` - Create new task
- `GET /api/tasks/{id}/` - Get task details
- `PUT /api/tasks/{id}/` - Update task
- `DELETE /api/tasks/{id}/` - Delete task

### Projects
- `GET /api/projects/` - List all projects
- `POST /api/projects/` - Create new project
- `GET /api/projects/{id}/` - Get project details

### Authentication
- `POST /api/auth/login/` - User login
- `POST /api/auth/register/` - User registration
- `POST /api/auth/logout/` - User logout

## 🚀 Deployment

### Backend Deployment (Render)
1. Connect your GitHub repository to [Render](https://render.com)
2. Create a new Web Service
3. Set environment variables for database connection
4. Deploy automatically from GitHub

### Frontend Deployment (Vercel)
1. Connect your GitHub repository to [Vercel](https://vercel.com)
2. Configure build settings for React
3. Update API URLs to point to your deployed backend
4. Deploy automatically from GitHub

### Database (Supabase)
- Already configured with free PostgreSQL hosting
- Automatic backups and scaling included

## 🧪 Testing

### Backend Tests
```bash
python manage.py test
```

### Frontend Tests
```bash
npm test
# or
yarn test
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 Environment Variables

Create a `.env` file in the root directory:

```env
# Database
DATABASE_URL=your-supabase-connection-string

# Django
SECRET_KEY=your-secret-key
DEBUG=True

# CORS (for development)
CORS_ALLOWED_ORIGINS=http://localhost:3000
```

## 🐛 Troubleshooting

### Common Issues

**Database Connection Error**
- Verify Supabase credentials in settings.py
- Check if PostgreSQL driver is installed: `pip install psycopg2-binary`

**CORS Error**
- Ensure `django-cors-headers` is installed and configured
- Add frontend URL to `CORS_ALLOWED_ORIGINS`

**Migration Issues**
- Delete migration files (keep `__init__.py`)
- Run `python manage.py makemigrations` and `python manage.py migrate`

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Your Name** - *Initial work* - [YourGitHub](https://github.com/yourusername)

## 🙏 Acknowledgments

- Django documentation and community
- React documentation and community
- Supabase for free PostgreSQL hosting
- All open source contributors