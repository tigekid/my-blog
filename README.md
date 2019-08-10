# My Blog

Social media forum for members to view and comment on similar interests.

## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/tigekid/my-blog.git
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Setup the local configurations:

```bash
cp .env.example .env
```

Create the database:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.