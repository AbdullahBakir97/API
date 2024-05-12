# Django Project

This project is a Django application that includes authentication functionalities such as signup, login, logout, password change, password reset, and related CRUD operations for teams, players, matches, fantasy teams, contests, and contest entries. It also includes serializers for API endpoints and filters for querying data.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python (3.x recommended)
- pip (Python package installer)

### Installing


1. **Clone the Repository**: Start by cloning the project repository:
   ```
   git clone https://github.com/AbdullahBakir97/API.git
   ```

2. **Navigate to the Project Directory**: Move into the project directory:
   ```
   cd API
   ```

3. **Create and Activate a Virtual Environment**: Set up a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. **Install Required Dependencies**: Install the necessary dependencies for the project:
   ```
   pip install -r requirements.txt
   ```

5. **Apply Database Migrations**: Apply database migrations to set up the database:
   ```
   python manage.py migrate
   ```

6. **Create a Superuser Account**: Create a superuser account for administrative access:
   ```
   python manage.py createsuperuser
   ```

7. **Start the Development Server**: Launch the development server:
   ```
   python manage.py runserver
   ```

8. **Access the Admin Panel**: Begin configuring your online store by accessing the admin panel at [http://localhost:8000/admin/](http://localhost:8000/admin/).


# API Endpoints

The following API endpoints are available:

- **Swagger**: /swagger/
- **Signup**: /accounts/signup/ (POST)
- **Login**: /accounts/login/ (POST)
- **Logout**: /accounts/logout/ (POST)
- **Change Password**: /accounts/change-password/ (POST)
- **Password Reset**: /accounts/reset-password/ (POST)
- **Password Reset Confirm**: /accounts/reset-password/confirm/ (POST)
- **Teams List/Create**: /teams/ (GET, POST)
- **Team Detail/Update/Delete**: /teams/<id>/ (GET, PUT, DELETE)
- **Players List/Create**: /players/ (GET, POST)
- **Player Detail/Update/Delete**: /players/<id>/ (GET, PUT, DELETE)
- **Matches List/Create**: /matches/ (GET, POST)
- **Match Detail/Update/Delete**: /matches/<id>/ (GET, PUT, DELETE)
- **Fantasy Teams List/Create**: /fantasy-teams/ (GET, POST)
- **Fantasy Team Detail/Update/Delete**: /fantasy-teams/<id>/ (GET, PUT, DELETE)
- **Contests List/Create**: /contests/ (GET, POST)
- **Contest Detail/Update/Delete**: /contests/<id>/ (GET, PUT, DELETE)
- **Contest Entries List/Create**: /contest-entries/ (GET, POST)
- **Contest Entry Detail/Update/Delete**: /contest-entries/<id>/ (GET, PUT, DELETE)

## Authors

- [Abdullah Bakir](https://github.com/AbdullahBakir97)

## License

This project is licensed under the [MIT License](LICENSE).  
