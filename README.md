# QA Automation Demo Project

This project demonstrates my skills as a Junior Software QA Engineer. It includes:
- A simple web application for testing.
- Manual test cases.
- Automated Selenium tests.
- API tests using Postman.
- A CI/CD pipeline using GitHub Actions.

## How to Run
1. Clone the repository.
2. Open the `app/` folder and run a local server (e.g., `python -m http.server 8000`).
3. Run the Selenium tests: `python tests/selenium/test_login.py`.
4. Import the Postman collection (`tests/api/test_api.postman_collection.json`) to test the API.

## CI/CD Pipeline
The GitHub Actions workflow runs the Selenium tests on every push or pull request.