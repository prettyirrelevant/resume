from resume import create_app
from settings import development

app = create_app(development)

if __name__ == "__main__":
    app.run()
