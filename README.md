# Django Real Estate Website

A comprehensive real estate website built with Django, featuring property listings, agent profiles, and advanced search functionality with Nigerian Naira (₦) currency support.

## Features

- **Property Management**: Sale, rent, and shortlet listings
- **Agent Profiles**: Detailed agent information with ratings and reviews
- **Advanced Search & Filtering**: Location, price, property type, and amenities
- **Responsive Design**: Mobile-first Bootstrap 5 design
- **Admin Panel**: Django Jazzmin admin interface
- **Nigerian Market**: Naira currency and Nigerian locations

## Installation

1. **Clone the repository**
\`\`\`bash
git clone <repository-url>
cd django-real-estate
\`\`\`

2. **Create virtual environment**
\`\`\`bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
\`\`\`

3. **Install dependencies**
\`\`\`bash
pip install -r requirements.txt
\`\`\`

4. **Run migrations**
\`\`\`bash
python manage.py makemigrations
python manage.py migrate
\`\`\`

5. **Create superuser**
\`\`\`bash
python manage.py createsuperuser
\`\`\`

6. **Load sample data**
\`\`\`bash
python manage.py shell < scripts/create_sample_data.py
\`\`\`

7. **Run development server**
\`\`\`bash
python manage.py runserver
\`\`\`

## Project Structure

\`\`\`
real_estate/
├── real_estate/          # Main project settings
├── properties/           # Property management app
├── agents/              # Agent management app
├── accounts/            # User accounts app
├── templates/           # HTML templates
├── static/             # CSS, JS, images
├── media/              # User uploaded files
└── scripts/            # Utility scripts
\`\`\`

## Key Components

### Models
- **Property**: Main property model with all listing details
- **PropertyImage**: Multiple images per property
- **Agent**: Agent profiles with ratings and specialties
- **PropertyInquiry**: Contact form submissions

### Views
- **Home**: Featured properties and agents
- **Property Lists**: Filtered property listings by type
- **Agent Lists**: Agent directory with filtering
- **Search**: Advanced search functionality

### Admin
- **Jazzmin Interface**: Modern admin panel
- **Inline Editing**: Property images inline editing
- **Bulk Actions**: Mass property management

## Configuration

### Settings
- Database: SQLite (development)
- Static Files: Local storage
- Media Files: Local storage
- Time Zone: Africa/Lagos
- Currency: Nigerian Naira (₦)

### Jazzmin Admin
- Custom branding and colors
- Enhanced navigation
- Search functionality
- Responsive design

## Usage

### Adding Properties
1. Access admin panel at `/admin/`
2. Navigate to Properties > Properties
3. Add new property with details and images
4. Set featured status for homepage display

### Managing Agents
1. Create user account first
2. Add agent profile with professional details
3. Link properties to agents
4. Manage ratings and reviews

### Customization
- Update `static/css/style.css` for styling
- Modify templates in `templates/` directory
- Add new property types in models
- Extend search functionality in views

## API Endpoints

- `/` - Homepage
- `/properties/sale/` - Properties for sale
- `/properties/rent/` - Properties for rent
- `/shortlets/` - Shortlet properties
- `/agents/` - Agent directory
- `/admin/` - Admin panel

## Contributing

1. Fork the repository
2. Create feature branch
3. Make changes
4. Test thoroughly
5. Submit pull request

## License

This project is licensed under the MIT License.
