from app import init

app = init.app

@app.route('/')
def hello():
    return 'Hello World'


if __name__ == '__main__':
    app.run()