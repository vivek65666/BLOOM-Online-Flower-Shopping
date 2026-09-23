# 🌸 BLOOM – Online Flower Shopping

**BLOOM** is a Django-based online flower shopping platform that provides a complete e-commerce workflow for browsing flowers, managing a shopping cart, placing orders, and processing test payments through Razorpay.

The application supports separate **Customer, Admin, and Vendor workflows**, with **MySQL** for persistent data storage and environment variables for database configuration.

---

## ✨ Key Features

### 🛍️ Customer Features

* User registration and login
* User authentication
* Browse flowers and categories
* View product details
* Add products to cart
* Update cart quantities
* Remove products from cart
* Checkout and shipping details
* Razorpay test payment integration
* Payment success handling
* Order history
* Forgot-password functionality

### 💳 Payment & Order Flow

BLOOM integrates the **Razorpay Checkout** flow for test payments.

```text
Customer
   ↓
Browse Products
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
Capture Razorpay Payment ID
   ↓
Update Order Status
   ↓
Order Status = Paid
   ↓
Customer / Admin / Vendor Order View
```

Successful payments store the Razorpay payment/transaction ID with the order.

The application uses the following order-status values:

```text
or_status = 1
```

Paid/successful order.

```text
or_status = 0
```

Unpaid or incomplete order.

The Admin paid-order view displays only orders with `or_status = 1`.

> **Note:** Razorpay is configured for test/development payments. Production payment credentials should never be committed to the repository.

---

# 👥 User Roles

## 👤 Customer

Customers can:

* Create an account
* Log in and log out
* Browse flower products
* Browse product categories
* View product details
* Add products to the shopping cart
* Update cart quantities
* Remove cart items
* Enter checkout/shipping information
* Make Razorpay test payments
* View successful orders
* View order history
* Use forgot-password functionality

---

## 🛠️ Admin

Administrators can:

* Manage application data
* Manage products
* Manage categories
* Manage users
* View customer orders
* View successfully paid orders
* Access administrative records

### Admin View Orders

The Admin **View Orders** section displays successfully paid orders with information such as:

* Order ID
* Customer
* Product
* Quantity
* Price
* Total Amount
* Order Date

Unpaid orders (`or_status = 0`) are excluded from the paid-order view.

---

## 🏪 Vendor

Vendors can:

* Manage vendor products
* View orders related to their products
* Monitor customer purchases
* Access vendor-specific order information

---

# 🛠️ Technology Stack

| Category        | Technologies                                   |
| --------------- | ---------------------------------------------- |
| Backend         | Python, Django                                 |
| Database        | MySQL                                          |
| Frontend        | HTML5, CSS3, JavaScript                        |
| UI              | Bootstrap, SCSS                                |
| Payment         | Razorpay Checkout                              |
| ORM             | Django ORM                                     |
| Version Control | Git, GitHub                                    |
| Development     | Visual Studio Code, Python Virtual Environment |

---

# 🗂️ Project Structure

```text
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
```

---

# ⚙️ Setup Instructions

## 1. Clone the Repository

```bash
git clone https://github.com/vivek65666/BLOOM-Online-Flower-Shopping.git
```

## 2. Navigate to the Project

```bash
cd BLOOM-Online-Flower-Shopping
```

## 3. Create a Virtual Environment

### Windows

```powershell
python -m venv venv
```

Activate the environment:

```powershell
.\venv\Scripts\Activate.ps1
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## 5. Configure Environment Variables

Create a local `.env` file in the project root.

Example:

```env
DB_NAME=flower_shoping
DB_USER=your_mysql_user
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_PORT=3306
```

The Django project reads these values using environment variables.

**Do not commit `.env` to GitHub.**

## 6. Create the MySQL Database

Open MySQL and run:

```sql
CREATE DATABASE flower_shoping;
```

Make sure the values in your local `.env` file match your MySQL configuration.

## 7. Run Django Migrations

```bash
python manage.py migrate
```

## 8. Check the Project

```bash
python manage.py check
```

Expected output:

```text
System check identified no issues (0 silenced).
```

## 9. Start the Development Server

```bash
python manage.py runserver
```

Open the application at:

```text
http://127.0.0.1:8000/
```

---

# 🖥️ Application Screenshots

## 🏠 Home Page

![Home Page](screenshots/Home%20Page.png)

## 🔐 Login Screen

![Login Screen](screenshots/Login%20Screen.png)

## 📝 Registration Screen

![Registration Screen](screenshots/Registration%20Screen.png)

## 🌸 Shop Screen

![Shop Screen](screenshots/Shop%20Screen.png)

## 📦 Product / Order Details

![Order Details Screen](screenshots/Order%20Details%20Screen.png)

## 🛒 Cart Screen

![Cart Screen](screenshots/Cart%20Screen.png)

## 🛠️ Admin Screen

![Admin Screen](screenshots/Admin%20Screen.png)

## 🏪 Vendor Screen

![Vendor Screen](screenshots/Vendor%20Screen.png)

---

# 🔐 Security & Configuration

Sensitive configuration should not be committed to the repository.

The project uses environment variables for MySQL configuration:

```python
"NAME": os.getenv("DB_NAME"),
"USER": os.getenv("DB_USER"),
"PASSWORD": os.getenv("DB_PASSWORD"),
"HOST": os.getenv("DB_HOST"),
"PORT": os.getenv("DB_PORT"),
```

The `.gitignore` file protects local and sensitive files such as:

```text
.env
*.env
venv/
venv39/
__pycache__/
*.pyc
*.sqlite3
.vscode/
.idea/
*.log
```

Never commit:

* Database passwords
* API secrets
* Razorpay secret keys
* `.env` files
* Virtual environments
* Local database files

---

# 🧪 Project Validation

The following workflows have been tested during development:

* ✅ Customer registration and login
* ✅ Product browsing
* ✅ Product details
* ✅ Shopping cart
* ✅ Checkout
* ✅ Razorpay test payment
* ✅ Payment success handling
* ✅ Order creation
* ✅ Paid order status
* ✅ Customer order history
* ✅ Admin View Orders
* ✅ Vendor View Orders
* ✅ Unpaid orders excluded from Admin paid-order view
* ✅ Django system check

---

# 🚀 Future Improvements

* Product search and filtering
* Wishlist functionality
* Order tracking
* Customer reviews and ratings
* Email notifications
* Production deployment
* Improved mobile responsiveness
* Automated testing
* CI/CD pipeline
* Production payment configuration

---

# 📌 Project Status

**Core e-commerce workflow implemented and tested locally.**

The project currently supports product browsing, cart management, checkout, Razorpay test payments, customer order history, and role-specific Admin/Vendor order management.

---

# 👨‍💻 Author

**Vivek C Raj**

GitHub:
https://github.com/vivek65666

Repository:
https://github.com/vivek65666/BLOOM-Online-Flower-Shopping

---

# 📄 Resume-Ready Project Description

**BLOOM – Online Flower Shopping | Python, Django, MySQL, JavaScript, Razorpay**

Developed a Django-based e-commerce platform for online flower shopping with customer authentication, product catalog, shopping cart, checkout, Razorpay test payment integration, and order management. Implemented separate Customer, Admin, and Vendor workflows with MySQL-backed order persistence, payment-status handling, and paid-order filtering. Configured database credentials using environment variables and maintained the project using Git and GitHub.

---

⭐ If you find this project useful, consider giving it a star.
