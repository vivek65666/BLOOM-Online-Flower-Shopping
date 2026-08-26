# 🌸 BLOOM – Online Flower Shopping

BLOOM is a web-based online flower shopping platform built with **Python and Django**. The application allows users to browse flowers, explore categories, view product details, manage their shopping cart, and place orders through a simple e-commerce interface.

## ✨ Features

* 🌺 Browse available flowers and products
* 🏷️ Product categories
* 🔎 Product details and information
* 👤 User registration and login
* 🔐 Authentication and account management
* 🛒 Add products to shopping cart
* ➕ Update product quantities
* 🗑️ Remove products from cart
* 📦 Order management
* 🔑 Forgot password functionality
* ⚙️ Django admin panel for managing application data
* 📱 Responsive web interface

## 🛠️ Technologies Used

### Backend

* Python
* Django

### Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap
* SCSS

### Database

- MySQL

### Development Tools

* Git
* GitHub
* Visual Studio Code

## 📂 Project Structure

```text
BLOOM-Online-Flower-Shopping/
│
├── app/
│   ├── migrations/
│   ├── static/
│   ├── templates/
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
├── manage.py
├── .gitignore
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/vivek65666/BLOOM-Online-Flower-Shopping.git
```

### 2. Navigate to the project

```bash
cd BLOOM-Online-Flower-Shopping
```

### 3. Create a virtual environment

Windows:

```bash
python -m venv venv
```

### 4. Activate the virtual environment

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Run the development server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

🖥️ Application Screenshots

### Home Page
![Home Page](screenshots)

### Login Screen
![Login Screen](screenshots)

### Registration Screen
![Registration Screen](screenshots)

### Shop Screen
![Shop Screen](screenshots)

### Product / Order Details Screen
![Order Details Screen](screenshots)

### Cart Screen
![Cart Screen](screenshots)

### Admin Screen
![Admin Screen](screenshots)

### Vendor Screen
![Vendor Screen](screenshots)

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
