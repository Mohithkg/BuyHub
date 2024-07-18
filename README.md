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

   git clone https://github.com/Mohithkg/BuyHub.git  <br />
   cd BuyHub

3. **Create a Virtual Environment and Activate It**
    python -m venv env  <br />
    source env/bin/activate <br /> # On Windows use `env\Scripts\activate`


4. **Install the Required Packages** <br />
    pip install -r requirements.txt

5. **Configure PostgreSQL Database**

        Update the DATABASES setting in BuyHub/settings.py with your PostgreSQL credentials: <br />
         DATABASES = { <br />
          'default': { <br />
              'ENGINE': 'django.db.backends.postgresql', <br />
              'NAME': 'your_db_name', <br />
              'USER': 'your_db_user', <br />
              'PASSWORD': 'your_db_password', <br />
              'HOST': 'your_db_host', <br />
              'PORT': 'your_db_port', <br />
          } <br />
       }

5. **Run Migrations** <br />
  python manage.py makemigrations <br />
  python manage.py migrate

6. **Create a Superuser** <br />
  python manage.py createsuperuser

7. **Run the Development Server** <br />
   python manage.py runserver <br />
    Visit http://127.0.0.1:8000/ to access the application locally.

### Usage
**Product Listing**: Browse products listed under various categories. <br />
**Cart Management**: Add products to the cart and manage cart items. <br />
**Order Processing**: Place orders and track order details. <br />

### Deployment <br />
The application is deployed on Render. You can access it live at BuyHub on Render.

### Contributing <br />
Contributions are welcome! Please fork the repository and create a pull request with your changes.

### License <br />
This project is licensed under the MIT License.
