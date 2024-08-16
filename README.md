live link = https://learn-match-api.onrender.com
# Learn Match

Learn Match is a tuition finding platform that connects tutors with tutoring opportunities. The primary purpose of this application is to streamline the process of finding and applying for tutoring jobs, making it easier for educators to secure employment.

## Features

- User registration and authentication
- Tuition job posting
- Tuition job search and filtering
- Application submission for tutors
- Dashboard with statistics

## Technologies Used

- Django Rest Framework
- SQLite
- Render (for deployment)
- Git & GitHub (version control)
- Django ORM

## Prerequisites

- Python 3.x
- pip

## Installation

1. Clone the repository:
git clone https://github.com/ashiqur-shohan/Learn-Match---API.git
cd learn-match
2. Install the required dependencies:
pip install -r requirements.txt
3. Run migrations:
python manage.py migrate
4. Start the development server:
python manage.py runserver

The application should now be running at `http://localhost:8000`.

## API Endpoints

### Authentication
- `POST /api/user/register/`: Register a new user
- `POST /api/user/login/`: Log in a user
- `POST /api/user/logout/`: Log out the current user
- `PUT /api/user/change-password/`: Change user password

### Tuition
- `GET /api/tuitions/`: List all tuition opportunities
- `GET /api/tuitions/{id}/`: Retrieve details of a specific tuition
- `POST /api/tuitions/`: Create a new tuition listing
- `PUT /api/tuitions/{id}/`: Update a tuition listing
- `DELETE /api/tuitions/{id}/`: Delete a tuition listing
- `GET /api/tuitions/search/?query=`: Search tuitions by keyword

### Applications
- `GET /api/applications/`: List all applications (admin only)
- `GET /api/applications/teacher/{teacher_id}/`: List applications for a specific teacher
- `POST /api/applications/`: Submit a new application
- `DELETE /api/applications/{id}/`: Delete an application

### Dashboard
- `GET /api/dashboard/stats/`: Retrieve dashboard statistics (total teachers, applications, live tuitions)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

For any inquiries, please contact:
Ashiqur Rahman - ashiqur.shohan@gmail.com

## License

This project is open source and available under the [MIT License](LICENSE).