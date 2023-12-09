from flask import Flask, redirect

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def redirect_to_new_domain(path):
    """
    Redirects incoming requests to a new domain.

    Args:
        path (str): The path from the original request.

    Returns:
        Response: Redirects to the new domain with the provided path, if any.
    """
    new_domain = 'http://phplin.com'
    new_url = f'{new_domain}/{path}' if path else new_domain
    return redirect(new_url, code=301)

if __name__ == '__main__':
    app.run()
