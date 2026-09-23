🌸 BLOOM – Online Flower Shopping

BLOOM is a Django-based online flower shopping platform that provides a complete e-commerce workflow for browsing flowers, managing a shopping cart, placing orders, and processing test payments through Razorpay.

The application includes separate Customer, Admin, and Vendor workflows, with MySQL used for persistent data storage and environment variables used for database configuration.

✨ Key Features
🛍️ Customer Features
User registration and login
User authentication
Browse flowers and categories
View product details
Add products to cart
Update cart quantities
Remove products from cart
Checkout and shipping details
Razorpay test payment integration
Payment success handling
Order history
Forgot-password functionality
💳 Payment & Order Flow

BLOOM integrates the Razorpay Checkout flow for test payments.

Customer
   ↓
Add Product to Cart
   ↓
Checkout
   ↓
Create Order
   ↓
Razorpay Checkout
   ↓
Successful Payment
   ↓
Payment ID Captured
   ↓
Order Status = Paid
   ↓
Order History / Admin / Vendor View

Successful orders are stored with payment information including the Razorpay transaction/payment ID.

Orders with:

or_status = 1

are treated as successfully paid and are displayed in the Admin View Orders section.

Orders with:

or_status = 0

remain unpaid/incomplete and are excluded from the Admin paid-order view.

Note: Razorpay is configured for testing/development in this project. No real production payment credentials should be committed to the repository.

👥 User Roles
👤 Customer

Customers can:

Register and log in
Browse flower products
View product details
Add products to the cart
Manage cart items
Enter checkout information
Make Razorpay test payments
View successful orders
View order history
🛠️ Admin

Administrators can:

Manage application data
View customer orders
View successfully paid orders
Manage products and categories
Manage user/application records

The Admin View Orders page displays paid orders and includes information such as:

Order ID
Customer
Product
Quantity
Price
Total amount
Order date
🏪 Vendor

Vendors can:

Manage vendor products
View orders related to their products
Monitor customer purchases
Access vendor-specific order information
🛠️ Technology Stack
Backend
Python
Django
Django ORM
Frontend
HTML5
CSS3
JavaScript
Bootstrap
SCSS
Database
MySQL
Payment
Razorpay Checkout
Development Tools
Git
GitHub
Visual Studio Code
Python Virtual Environment
🗂️ Project Structure
BLOOM-Online-Flower-Shopping/
│
├── app/
│   ├── migrations/
│   ├── static/
│   │   └── media/
│   ├── templates/
│   │   └── web/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   └── views.py
│
├── project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── screenshots/
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
⚙️ Setup Instructions
1. Clone the Repository
git clone https://github.com/vivek65666/BLOOM-Online-Flower-Shopping.git
2. Navigate to the Project
cd BLOOM-Online-Flower-Shopping
3. Create a Virtual Environment
Windows
python -m venv venv

Activate it:

.\venv\Scripts\Activate.ps1
Linux / macOS
python3 -m venv venv
source venv/bin/activate
4. Install Dependencies
pip install -r requirements.txt
5. Configure Environment Variables

Create a local .env file in the project root.

Example:

DB_NAME=flower_shoping
DB_USER=your_mysql_user
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_PORT=3306

Do not commit the .env file to GitHub.

The project uses environment variables in project/settings.py for database configuration.

6. Create the MySQL Database

Create a MySQL database:

CREATE DATABASE flower_shoping;

Then make sure the credentials in your local .env file match your MySQL configuration.

7. Run Django Migrations
python manage.py migrate
8. Check the Project
python manage.py check

Expected result:

System check identified no issues (0 silenced).
9. Start the Development Server
python manage.py runserver

Open:

http://127.0.0.1:8000/
```

🖥️ Application Screenshots

### Home Page
![Home Page](screenshots/Home%20Page.png)

### Login Screen
![Login Screen](screenshots/Login%20Screen.png)

### Registration Screen
![Registration Screen](screenshots/Registration%20Screen.png)

### Shop Screen
![Shop Screen](screenshots/Shop%20Screen.png)

### Product / Order Details Screen
![Order Details Screen](screenshots/Order%20Details%20Screen.png)

### Cart Screen
![Cart Screen](screenshots/Cart%20Screen.png)

### Admin Screen
![Admin Screen](screenshots/Admin%20Screen.png)

### Vendor Screen
![Vendor Screen](screenshots/Vendor%20Screen.png)

## 👤 User Functionality

Users can:

* Create an account
* Log in and log out
* Browse flowers
* View product information
* Add products to the cart
* Manage cart quantities
* Place orders
* Manage their account

## ⚙️ Admin Functionality

The Django admin interface can be used to manage application data such as:

* Products
* Categories
* Users
* Orders
* Other application records

## 🔐 Security

Sensitive configuration such as environment variables and local database files should not be committed to the repository.

The project uses `.gitignore` to prevent files such as virtual environments, environment variables, Python cache files, and local database files from being committed.

## 🚀 Future Improvements

* Online payment gateway integration
* Product search and filtering
* Wishlist functionality
* Order tracking
* Customer reviews and ratings
* Email notifications
* Production deployment
* Improved mobile responsiveness

## 📌 Project Status

This project is developed as a Django-based online flower shopping application and is currently under development/improvement.

## 👨‍💻 Author

**Vivek C Raj**

GitHub: https://github.com/vivek65666

---

⭐ If you find this project useful, consider giving it a star.
