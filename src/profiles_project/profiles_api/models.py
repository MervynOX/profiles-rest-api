from django.db import models
from django.contrib.auth.models import AbstractBaseUser #import it so we can later substitue it woth our very own custom model
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


class UserProfileManager(BaseUserManager):
    """Helps Django work with our custom user model"""

    def create_user(self, email, first_name, last_name, password=None):
            """Creates a new user profile object"""

            #when no email or invalid
            if not email:
                raise ValueError('Users must have an email address.')

            #normalize converts all into lowercase
            email = self.normalize_email(email)
            user = self.model(email=email, first_name=first_name, last_name=last_name)

            #it will encrypt password
            user.set_password(password)
            user.save(using=self._db)

            return user

    #admin
    def create_superuser(self, email, first_name,last_name, password):
        """Creates and saves a new superuser with given details"""

        user = self.create_user(email, first_name, last_name, password)

        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True

        user.save(using=self._db)

        return user

    def create_adminuser(self, email, name, password):
        """Creates and saves a new admin with given details"""

        user = self.create_user(email, name, password)

        user.is_admin = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represent a "user profile" inside our system"""

    email = models.EmailField(max_length=255, unique=True) #unique means one and only one
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True) #needed for substition later
    is_staff = models.BooleanField(default=False) #needed for substition later

    #object manager to manage user profile *needed for substition later
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    #will be used later on with the django admin
    def get_full_name(self):                        #possible to make this into a get_first_name and get_last_name
        """Used to get a users full name"""

        return self.first_name

    def get_short_name(self):                       #possible to make this into  a get_first_name or get_last_name
        """Used to get a users short name"""

        return self.first_name

    def __str__(self):
        """Django uses this when it needs to convert the object to a string"""

        return self.email

class ProfileFeedItem(models.Model):
    """Profile status update"""

    # use foreign key to get to another model
    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)#if user profile is deleted, then all profile feed will also be deleted
    # create status
    status_text = models.CharField(max_length=255)
    # store date status is created
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string."""

        return self.status_text

class EventProfile(models.Model):
    """Represent a "event profile" inside our system"""

    title = models.CharField(max_length=255, null=False, blank=False ) #unique means one and only one
    location = models.CharField(max_length=255, null=False, blank=False )
    about = models.TextField(max_length=5000, null=False, blank=False)
    #user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE) #needed for substition later
    date_time = models.DateTimeField() #needed for substition later
    user_profile = models.ForeignKey('UserProfile',on_delete=models.CASCADE)


    #object manager to manage user profile *needed for substition later
#    objects = EventProfileManager()

    #will be used later on with the django admin
    def __str__(self):                        #possible to make this into a get_first_name and get_last_name

        return self.title

'''class EventProfileManager(models.Model):
    """Helps Django work with our custom user model"""

    def create_event(self, title, location, about, organiser_id,date_time):
            """Creates a new event profile object"""

            #when no email or invalid
            if not title:
                raise ValueError('Events must have a title.')

            #normalize converts all into lowercase
            event = self.model(title=title, location=location, about=about, organiser_id=organiser_id , date_time=date_time)

            event.organiser_id=

            return user


'''
