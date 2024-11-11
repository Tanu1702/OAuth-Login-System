# OAuth Login System

## Project Overview
The OAuth Login System is a secure and efficient method for handling user authentication in web applications using OAuth 2.0. Built with Python and Flask, this project enables users to log in with existing credentials from providers like Google or Facebook, streamlining the login process and enhancing security.

## Features
- **OAuth 2.0 Protocol**: Secure user authentication with industry-standard protocol.
- **Session Management**: Stores access tokens securely within the session.
- **Profile Access**: Retrieves user profile information post-authentication.
- **CSRF Protection**: State parameter ensures secure redirect handling.

## Prerequisites
- **OS**: Kali Linux or compatible Linux OS
- **Python Version**: 3.x
- **Libraries**: Flask, Requests
- **Optional**: OpenSSL for self-signed certificates (if SSL testing is desired)

## Installation and Setup

1. **Install Required Packages**
   ```bash
   sudo apt update
   sudo apt install python3-pip
   pip3 install Flask requests
   
2. **Generate SSL Certificates**
```mkdir ~/certs && cd ~/certs
   openssl genrsa -out privatekey.pem 2048
   openssl req -new -key privatekey.pem -out csr.pem
   openssl x509 -req -days 365 -in csr.pem -signkey privatekey.pem -out certificate.pem

3. **Configure the Application Update app.py:**
```AUTH_SERVER: OAuth provider’s authorization server URL.
```CLIENT_ID and CLIENT_SECRET: OAuth credentials.
```REDIRECT_URI: Must match URI registered with OAuth provider.

4.**Run the Application**
```bash
   Copy code
   sudo python3 app.py

5.**Access the Application**
```Go to http://127.0.0.1:8000/login in a web browser to start the login process.
```Navigate to http://127.0.0.1:8000/profile after login to view user profile data.
