ure! Below is a detailed `README.md` file for your project:

```markdown
# AirBnB Clone - Application Server Setup

## Introduction

This project is part of the AirBnB clone series, where we set up a development environment to serve our web application using Flask and integrate it with an application server. This setup is essential for testing and debugging before deploying to a production environment.

## Prerequisites

1. **SSH Key-Based Authentication**: Ensure that SSH key-based authentication is set up for the `web-01` server.
2. **Install `net-tools` Package**: This package provides various network-related tools, such as `ifconfig`.
   ```bash
   sudo apt update
   sudo apt install -y net-tools
   ```

## Setup Steps

### 1. Clone the Repository

Clone the `AirBnB_clone_v2` repository on your `web-01` server:
```bash
git clone https://github.com/your-username/AirBnB_clone_v2.git
cd AirBnB_clone_v2
```

### 2. Modify the Flask Application

Update the `web_flask/0-hello_route.py` file to serve its content from the route `/airbnb-onepage/` on port 5000. Ensure the Flask application object is named `app`.

```python
#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

@app.route('/airbnb-onepage/')
def hello_hbnb():
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### 3. Run the Flask Application

To start your Flask application, run the following command:
```bash
python3 -m web_flask.0-hello_route
```

Expected output:
```
 * Serving Flask app "0-hello_route" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

### 4. Test the Application

Open another terminal session, log into your `web-01` server, and use `curl` to test the Flask application:

```bash
curl 127.0.0.1:5000/airbnb-onepage/
```

Expected response:
```
Hello HBNB!
```

## Additional Information

- **Flask**: A lightweight WSGI web application framework in Python.
- **Gunicorn**: A Python WSGI HTTP server for UNIX. It's a pre-fork worker model, which is suitable for production environments.
- **Nginx**: A high-performance HTTP server and reverse proxy. It can be used to serve static files, reverse proxy HTTP requests to Gunicorn, and handle load balancing.

## Conclusion

By following these steps, you have set up a development environment for your AirBnB clone project on `web-01` using Flask. This environment is crucial for testing and debugging your application before moving to production.
