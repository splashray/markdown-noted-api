# Markdown-Noted-App

Welcome to the Markdown-Noted App! This Flask-based application allows users to create, manage, and retrieve their notes using Markdown formatting. The app is built with a RESTful API and secured with JWT authentication.

## Features

- **User Authentication:**

  - Register new users
  - Login to access notes

- **Note Management:**

  - Create new notes
  - Retrieve all notes for a user
  - Retrieve individual notes by ID

- **Markdown Support:**
  - Notes can be written in Markdown and are rendered to HTML

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Flask
- Flask-JWT-Extended
- Markdown2
- SQLAlchemy

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/splashray/markdown-noted-api.git
   cd markdown-noted-api
   ```

   Create a Virtual Environment and Install Dependencies:

   ````bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

   Set Up Environment Variables:

   Create a .env file and configure the necessary environment variables like SECRET_KEY, JWT_SECRET_KEY, DATABASE_URI, etc.

   Run Database Migrations:

   ```bash
   flask db upgrade
   ````

   Run the Application:

   ```bash
   f   lask run
   ```

Test the Endpoints:

Use Postman or a similar tool to test the API endpoints for creating, retrieving, updating, and deleting notes.

2. **Error Handling :**

400 Bad Request: Missing required fields or invalid input.
404 Not Found: Requested resource does not exist.
500 Internal Server Error: Unexpected server error.
Development

3. **Contributing :**

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

4. **License :**

This project is licensed under the MIT License. See the LICENSE file for details.

5. **Contact :**
   For questions or issues, please contact splashraycreations@gmail.com.

### Notes:

- **Project URL:** Replace `https://github.com/splashray/markdown-noted-api.git` with the actual repository URL.
- **Email Contact:** `[splashraycreations@gmail.com](mailto:splashraycreations@gmail.com)`.
- **Database Configuration:** Ensure you configure the database for SQLite

This `README.md` provides a comprehensive overview of the project, including setup instructions, and contribution guidelines.
