# University Student Association Management System

A comprehensive Django web application for managing university student associations, featuring member management, event organization, and social feed functionality.

## 🎯 Overview

This project is a complete student association management system built with Django that provides:

- **Member Management**: Organize association members by divisions and positions with hierarchical structure
- **Event Management**: Create, manage, and display upcoming and past events
- **Social Feed**: Interactive news feed with posts, likes, and comments
- **Responsive Design**: Modern, mobile-friendly interface

## ✨ Features

### 👥 Member Management
- **Hierarchical Organization**: Members organized by divisions and positions
- **Position Priority System**: Automatic ordering based on position hierarchy
- **Member Profiles**: Complete member information including photos, bios, and contact details
- **Division Management**: Organize members into different association divisions

### 📅 Event Management
- **Event Creation**: Add events with descriptions, images, dates, and locations
- **Event Categories**: Separate upcoming and past events
- **Event Details**: Detailed event pages with full information
- **Image Support**: Upload and display event images

### 📱 Social Feed
- **Post Management**: Create and manage association posts
- **Interactive Features**: Like and comment system
- **Session-based Interaction**: User-friendly like/comment system without requiring accounts
- **Media Support**: Posts can include images

### 🎨 User Interface
- **Modern Design**: Clean, professional interface with gradient backgrounds
- **Responsive Layout**: Works perfectly on desktop, tablet, and mobile devices
- **Interactive Elements**: Smooth animations and hover effects
- **Font Awesome Icons**: Professional iconography throughout

## 🛠️ Technology Stack

- **Backend**: Django 4.2.7
- **Database**: SQLite (development)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with modern design principles
- **Icons**: Font Awesome 6.0.0
- **Fonts**: Google Fonts (Inter)

## 📁 Project Structure

```
association/
├── association/          # Main Django project settings
│   ├── settings.py      # Django configuration
│   ├── urls.py          # Main URL routing
│   └── wsgi.py          # WSGI configuration
├── members/             # Member management app
│   ├── models.py        # Member, Division, Position models
│   ├── views.py         # Member-related views
│   └── urls.py          # Member URL patterns
├── events/              # Event management app
│   ├── models.py        # Event model
│   ├── views.py         # Event-related views
│   └── urls.py          # Event URL patterns
├── feed/                # Social feed app
│   ├── models.py        # Post, Like, Comment models
│   ├── views.py         # Feed-related views
│   └── urls.py          # Feed URL patterns
├── templates/           # HTML templates
│   ├── base.html        # Base template
│   ├── index.html       # Homepage
│   ├── members.html     # Member listing
│   ├── events.html      # Event listing
│   ├── event_detail.html # Event details
│   ├── feed.html        # Social feed
│   └── post_detail.html # Post details
├── static/              # Static files
│   ├── css/            # Stylesheets
│   ├── js/             # JavaScript files
│   └── images/         # Static images
├── media/               # User-uploaded files
│   ├── members/        # Member photos
│   ├── events/         # Event images
│   └── feed/           # Post images
└── manage.py           # Django management script
```
## 🖼️ Project Preview

### 🏠 Home Page
<img width="1850" height="920" alt="Screenshot 2025-10-18 234211" src="https://github.com/user-attachments/assets/da0b899f-ee18-4f72-b605-a1e1adb69670" />


### 👥 Our Team
<img width="1852" height="926" alt="Screenshot 2025-10-18 234238" src="https://github.com/user-attachments/assets/9cff912c-e089-4636-8ae5-293ac1537002" />

### Event 
<img width="1848" height="922" alt="Screenshot 2025-10-18 234257" src="https://github.com/user-attachments/assets/9accb7f5-1748-49cc-873c-4c19699ff8a2" />


### 📰 Feed
<img width="1864" height="927" alt="Screenshot 2025-10-18 234305" src="https://github.com/user-attachments/assets/39ccc00f-f853-49a3-936b-6dbc6d7b1e98" />

### 📞 Contact Page
<img width="1857" height="915" alt="Screenshot 2025-10-18 234313" src="https://github.com/user-attachments/assets/cada999b-c788-4a74-aaf6-57abdf454a5c" />


##  Admin
<img width="1866" height="927" alt="Screenshot 2025-10-18 234334" src="https://github.com/user-attachments/assets/3f3af195-4c90-45bf-8357-ec6fad57eb98" />



---

## 🎥 Demo Video

Watch the full demo below 👇


https://github.com/user-attachments/assets/6922a48c-fa66-4c66-beae-2cb3a1059c71



> 🎬 *Click the thumbnail to watch the project walkthrough on YouTube.*

---
## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd student_association
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   cd association
   python manage.py migrate
   ```

5. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Open your browser and go to `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## 📊 Database Models

### Member Management
- **Division**: Association divisions (e.g., Core, Cultural, Sports)
- **Position**: Specific roles within divisions with priority ordering
- **Member**: Individual member information and profile data

### Event Management
- **Event**: Event details including title, description, date, location, and images

### Social Feed
- **Post**: Association posts with content and media
- **Like**: User likes on posts (session-based)
- **Comment**: User comments on posts

## 🎨 Customization

### Adding New Divisions
1. Access Django admin panel
2. Navigate to Members > Divisions
3. Add new division with appropriate priority

### Managing Members
1. Go to Members > Members in admin panel
2. Add members with their positions and details
3. Upload member photos to the media/members/ directory

### Creating Events
1. Navigate to Events > Events in admin panel
2. Add event details including date, location, and description
3. Upload event images to the media/events/ directory

## 🔧 Configuration

### Settings
- **DEBUG**: Set to `False` in production
- **SECRET_KEY**: Change the secret key for production
- **ALLOWED_HOSTS**: Add your domain for production deployment
- **MEDIA_ROOT**: Configure media file storage
- **STATIC_ROOT**: Configure static file storage

### Database
- Currently configured for SQLite (development)
- For production, consider PostgreSQL or MySQL

## 📱 Usage

### For Association Administrators
1. **Member Management**: Add and organize association members
2. **Event Planning**: Create and manage association events
3. **Content Management**: Post updates and announcements
4. **User Engagement**: Monitor likes and comments on posts

### For Students/Visitors
1. **Browse Members**: View association leadership and members
2. **Check Events**: See upcoming and past events
3. **Read Updates**: Follow association news and announcements
4. **Interact**: Like and comment on posts

## 🚀 Deployment

### Production Checklist
- [ ] Set `DEBUG = False`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Set up proper database (PostgreSQL recommended)
- [ ] Configure static file serving
- [ ] Set up media file serving
- [ ] Use environment variables for sensitive settings
- [ ] Set up SSL certificate
- [ ] Configure web server (Nginx/Apache)

### Recommended Hosting Platforms
- **Heroku**: Easy Django deployment
- **DigitalOcean**: VPS with Django setup
- **AWS**: Scalable cloud hosting
- **PythonAnywhere**: Django-friendly hosting

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

For support and questions:
- Create an issue in the repository
- Contact the development team
- Check the Django documentation for technical questions

## 🔮 Future Enhancements

- [ ] User authentication system
- [ ] Email notifications
- [ ] Event registration system
- [ ] Member voting system
- [ ] Mobile app integration
- [ ] Advanced analytics
- [ ] Multi-language support
- [ ] API endpoints for mobile apps

---

**Built with ❤️ for university student associations**

