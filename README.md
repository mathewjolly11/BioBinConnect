# BioBinConnect 🌱

**Smart Biodegradable Waste Management Platform**

A comprehensive web-based waste management system that connects households, collectors, compost managers, and farmers in a circular economy ecosystem.

[![Django](https://img.shields.io/badge/Django-6.0-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-orange.svg)](https://www.mysql.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Stakeholder Roles](#stakeholder-roles)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 🌟 Overview

BioBinConnect is a Django-based platform that revolutionizes biodegradable waste management by creating a seamless connection between waste generators (households), collectors, processors (compost managers), and end-users (farmers). The system promotes sustainability, reduces manual errors, and supports a zero-waste circular economy.

### Key Highlights

- 🏠 **27 Active Users** across 5 stakeholder types
- ♻️ **2,500+ kg** of waste collected and processed
- 🌾 **363+ kg** of compost produced
- 📊 **Real-time tracking** of collections, inventory, and payments
- 💰 **Automated salary** calculations and payment processing

---

## ✨ Features

### For Households

- 📦 Request waste pickups with auto-collector assignment
- 💳 Monthly payment processing (UPI/Cash/Card)
- 📊 Track pickup history and payment records
- 📧 Email confirmations for pickups

### For Collectors

- 📋 Daily pickup schedules with route assignments
- ⚖️ Log collections with actual weights
- 📦 Manage waste inventory (30-day auto-expiry)
- 🚚 Handle farmer orders and deliveries
- 💰 Track earnings (₹1,000 per day worked)

### For Compost Managers

- 🍂 Create compost batches from collected waste
- 📊 Quality grading system (Premium/A/B/C)
- 💵 Set pricing per kg
- 📈 Track batch status (Processing → Ready → Sold)
- 💰 Earn ₹1,000 per day worked

### For Farmers

- 🛒 Browse and order organic waste or compost
- 📦 Track order status and deliveries
- 💳 Multiple payment options
- 📊 View complete order history

### For Admins

- 👥 User management and approval system
- 🗺️ Infrastructure setup (districts, locations, routes)
- 👷 Collector assignment to routes and days
- 💰 Salary processing with UPI PIN security
- 📊 Comprehensive reports and analytics
- ⚙️ System settings configuration

---

## 🏗️ System Architecture

```
┌─────────────┐     ┌─────────────┐     ┌──────────────┐     ┌─────────┐
│  Household  │────▶│  Collector  │────▶│   Compost    │────▶│ Farmer  │
│             │     │             │     │   Manager    │     │         │
└─────────────┘     └─────────────┘     └──────────────┘     └─────────┘
      │                   │                     │                  │
      │                   │                     │                  │
      └───────────────────┴─────────────────────┴──────────────────┘
                                  │
                            ┌─────▼─────┐
                            │   Admin   │
                            │  System   │
                            └───────────┘
```

### Workflow

1. **Household** requests pickup → Auto-assigned to **Collector**
2. **Collector** collects waste → Logs in inventory
3. **Compost Manager** creates batches → Processes into compost
4. **Farmer** orders products → Receives delivery
5. **Admin** manages system → Processes payments

---

## 🛠️ Tech Stack

### Backend

- **Framework:** Django 6.0
- **Language:** Python 3.x
- **Database:** MySQL 8.0
- **ORM:** Django ORM

### Frontend

- **HTML5** with Django Templates
- **CSS3** (Vanilla CSS)
- **JavaScript** (Vanilla JS + AJAX)
- **Icons:** Icofont

### Key Libraries

- `django-cors-headers` - CORS handling
- `mysqlclient` - MySQL database adapter
- `Pillow` - Image processing
- `python-decouple` - Environment configuration

---

## 📥 Installation

### Prerequisites

- Python 3.8 or higher
- MySQL 8.0 or higher
- pip (Python package manager)

### Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/BioBinConnect.git
cd BioBinConnect/MyProject
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Database Setup

```bash
# Create MySQL database
mysql -u root -p
CREATE DATABASE db_biobinconnect;
EXIT;

# Import database schema (optional)
mysql -u root -p db_biobinconnect < db_biobinconnect.sql
```

### Step 5: Configure Environment

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
DB_NAME=db_biobinconnect
DB_USER=root
DB_PASSWORD=your-mysql-password
DB_HOST=localhost
DB_PORT=3306
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### Step 6: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 7: Create Superuser

```bash
python manage.py createsuperuser
```

### Step 8: Run Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

---

## ⚙️ Configuration

### System Settings

Configure via Admin Panel → System Settings:

| Setting                    | Default | Description                                      |
| -------------------------- | ------- | ------------------------------------------------ |
| `compost_conversion_ratio` | 4       | Waste to compost ratio (4kg waste = 1kg compost) |
| `waste_price_per_kg`       | ₹10.00  | Default waste price for farmers                  |
| `auto_unavailable_days`    | 30      | Days before waste auto-expires                   |
| `low_stock_threshold`      | 50kg    | Low inventory warning level                      |
| `expiry_warning_days`      | 7       | Days before expiry warning                       |

### Email Configuration

Update `settings.py` for email notifications:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
```

---

## 🚀 Usage

### Admin Access

1. Navigate to `/admin/`
2. Login with superuser credentials
3. Manage users, routes, and system settings

### User Registration

1. Visit homepage
2. Click "Sign Up"
3. Select role (Household/Collector/Manager/Farmer)
4. Complete registration form
5. Wait for admin approval

### Household Workflow

1. Login → Dashboard
2. Click "Request Pickup"
3. Select bin type and estimated weight
4. System auto-assigns collector
5. Receive email confirmation
6. Make monthly payment

### Collector Workflow

1. Login → View today's pickups
2. Visit households on route
3. Log collection with actual weight
4. Manage inventory
5. Fulfill farmer orders

### Manager Workflow

1. Login → Browse available waste
2. Create compost batch
3. Set quality grade and price
4. Update status when ready
5. Track sales to farmers

### Farmer Workflow

1. Login → Browse products
2. Select waste or compost
3. Place order with delivery address
4. Track order status
5. Make payment on delivery

---

## 👥 Stakeholder Roles

### 1. Admin

- **Count:** 1
- **Responsibilities:** System management, user approval, salary processing
- **Key Features:** 43 admin functions

### 2. Household

- **Count:** 13
- **Responsibilities:** Generate waste, request pickups, make payments
- **Key Features:** 12 household functions

### 3. Collector

- **Count:** 6
- **Responsibilities:** Collect waste, manage inventory, deliver orders
- **Key Features:** 15 collector functions
- **Earnings:** ₹1,000 per day worked

### 4. Compost Manager

- **Count:** 2
- **Responsibilities:** Process waste into compost, manage batches
- **Key Features:** 13 manager functions
- **Earnings:** ₹1,000 per day worked

### 5. Farmer

- **Count:** 4
- **Responsibilities:** Purchase waste/compost for farming
- **Key Features:** 14 farmer functions

---

## 📁 Project Structure

```
BioBinConnect/MyProject/
├── GuestApp/              # Guest & authentication
│   ├── models.py          # User models (Household, Collector, etc.)
│   ├── views.py           # Authentication views
│   └── forms.py           # Registration forms
├── HouseholdApp/          # Household features
│   ├── views.py           # Pickup requests, payments
│   └── urls.py            # Household routes
├── CollectorApp/          # Collector features
│   ├── views.py           # Collections, inventory, deliveries
│   └── urls.py            # Collector routes
├── CompostManagerApp/     # Manager features
│   ├── views.py           # Batch creation, management
│   └── urls.py            # Manager routes
├── FarmerApp/             # Farmer features
│   ├── views.py           # Product browsing, orders
│   └── urls.py            # Farmer routes
├── MyApp/                 # Core & admin features
│   ├── models.py          # Core models (Routes, Batches, etc.)
│   ├── views.py           # Admin dashboard
│   ├── salary_views.py    # Salary processing
│   ├── sales_views.py     # Sales management
│   └── constants.py       # System constants
├── templates/             # HTML templates
│   ├── Guest/             # Guest pages
│   ├── HouseHold/         # Household pages
│   ├── Collector/         # Collector pages
│   ├── Farmer/            # Farmer pages
│   ├── CompostManager/    # Manager pages
│   └── Admin/             # Admin pages
├── static/                # Static files (CSS, JS, images)
├── media/                 # User uploads
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

---

## 💰 Pricing & Payments

### Revenue Model

- **Household Payments:** Monthly service fees (₹50-₹100 per bin)
- **Farmer Purchases:** Waste (₹10/kg) and Compost (₹200/kg)

### Expense Model

- **Collector Salaries:** ₹1,000 per day worked
- **Manager Salaries:** ₹1,000 per day worked

### Payment Methods

- 💳 UPI (Unified Payments Interface)
- 💵 Cash on Delivery
- 💳 Card Payment

---

## 📊 Current Statistics

- **Total Users:** 27
- **Waste Collected:** ~2,500 kg (56 pickups)
- **Compost Produced:** ~363.5 kg (8 batches)
- **Active Routes:** 6
- **Districts:** 1 (Idukki, Kerala)
- **Completion Rate:** 100%

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Coding Standards

- Follow PEP 8 for Python code
- Use meaningful variable names
- Add comments for complex logic
- Write unit tests for new features

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📞 Contact

**Project Maintainer:** BioBinConnect Team

- **Email:** contact@biobinconnect.com
- **Phone:** +91 9746573645
- **Location:** Green Valley, Eco District, Kerala
- **Hours:** Monday - Friday: 08:00 AM - 06:00 PM

---

## 🙏 Acknowledgments

- Django community for the excellent framework
- All contributors and testers
- Local communities in Kerala for feedback

---

## 🔮 Future Enhancements

- [ ] Mobile app for Android/iOS
- [ ] Real-time GPS tracking for collectors
- [ ] AI-based waste classification
- [ ] Integration with government waste management systems
- [ ] Multi-language support
- [ ] Advanced analytics dashboard
- [ ] Blockchain for transparent transactions

---

**Made with ❤️ for a sustainable future**
