from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>CSI2113 DevOps Practical</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #1e1e2f;
                color: white;
                text-align: center;
                padding-top: 100px;
            }
            h1 {
                color: #4CAF50;
            }
            p {
                font-size: 18px;
            }
        </style>
    </head>
    <body>
        <h1>Hello from CSI2113 DevOps Practical!</h1>
        <p>Student: Sasindu Nimsara - 8003369</p>
        <p>This app was deployed automatically using Docker and GitHub Actions CI/CD Pipeline.</p>
    </body>
    </html>
    """, 200

@app.route('/health')
def health():
    return jsonify(status="healthy"), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)