# Movie-Ticket-Booking-using-Django

Sure! Here's a detailed README file for a movie ticket booking system using Django:

---

# Movie Ticket Booking System

This project is a web-based application for booking movie tickets. It is built using Django, a high-level Python web framework that encourages rapid development and clean, pragmatic design.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Database Setup](#database-setup)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [License](#license)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.x.
- You have installed Django (version 3.x or higher).

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/movie-ticket-booking-system.git
   cd movie-ticket-booking-system
   ```

2. **Create a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Django Project:**

   If you haven't already created a Django project, you can do so by running:

   ```bash
   django-admin startproject booking
   cd booking
   django-admin startapp movie
   ```

## Project Structure

The project's directory structure should look like this:

```
movie-ticket-booking-system/
├── booking/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
├── movie/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   ├── movie/
│   │   │   ├── base_generic.html
│   │   │   ├── movie_list.html
│   │   │   ├── movie_detail.html
│   │   │   ├── booking_form.html
│   │   │   ├── booking_confirmation.html
│   ├── static/
│   │   ├── css/
│   │   │   ├── styles.css
│   │   ├── js/
│   │       ├── scripts.js
├── manage.py
├── requirements.txt
```

## Database Setup

1. **Run Migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

2. **Create a Superuser:**

   ```bash
   python manage.py createsuperuser
   ```

3. **Load Initial Data:**

   If you have initial data to load, you can do so by creating fixtures and using:

   ```bash
   python manage.py loaddata initial_data.json
   ```

## Running the Application

1. **Start the Development Server:**

   ```bash
   python manage.py runserver
   ```

2. **Access the Application:**

   Open your web browser and go to `http://127.0.0.1:8000/` to see the application running.

## Usage

1. **Home Page:**

   - The home page lists all available movies.
   - Users can click on a movie to see its details.

2. **Movie Details:**

   - The movie detail page shows information about the movie and available showtimes.
   - Users can book tickets for a selected showtime.

3. **Booking Tickets:**

   - Fill out the booking form with required details (e.g., name, email, number of tickets).
   - Submit the form to book tickets.
   - A confirmation page will display the booking details.

4. **Admin Interface:**

   - Admins can log in to the admin interface to manage movies, showtimes, and bookings.
   - Access the admin interface at `http://127.0.0.1:8000/admin/`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

