# Flask URL Redirect to New Domain 🌐

This Flask application redirects all incoming requests to a new domain using a 301 (permanent) redirect.

## Description ℹ️

This simple Flask app redirects all incoming requests to a specified new domain. If the original request had a path, it preserves that path while redirecting.

## Setup and Usage 🚀

1. **Requirements:**
    - Python 🐍
    - Flask (install via `pip install Flask`) 📦

2. **Running the Application:**

    a. Clone the repository:
    ```
    git clone https://github.com/loka1/Redirect-code-for-domains-flask
    ```

    b. Navigate to the project directory:
    ```
    cd Redirect-code-for-domains-flask
    ```

    c. Run the Flask application:
    ```
    python api/index.py
    ```

3. **Usage:**

    Once the application is running, it will redirect all requests to the specified new domain `http://phplin.com`.

    - If you access `http://your_domain/any_path`, it will redirect to `http://phplin.com/any_path`.
    - Accessing `http://your_domain/` will redirect to `http://phplin.com`.

## Configuration ⚙️

- **Changing the New Domain:** If you want to redirect to a different domain, modify the `new_domain` variable in `app.py`.

## Important Notes 📝

- This code uses a 301 HTTP status code for permanent redirection.
- Ensure you handle the `new_domain` variable securely to avoid unintended redirections.

## License 📄

## Contributions 🤝

Feel free to contribute, open issues, or make suggestions for improvement.

## Acknowledgments 🙌


