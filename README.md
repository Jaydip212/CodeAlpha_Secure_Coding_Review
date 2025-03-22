# Secure Coding Review Report  

## Vulnerabilities Fixed  
1. **SQL Injection**: Parameterized queries with SQLAlchemy.  
2. **Debug Mode**: Disabled in production.  
3. **Password Hashing**: Used bcrypt.  

## How to Test the Application  

### Step 1: Run the Flask App  
```bash
$ python login.py
$ bandit login.py  
$ python init_db.py

Step 2: Test Login Endpoint
Valid Credentials:

curl -X POST http://localhost:5000/login -d "username=testuser&password=testpassword"
Output: Login Successful!

Invalid Credentials:

 curl -X POST http://localhost:5000/login -d "username=testuser&password=wrongpassword"
 Invalid Credentials!

 Bandit Security Report:

 $ bandit login.py  
[main]  INFO    No issues identified.
