from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>My Portfolio</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <style>
        * {
            box-sizing: border-box;
            font-family: 'Segoe UI', sans-serif;
        }

        body {
            margin: 0;
            min-height: 100vh;
            background: linear-gradient(-45deg, #1d2671, #c33764, #1d2671);
            background-size: 400% 400%;
            animation: gradient 10s ease infinite;
            color: #fff;
        }

        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        header {
            text-align: center;
            padding: 60px 20px;
        }

        header h1 {
            font-size: 3rem;
            margin-bottom: 10px;
        }

        header p {
            font-size: 1.2rem;
            opacity: 0.9;
        }

        section {
            max-width: 900px;
            margin: auto;
            padding: 20px;
        }

        .card {
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 25px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.3);
            transition: transform 0.3s;
        }

        .card:hover {
            transform: translateY(-5px);
        }

        h2 {
            color: #ffdd57;
            margin-bottom: 15px;
        }

        ul {
            padding-left: 20px;
        }

        li {
            margin-bottom: 8px;
        }

        input, textarea {
            width: 100%;
            padding: 12px;
            margin: 10px 0;
            border-radius: 8px;
            border: none;
            outline: none;
        }

        textarea {
            resize: none;
            height: 100px;
        }

        button {
            width: 100%;
            padding: 12px;
            background: #ffdd57;
            color: #000;
            border: none;
            border-radius: 8px;
            font-size: 1rem;
            font-weight: bold;
            cursor: pointer;
            transition: background 0.3s;
        }

        button:hover {
            background: #ffc107;
        }

        .success {
            color: #90ff90;
            font-weight: bold;
            margin-top: 10px;
            text-align: center;
        }

        footer {
            text-align: center;
            padding: 20px;
            opacity: 0.8;
        }

        @media (max-width: 600px) {
            header h1 {
                font-size: 2.2rem;
            }
        }
    </style>
</head>

<body>

<header>
    <h1>{{ name }}</h1>
    <p>{{ role }}</p>
</header>

<section>

    <div class="card">
        <h2>👨‍💻 About Me</h2>
        <p>{{ about }}</p>
    </div>

    <div class="card">
        <h2>🛠 Skills</h2>
        <ul>
            {% for skill in skills %}
            <li>{{ skill }}</li>
            {% endfor %}
        </ul>
    </div>

    <div class="card">
        <h2>📩 Contact Me</h2>
        <form method="POST">
            <input type="text" name="name" placeholder="Your Name" required>
            <input type="email" name="email" placeholder="Your Email" required>
            <textarea name="message" placeholder="Your Message" required></textarea>
            <button type="submit">Send Message</button>
        </form>

        {% if success %}
        <div class="success">✔ Message sent successfully!</div>
        {% endif %}
    </div>

</section>

<footer>
    © 2026 | Built with Flask 💙
</footer>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    success = False

    if request.method == "POST":
        print("📩 New Message")
        print("Name:", request.form["name"])
        print("Email:", request.form["email"])
        print("Message:", request.form["message"])
        print("-" * 40)
        success = True

    return render_template_string(
        HTML_PAGE,
        name="Your Name",
        role="Python Developer | Flask Intern",
        about="I build clean, user-friendly web applications using Python and Flask. I enjoy turning ideas into real-world projects.",
        skills=["Python", "Flask", "HTML", "CSS", "GitHub", "APIs"],
        success=success
    )

if __name__ == "__main__":
    app.run(debug=True)