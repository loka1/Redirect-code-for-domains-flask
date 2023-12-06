from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def redirect_to_new_domain(path):
    new_domain = 'http://phplin.com'
    new_url = f'{new_domain}/{path}' if path else new_domain
    return redirect(new_url, code=301)

if __name__ == '__main__':
    app.run()
