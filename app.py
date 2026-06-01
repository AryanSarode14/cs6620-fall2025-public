from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <html>
    <head>
        <title>Automated EC2 Deployment</title>
    </head>
    <body>
        <h1>Hello from Automated CI/CD Pipeline!</h1>

        <p><strong>Version:</strong> 2.0 - Automated Deployment</p>

        <p><strong>Deployed via:</strong> GitHub Actions + AWS SSM</p>

        <p><strong>Build Date:</strong> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>

        <p><strong>Assignment:</strong> Automated EC2 Deployment</p>
    </body>
    </html>
    """
