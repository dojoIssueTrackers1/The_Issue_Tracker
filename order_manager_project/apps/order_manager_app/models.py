from __future__ import unicode_literals
from django.db import models

import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        # First Name Validation
        if len(postData['first_name']) < 1:
            errors['first_name'] = "First Name is a Required Field!"
        elif len(postData['first_name']) < 2:
            errors['first_name'] = "First name must have 2 or more characters"
        elif postData['first_name'].isalpha() == False:
            errors['first_name'] = "First name must only contain letters!"

        # Last Name Validation
        if len(postData['last_name']) < 1:
            errors['last_name'] = 'Last name is a Required Field!'
        elif len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must have 2 or more characters"
        elif postData['last_name'].isalpha() == False:
            errors['last_name'] = "Last name must only contain letters!"

        # Email Validation
        if len(postData['email']) < 1:
            errors['email'] = "Email is a Required Field!"
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid Email!"
        existing_users = User.objects.filter(email=postData['email'])
        if len(existing_users) > 0:
            errors['email'] = "That email already exists!"

        # Password Validation
        if len(postData['pw']) < 1:
            errors['pw'] = "Password is a Required Field"
        elif len(postData['pw']) < 8:
            errors['pw'] = "The password must contain 8 characters or more!"
        else:
            if postData['cpw'] != postData['cpw']:
                errors['cw'] = "The passwords do not match!"

        return errors

    def login_validator(self, postData):
        errors = {}
        # Email Validation
        if len(postData['LEmail']) < 1:
            errors['email'] = "Email is a Required Field!"
        elif not EMAIL_REGEX.match(postData['LEmail']):
            errors['email'] = "Invalid Email!"

        # Password Validation
        if len(postData['Lpw']) < 1:
            errors['pw'] = "Password is a Required Field"
        elif len(postData['Lpw']) < 8:
            errors['pw'] = "The password must contain 8 characters or more!"

        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pw = models.CharField(max_length=255)
    objects = UserManager()


################### Second Table ##############################

class IssueManager(models.Manager):
    def job_validator(self, postData):
        errors={}
        if len(postData['jobTitle']) < 1:
            errors['title'] = "The Title field is a required field!"
        if len(postData['jobTitle']) < 3:
            errors['title'] = "The title must be 3 or more characters"

        if len(postData['description']) < 1:
            errors['desc'] = "The description field is required!"
        if len(postData['description']) < 10:
            errors['desc'] = "The description field must contain at least 10 characters!"

        if len(postData['location']) <1:
            errors['location'] = "The Location field is a required field and must not be blank!"

        return errors


class Issue(models.Model):
    order_number = models.IntegerField()
    customer_id = models.IntegerField()
    issue_type = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    priority = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    creator = models.ForeignKey(User, related_name="issued_by")
    objects = IssueManager()