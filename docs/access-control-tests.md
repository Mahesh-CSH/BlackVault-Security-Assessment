# BlackVault — Access Control Testing

## 1. Assessment Scope

Application: BlackVault Document Management Portal
Target: http://127.0.0.1:5000
Environment: Local Kali Linux lab
Testing Type: Web Application Security Assessment

## 2. Test Results

|        Test                |   Endpoint    | Expected Status | Observed Status |
|----------------------------|---------------|-----------------|-----------------|
| Public document access     | /document/1   | 200 OK          | 200 OK          |
| Restricted document access | /document/3   | 403 Forbidden   | 403 Forbidden   |
| Nonexistent document       | /document/888 | 404 Not Found   | 404 Not Found   |

## 3. Search Testing

### Test A: Search for audit

Endpoint: /search?q=audit

Observed Result:
No search results returned.

### Test B: Search for security

Endpoint: /search?q=security

Observed Result:
The public Security Policy document was returned.

## 4. Security Observations

- Public document access behaved as expected.
- Direct access to the restricted document was denied.
- Requests for nonexistent documents returned 404.
- Search results did not expose the internal audit document
  during the tested cases.

## 5. Limitations

These tests cover only the listed endpoints and inputs.
They do not establish that the entire application is secure.

Further testing is required for authentication, authorization,
input validation, injection vulnerabilities, and security headers.

## 6. Conclusion

The tested access-control cases produced the expected responses.
Additional security testing is required to assess the application's
overall security posture.
