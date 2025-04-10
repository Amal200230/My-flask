# Flask + SQL Server (SSMS) + API Integration

Author: Amal Prakash

This project demonstrates how to create a Flask application that connects to SQL Server (SSMS) and exposes APIs using Flask and SQLAlchemy.


****** Steps Followed******

1. Imported Flask and SQLAlchemy libraries.
2. Connected SQL Server with the Flask application using the appropriate connection string.
3. Initialized the database using `db.create_all()`.
4. Created API endpoints using HTTP methods:
   - `GET`
   - `POST`
   - `PUT`
   - `DELETE`
5. Ran the Flask app using `app.run()`.
6. Copied the server address from the terminal and tested endpoints in Postman.
7. Performed API operations (GET, POST, PUT, DELETE).
8. Verified if entries were updated in SQL Server (SSMS).
9. Performed direct SQL operations using SSMS as well.



**** Notes

- SQLAlchemy ORM is used to manage table creation and database operations via Python.
- Postman is used for testing APIs during development.










