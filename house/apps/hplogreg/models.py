from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
import re
from django.contrib import messages
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UserManager(models.Manager):
    def register(self, data):
        error = []
            #index 1 of the innerlist, retrieve in views side
        if len(data["name"]) < 3 or any(char.isdigit() for char in data["name"]):
            error.append('Name must be at least 2 characters and contain no numbers')
        if not EMAIL_REGEX.match(data['email']):
            error.append('Incorrect email')
        if len(data["password"]) < 8:
            error.append('Incorrect password length')

        user = self.filter(email = data['email']) #check if false

        if user:
            error.append('email taken')
        if data['password'] != data['password_confirm']:
            error.append('please match your passwords')
        if error:
            return (False, error)

        hashed = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
        user = self.create(name = data["name"],email = data["email"], password = hashed)
        return (True, user)

    def login(self, data):
        error = []
        user = self.filter(email=data['email'])
        if user:
            if bcrypt.hashpw(data['password'].encode('utf-8'), user[0].password.encode('utf-8')) == user[0].password:
                return (True, user[0])
        error.append("Invalid credentials, please try again")
        return (False, error)


class User(models.Model):
    name = models.CharField(max_length=45)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
