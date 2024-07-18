# BuyHub

BuyHub is a comprehensive ecommerce application developed using Django for the backend and HTML, Bootstrap, and JavaScript for the frontend. It offers essential functionalities like product listing, cart management, and order processing.

## Features

### Django Applications
- **Account**: Manages user login, registration, and logout.
- **Store**: Stores product information and variations such as size and color.
- **Category**: Lists products under various categories.
- **Carts**: Tracks products added to the cart, including cart items.
- **Order**: Contains order details, ordered product details, and payment information.

### Database
- **PostgreSQL**: Used for storing and managing the application’s data.

### Deployment
- **Render**: The application is deployed on Render. You can access it [here](https://buyhub.onrender.com).

## Project Setup

### Prerequisites
- Python 3.x
- Django
- PostgreSQL

### Installation

1. **Clone the Repository**

   git clone https://github.com/Mohithkg/BuyHub.git
   cd BuyHub

2. **Create a Virtual Environment and Activate It**
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`


3. **Install the Required Packages** 
    pip install -r requirements.txt

4. **Configure PostgreSQL Database**

  Update the DATABASES setting in BuyHub/settings.py with your PostgreSQL credentials:
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'your_db_host',
        'PORT': 'your_db_port',
    }
}

5. **Run Migrations**
  python manage.py makemigrations
  python manage.py migrate

6. **Create a Superuser**
  python manage.py createsuperuser

7. **Run the Development Server**
   python manage.py runserver
    Visit http://127.0.0.1:8000/ to access the application locally.

### Usage
**Product Listing**: Browse products listed under various categories.
**Cart Management**: Add products to the cart and manage cart items.
**Order Processing**: Place orders and track order details.

### Deployment
The application is deployed on Render. You can access it live at BuyHub on Render.

### Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

### License
This project is licensed under the MIT License.
