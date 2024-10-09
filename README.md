# Inventory Management System - Backend API

## Table of Contents

- [Project Overview](#project-overview)
- [Requirements](#requirements)
- [Installation](#installation)
  - [Clone the Repository](#clone-the-repository)
  - [Setting up the Virtual Environment](#setting-up-the-virtual-environment)
  - [Install Dependencies](#install-dependencies)
  - [Configure the Database](#configure-the-database)
  - [Apply Migrations](#apply-migrations)
  - [Setting up Redis](#setting-up-redis)
  - [Environment Variables](#environment-variables)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
  - [Authentication](#authentication)
  - [Inventory CRUD Operations](#inventory-crud-operations)
- [Caching with Redis](#caching-with-redis)
- [Logging](#logging)
- [Testing](#testing)
- [License](#license)


## Project Overview

This **Inventory Management System** is a backend API built using Django and Django Rest Framework (DRF). It supports secure CRUD operations on inventory items with JWT-based authentication. PostgreSQL is used for database management, and Redis is integrated to cache frequently accessed items to improve performance.

## Requirements

- **Python**
- **Django** 
- **Django Rest Framework** 
- **PostgreSQL** 
- **Redis** 
- **djangorestframework-simplejwt** for JWT Authentication

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/inventory-management-api.git
cd inventory-management-api

## Setting up the Virtual Environment
### Create a Python virtual environment to isolate the project dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

## Install Dependencies
### Install the required dependencies from requirements.txt:

```bash
pip install -r requirements.txt

## Configure the Database
### 1.Ensure PostgreSQL is installed and running.
### 2.Create a PostgreSQL database for the project:

```bash
CREATE DATABASE inventory_db;
CREATE USER inventory_user WITH PASSWORD 'password';
ALTER ROLE inventory_user SET client_encoding TO 'utf8';
ALTER ROLE inventory_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE inventory_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE inventory_db TO inventory_user;

### 3.Update settings.py with your PostgreSQL database configuration:
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'inventory_db',
        'USER': 'inventory_user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

## Apply Migrations
### After configuring the database, apply the database migrations:

```bash
python manage.py migrate

##vSetting up Redis
### Ensure Redis is installed and running on your machine. Update your settings.py to include the Redis configuration:

```bash
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

## Running the Application
### Start the development server with the following command:

```bash
python manage.py runserver

## API Endpoints
## Authentication
### JWT authentication is required to access any API endpoints. You can authenticate using the following endpoints:
  ### User Registration

  ### Method: POST
  ### URL: /auth/register/
  ### Request Body
  ```bash
  {
    "username": "your_username",
    "password": "your_password"
  }

 ### Login and Retrieve JWT Token

  ### Method: POST
  ### URL: /auth/login/
  ### Request Body
  ```bash
  {
    "username": "your_username",
    "password": "your_password"
  }

  ### Response:
  ```bash
  {
  "access": "jwt_access_token",
  "refresh": "jwt_refresh_token"
}

 ### Token Refresh
  ### Method: POST
  ### URL: /auth/login/
  ### Request Body
  ```bash
  {
  "refresh": "jwt_refresh_token"
  }

## Inventory CRUD Operations

  ### 1.Create Item
    ### Method: POST
    ### URL: /items/
    ### Request Body
    ```bash
    {
    "name": "item_name",
    "description": "item_description"
    }

   ### Response:
  ```bash
    {
    "id": 1,
    "name": "item_name",
    "description": "item_description"
  }


  ### 2.Read Item
    ### Method: GET
    ### URL: /items/{item_id}/

   ### Response:
  ```bash
      {
    "id": 1,
    "name": "item_name",
    "description": "item_description"
    }

  ### 3.Update Item
    ### Method: PUT
    ### URL: /items/{item_id}/

   ### Request Body:
  ```bash
    {
    "name": "updated_name",
    "description": "updated_description"
    }

  ### 4.Delete Item
    ### Method: DELETE
    ### URL: /items/{item_id}/

   ### Response:
  ```bash
   {
  "message": "Item deleted successfully"
  }


## Caching with Redis
### The Read Item endpoint is cached using Redis. When an item is accessed for the first time, it is stored in the Redis cache. Subsequent requests for the same item will be fetched from Redis to improve performance.

### To configure Redis caching, ensure that Redis is installed and running, and the CACHES setting in settings.py is properly configured.

## Testing
### Unit tests are implemented using Django’s built-in test framework. To run tests, use the following command:
```bash
python manage.py test










  




