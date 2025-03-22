# Secure Coding Review Report  
## Vulnerabilities Fixed  
1. **SQL Injection**: Parameterized queries with SQLAlchemy.  
2. **Debug Mode**: Disabled in production.  
3. **Password Hashing**: Used bcrypt.  

## Bandit Report  
```bash
$ bandit login.py  
[main]  INFO    No issues identified.