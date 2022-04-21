# Description

In this Social Media type API user's can create their account, create a post, like a post and can only update and delete their own post.

# Technologies Used

- FastAPI
- Postgresql
- Sqlalchemy
- Alembic database migration tool
- OAuth using JWT
- PyTest for testing
- CI/CD using Github Actions
- Swagger UI

# Installation

- First clone the repository to your machine then run `pip install requirements.txt` to install all the project dependencies.
- Then create a env file in root folder and copy all the variables from env.example file and assign your own database values.

- To start the project type
  `uvicorn app.main:app`
- By default fastapi runs on port 8000 on your localhost

# Website URL

https://fastapi-socialmedia.herokuapp.com/docs

fastapi.png
