from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Custom user manager to handle user creation with additional validations.
class MyAccountManager(BaseUserManager):

    #Custom manager for the Account model, handling user creation and superuser creation.
    def create_user(self, first_name, last_name, username, email, password = None):
        """
            Create and return a regular user with an email and password.
               Args:
                   first_name (str): User's first name.
                   last_name (str): User's last name.
                   username (str): User's username.
                   email (str): User's email address.
                   password (str): User's password.
        """
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have an username')

        user=self.model(
            email=self.normalize_email(email),
            username= username,
            first_name= first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, first_name, last_name, username, password):
        """
               Create and return a superuser with the given email and password.
               Args:
                   email (str): Superuser's email address.
                   first_name (str): Superuser's first name.
                   last_name (str): Superuser's last name.
                   username (str): Superuser's username.
                   password (str): Superuser's password.

        """
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        # Set superuser permissions and attributes
        user.is_admin=True
        user.is_active=True
        user.is_staff=True
        user.is_superadmin=True
        user.save(using=self._db)
        return user

# Custom user model extending AbstractUser to include additional fields.
class Account(AbstractUser):
    #Custom user model extending AbstractUser to include additional fields.

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)

    #Required fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    # Use email for authentication instead of username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']

    # Set custom manager
    objects= MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        #Check if the user has a specific permission.
        return self.is_admin

    def has_module_perms(self, app_label):
        #Check if the user has permissions for a specific app.
        return True
