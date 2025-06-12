from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# Home page


@app.route('/')
def home():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Simple Flask App</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .container { max-width: 600px; margin: 0 auto; }
            h1 { color: #333; }
            .nav { margin: 20px 0; }
            .nav a { margin-right: 15px; text-decoration: none; color: #007bff; }
            .nav a:hover { text-decoration: underline; }
            .form-group { margin: 15px 0; }
            input, button { padding: 8px; margin: 5px; }
            button { background: #007bff; color: white; border: none; cursor: pointer; }
            button:hover { background: #0056b3; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to Flask!</h1>
            <div class="nav">
                <a href="/">Home</a>
                <a href="/about">About</a>
                <a href="/contact">Contact</a>
                <a href="/api/data">API Data</a>
            </div>
            <p>This is a simple Flask application with multiple routes.</p>
            <h3>Quick Form Test</h3>
            <form action="/submit" method="POST">
                <div class="form-group">
                    <input type="text" name="name" placeholder="Enter your name" required>
                </div>
                <div class="form-group">
                    <button type="submit">Submit</button>
                </div>
            </form>
        </div>
    </body>
    </html>
    ''')


@app.route('/about')
def about():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>About - Flask App</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .container { max-width: 600px; margin: 0 auto; }
            h1 { color: #333; }
            .nav { margin: 20px 0; }
            .nav a { margin-right: 15px; text-decoration: none; color: #007bff; }
            .nav a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>About This App</h1>
            <div class="nav">
                <a href="/">Home</a>
                <a href="/about">About</a>
                <a href="/contact">Contact</a>
                <a href="/api/data">API Data</a>
            </div>
            <p>This is a simple Flask application demonstrating:</p>
            <ul>
                <li>Multiple routes</li>
                <li>HTML templates</li>
                <li>Form handling</li>
                <li>JSON API endpoints</li>
            </ul>
        </div>
    </body>
    </html>
    ''')


@app.route('/contact')
def contact():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Contact - Flask App</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .container { max-width: 600px; margin: 0 auto; }
            h1 { color: #333; }
            .nav { margin: 20px 0; }
            .nav a { margin-right: 15px; text-decoration: none; color: #007bff; }
            .nav a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Contact Us</h1>
            <div class="nav">
                <a href="/">Home</a>
                <a href="/about">About</a>
                <a href="/contact">Contact</a>
                <a href="/api/data">API Data</a>
            </div>
            <p>Get in touch with us!</p>
            <p>Email: contact@example.com</p>
            <p>Phone: (555) 123-4567</p>
        </div>
    </body>
    </html>
    ''')


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name', 'Anonymous')
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Submitted - Flask App</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .container { max-width: 600px; margin: 0 auto; }
            h1 { color: #333; }
            .nav { margin: 20px 0; }
            .nav a { margin-right: 15px; text-decoration: none; color: #007bff; }
            .nav a:hover { text-decoration: underline; }
            .success { background: #d4edda; padding: 15px; border-radius: 5px; color: #155724; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Form Submitted!</h1>
            <div class="nav">
                <a href="/">Home</a>
                <a href="/about">About</a>
                <a href="/contact">Contact</a>
                <a href="/api/data">API Data</a>
            </div>
            <div class="success">
                <p>Thank you, {{ name }}! Your form has been submitted successfully.</p>
            </div>
        </div>
    </body>
    </html>
    ''', name=name)


@app.route('/api/data')
def api_data():
    return jsonify({
        'message': 'Hello from Flask API!',
        'status': 'success',
        'data': {
            'users': ['Alice', 'Bob', 'Charlie'],
            'total_users': 3,
            'app_version': '1.0.0'
        }
    })


@app.route('/api/users/<int:user_id>')
def get_user(user_id):
    users = {
        1: {'name': 'Alice', 'email': 'alice@example.com'},
        2: {'name': 'Bob', 'email': 'bob@example.com'},
        3: {'name': 'Charlie', 'email': 'charlie@example.com'}
    }

    user = users.get(user_id)
    if user:
        return jsonify({'user': user})
    else:
        return jsonify({'error': 'User not found'}), 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
