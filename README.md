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
