🛒 Ecommerce Website (Django + JavaScript)

This is a full-featured Ecommerce web application built with Django (backend) and JavaScript (frontend).
It provides a simple, scalable foundation for online shopping systems with user authentication, product management, and cart functionality.

🚀 Features

🔐 User Authentication (Register, Login, Logout)

🛍️ Product Catalog with images, categories, and details

🛒 Shopping Cart (Add to Cart, Remove from Cart, Update Quantity)

💳 Checkout Flow (order summary & purchase simulation)

🎨 Responsive UI using HTML, CSS, Bootstrap

📂 Django Admin Panel for managing products and users

⚡ JavaScript Enhancements for dynamic cart and UI updates

🛠️ Tech Stack

Frontend:

HTML, CSS, Bootstrap

JavaScript (vanilla)

Backend:

Django (Python Framework)

Django Templating Engine

SQLite3 (default, can be switched to MySQL/PostgreSQL)

📂 Project Structure
Ecommerce-django-and-javascript/
│── shop/                # Main Django app
│   ├── templates/       # HTML templates
│   ├── static/          # Static files (CSS, JS, images)
│   ├── views.py         # Views & business logic
│   ├── urls.py          # URL routes
│   └── models.py        # Database models
│
│── static/              # Project-wide static files
│── db.sqlite3           # Default database
│── manage.py            # Django project manager
└── README.md            # Project documentation

⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/Rushendrababu001/Ecommerce-django-and-javascript.git
cd Ecommerce-django-and-javascript

2. Create Virtual Environment & Install Dependencies
python -m venv venv
venv\Scripts\activate    # On Windows
source venv/bin/activate # On Mac/Linux

pip install -r requirements.txt

3. Run Database Migrations
python manage.py migrate

4. Create Superuser (Admin)
python manage.py createsuperuser

5. Start Development Server
python manage.py runserver


Visit 👉 http://127.0.0.1:8000/

📸 Screenshots (Optional)

Add some screenshots of your project UI here.

📌 Future Enhancements

Payment Gateway Integration (Razorpay/Stripe)

Product Reviews & Ratings

Order History & Tracking

Wishlist Feature

REST API with Django Rest Framework

🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.
