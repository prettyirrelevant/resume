from resume import create_app
from settings import development, production

app = create_app(development, production)

if __name__ == "__main__":
    app.run()
