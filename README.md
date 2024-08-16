# Learn Match

Learn Match is a tuition finding platform that connects tutors with tutoring opportunities. The primary purpose of this application is to streamline the process of finding and applying for tutoring jobs, making it easier for educators to secure employment.

## Table of Contents

- [Features](#features)
- [Project Links](#project-links)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Installation and Run the Project](#installation-and-run-the-project)
- [API Endpoints](#api-endpoints)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [Contact](#contact)
- [License](#license)

## Features

- User registration and authentication
- Tuition job posting
- Tuition job search and filtering
- Application submission for tutors
- Dashboard with statistics

## Project Links

### Live Link
- Live API: [https://learn-match-api.onrender.com](https://learn-match-api.onrender.com)

### Frontend Part
- Source Code: [https://github.com/ashiqur-shohan/Learn-Match](https://github.com/ashiqur-shohan/Learn-Match)
- Live link: [https://learn-match.netlify.app/](https://learn-match.netlify.app/)

## Technologies Used

- Django Rest Framework
- SQLite
- Render (for deployment)
- Git & GitHub (version control)
- Django ORM

## Prerequisites

- Python 3.x
- pip

## Installation and Run the Project

1. Clone the repository:
```bash
git clone https://github.com/ashiqur-shohan/Learn-Match---API.git
```
2. Navigate to the project directory:
> **Important:** This step ensures all following commands are executed in the correct project directory.
```bash
cd learn-match
```
3. Install the required dependencies:
```bash
pip install -r requirements.txt
```
4. Run migrations:
```bash
python manage.py migrate
```
5. Start the development server:
```bash
python manage.py runserver
```

The application should now be running at 
```bash
http://localhost:8000
```

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


## Deployment

This project is deployed using [Render](https://render.com). To deploy your own instance of Learn Match, follow these steps:

1. **Prerequisites**
   - A Render account
   - Your project pushed to a Git repository (GitHub, GitLab, or Bitbucket)

2. **Setup on Render**
   - Log in to your Render dashboard
   - Click on "New +" and select "Web Service"
   - Connect your Git repository
   - Select the branch you want to deploy

3. **Configuration**
   - Set the Environment to "Python"
   - Set the Build Command to `pip install -r requirements.txt`
   - Set the Start Command to `python manage.py runserver 0.0.0.0:80`

4. **Environment Variables**
   - Add the following environment variables:
     - `DEBUG`: Set to `False` for production
     - `SECRET_KEY`: Your Django secret key
     - `ALLOWED_HOSTS`: Add your Render URL and any custom domains

5. **Database Setup**
   - If using Render's PostgreSQL, add the `DATABASE_URL` to your environment variables
   - Run migrations manually or add a build script

6. **Static Files**
   - Set up static file serving through Render or a CDN

7. **Custom Domain (Optional)**
   - Add your custom domain in the Render dashboard
   - Update your DNS settings as per Render's instructions

For more detailed instructions, refer to Render's [Python deployment guide](https://render.com/docs/deploy-python).

**Note:** Make sure to update your `settings.py` file to use environment variables for sensitive information and to accommodate the production environment.


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

For any inquiries, please contact:
- E-mail - ashiqur.shohan@gmail.com
- What's app - +8801633640145

## License

This project is open source and available under the [MIT License](License.md).