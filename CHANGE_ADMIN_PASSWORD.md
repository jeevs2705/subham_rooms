# How to Change Admin Login Credentials

## Current Credentials:
- **Username**: vignesh
- **Password**: vignesh

## To Change the Credentials:

1. Open the file: `app.py`

2. Find these lines near the top (around line 18-19):
   ```python
   ADMIN_USERNAME = "vignesh"
   ADMIN_PASSWORD = "vignesh"
   ```

3. Change them to your desired username and password:
   ```python
   ADMIN_USERNAME = "your_new_username"
   ADMIN_PASSWORD = "your_new_password"
   ```

4. Save the file

5. Restart Flask:
   - Press `Ctrl + C` to stop
   - Run `python app.py` to start again

## Example:
If you want username "admin" and password "secure123":
```python
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "secure123"
```

## Security Tips:
- Use a strong password (mix of letters, numbers, symbols)
- Don't share your credentials
- Change password regularly
- Don't use common passwords like "password123"

## Admin Access:
- Login URL: http://127.0.0.1:5000/vedhyogi/login
- After login, you'll be redirected to the admin dashboard
- Click "Logout" button to log out
