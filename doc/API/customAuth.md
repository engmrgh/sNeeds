
## Authentication
> auth/jwt/token/ [POST]

body:
```
{
    "email":"b2@g.com",
    "password":"passwordhere"
}
```
If authenticated:
```
HTTP 400 Bad Request
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "detail": "You are already authenticated"
}
```
If credentials are wrong:
```
HTTP 401 Unauthorized
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "detail": "Invalid email/password"
}
```

If everything is right:
```
HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "expires": "2019-07-22T08:51:47.324472Z",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImIyQGcuY29tIiwib3JpZ19pYXQiOjE1NjMxODA5MDcsInVzZXJfaWQiOjE0LCJ1c2VybmFtZSI6ImIyQGcuY29tIiwiZXhwIjoxNTYzNzg1NzA3fQ.R0e89tIOLtOUKP_1D6JsM0jNhAlTR5wMStxRcrJuITQ"
}
```
---
> auth/jwt/token/refresh/ [POST]

body:
```json
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImIyQGcuY29tIiwib3JpZ19pYXQiOjE1NjMxODA5ODYsInVzZXJfaWQiOjE0LCJ1c2VybmFtZSI6ImIyQGcuY29tIiwiZXhwIjoxNTYzNzg1Nzg2fQ.cx2HAQh26Sj6V4xFBZZVqrALZmhSRY2TGRcxfit-S7o"
}
```
If failed: 
```
HTTP 400 Bad Request
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "non_field_errors": [
        "Error decoding signature."
    ]
}
```

If succeeded:
```
HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "expires": "2019-07-22T08:53:26.591912Z",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImIyQGcuY29tIiwib3JpZ19pYXQiOjE1NjMxODA5ODYsInVzZXJfaWQiOjE0LCJ1c2VybmFtZSI6ImIyQGcuY29tIiwiZXhwIjoxNTYzNzg1ODA2fQ.8s1Ch93w9CViZAW72LbG6m1RHINtTdJx5dbxI_hBlFg"
}
```
> auth/accounts/ [POST]  (used for registeration)

body:
```json
{
    "email": "bartararya111@gmail.com",
    "first_name": "Arya",
    "last_name": "Khaligh",
    "phone_number":"09011353909",
    "address":"Ardabil",
    "password":"temppass",
    "password2":"temppass"
}
```

Response: 
``` 
HTTP 201 Created
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "email": "bartararya111@gmail.com",
    "first_name": "Arya",
    "last_name": "Khaligh",
    "phone_number": "09011353909",
    "address": "Ardabil",
    "token_response": {
        "expires": "2019-07-22T08:58:16.758102Z",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImJhcnRhcmFyeWExMTFAZ21haWwuY29tIiwib3JpZ19pYXQiOjE1NjMxODEyOTYsInVzZXJfaWQiOjE2LCJ1c2VybmFtZSI6ImJhcnRhcmFyeWExMTFAZ21haWwuY29tIiwiZXhwIjoxNTYzNzg2MDk2fQ.NcS4eG3HATZikUekB60vQRkZNkQ7wxoX6feLUYfIp4A"
    }
}
```
---
> auth/accounts/{ID}/ [GET]  
> auth/accounts/14/ [GET]

If you are not logged in as this user:
```
HTTP 403 Forbidden
Allow: GET, PUT, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "detail": "This user is not the user that is trying to access."
}
```

If you are:
```
HTTP 200 OK
Allow: GET, PUT, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "email": "b2@g.com",
    "first_name": "Arya",
    "last_name": "Khaligh",
    "phone_number": "09011353909",
    "address": "Ardabil"
}
```
---
> auth/accounts/{ID}/ [PUT]  
> auth/accounts/14/ [PUT]

body:
```
{
    "first_name": "Arya",
    "last_name": "Khaligh",
    "phone_number":"09011353909",
    "address":"Ardabil",
    "password":"temptest",
    "password2":"temptest"
}
```
You can use either of these fields e.g:
```json
{
    "phone_number": "99999999999"
}
```
OR
```json
{
    "first_name": "AryaHadi",
    "phone_number": "99999999999"
}
```


- Note: If you change password you will be logged out and get this message:
``` 
HTTP 401 Unauthorized
Allow: GET, PUT, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
WWW-Authenticate: JWT realm="api"

{
    "detail": "Authentication credentials were not provided."
}
```
