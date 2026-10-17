# BlackVault – Web Application Security Assessment Lab

A Flask-based corporate document management portal built for
hands-on web application security testing, access control
validation, and automated security regression testing.

## Project Overview

BlackVault is a local security assessment lab designed to evaluate
document access controls, search functionality, HTTP security
headers, and error handling.

## Key Features

- Document search and retrieval
- Public and restricted document access controls
- HTTP security header verification
- Health-check endpoint testing
- Automated security regression testing with Pytest
- Security assessment documentation

## Technology Stack

- Python 3
- Flask
- Pytest
- Kali Linux
- Git and GitHub
- cURL

## Security Testing

The assessment covers the following areas:

| Test Area | Validation |
|---|---|
| Health endpoint | Endpoint availability |
| Public documents | Expected access allowed |
| Restricted documents | Unauthorized access denied |
| Invalid document IDs | Appropriate error handling |
| Document search | Public documents returned |
| Sensitive document exposure | Internal audit document excluded |
| HTTP security headers | Headers verified on main page |
| Health endpoint headers | Headers verified |

## Test Results

Latest local regression test results:

- Total tests: 8
- Passed: 8
- Failed: 0

Run the tests locally:

```bash
python3 -m pytest -v
```

## Run Locally
Clone the repository:
```
git clone https://github.com/Mahesh-CSH/BlackVault-Security-Assessment.git
```
```
cd BlackVault-Security-Assessment
```
Install dependencies:
```text
python3 -m pip install -r requirements.txt
```
Start the application:
```
python3 app.py
```
Open the application:
```text
http://127.0.0.1:5000/
```
Health endpoint:
```text
http://127.0.0.1:5000/health
```
## Project Documentation

- docs/security-assessment.md – Assessment scope, observations,
  recommendations, and test results.
- docs/access-control-tests.md – Access control test cases.
- docs/test-results.txt – Automated test evidence.

## Security Recommendations

- Implement authentication and authorization.
- Enforce document ownership on protected endpoints.
- Validate and normalize user input.
- Prevent confidential metadata exposure.
- Maintain secure session settings.
- Use HTTPS in production.
- Keep application dependencies updated.

## Scope and Limitations

This project is a local web application security assessment lab.
The results apply only to the tested scenarios and do not establish
that the application is free from all security vulnerabilities
or suitable for production deployment.

All testing should be performed in authorized environments.

### Author
Mahesh
