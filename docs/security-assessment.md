# BlackVault Security Assessment

## 1. Project Overview

BlackVault is a Flask-based corporate document portal
developed as a local web application security lab.

## 2. Scope

Target: http://127.0.0.1:5000

Endpoints:
- GET /
- GET /search
- GET /health
- GET /document/<doc_id>

Testing was performed against the local lab application.

## 3. Testing Methodology

The assessment included:
- Endpoint functionality testing
- Document authorization checks
- Search information-disclosure checks
- Invalid document ID handling
- Automated regression testing using pytest

## 4. Initial Test Results

Eight automated tests passed during the final regression
test run.

The tests covered:

- Health check
- Public document access
- Internal document access denial
- Nonexistent document handling
- Public-only document search
- Internal audit exclusion from search
- Security headers on the main page
- Security headers on the health endpoint

See `docs/test-results.txt` for the recorded test output.

## 5. Observations

The tested application returned:
- HTTP 200 for public document access
- HTTP 403 for the internal audit document
- HTTP 404 for a nonexistent document
- Public documents only in the tested search results

These results apply only to the tested cases.
They do not establish that the entire application is secure.

## 6. Recommendations

- Implement authentication and authorization.
- Enforce document ownership on every protected endpoint.
- Validate and normalize user input.
- Avoid exposing confidential metadata in search results.
- Add automated authorization regression tests.
- Use HTTPS and secure session settings in production.
- Maintain application and dependency updates.

## 7. Limitations

This is an initial assessment of a small prototype.
Further testing is required before making claims about
overall security or production readiness.

## 8. Evidence

Automated test results are available in:
docs/test-results.txt


## 9. Regression Testing

Automated regression testing was performed using pytest.

### Results

- Total tests: 8
- Passed: 8
- Failed: 0

### Security Controls Verified

- Public document access
- Restricted document access denial
- Nonexistent document handling
- Public-only document search
- Prevention of internal audit document exposure
- Security headers on the main page
- Security headers on the health endpoint

### Conclusion

All eight automated tests passed in the local test
environment. These results validate the tested behaviors
but do not establish that the application is free from
other security vulnerabilities or ready for production.
