# Internship Manager

## Introduction
This project was made for the [RedLight Summer Internship 2023 - Dev Challenge](https://gitlab.com/PedroDSFerreira/si-23-dev-challenge)

## Architecture

### Front-end

- HTML
- Tailwind CSS
- Flowbite
### Back-end

- Django
- PL/pgSQL

## Requirements

- Python 3.x
- PostgreSQL
- Pipenv (optional)

## Set Up

1. Clone the repository:
    
    ```
    git clone https://github.com/joas124/ChallengeRedLight.git
    ```
    If you don't have git installed, you can download the .zip file [here](https://github.com/joas124/ChallengeRedLight/archive/refs/heads/main.zip).
    
2. Navigate to the project directory.
    
    ```
    cd ChallengeRedLight
    ```

3. Create the database and user in PostgreSQL:

    * Connect to the PostgreSQL server with the the following command (you will be prompted to enter the password you set during the installation):

    ```
    psql -h localhost -p {port: default 5432} -d postgres - U postgres
    ```
    > **Note:** If you are using Windows, you can use the [pgAdmin](https://www.pgadmin.org/) tool to manage your PostgreSQL server.
    
    * Then, run the following commands to create the database and user:

    ```sql
    CREATE DATABASE redlightchallenge;
    CREATE USER redlight WITH PASSWORD 'redlight';
    ALTER DATABASE redlightchallenge OWNER TO redlight;
    ```
    
    > **Note:** If you want to use a different database name, user, or password, make sure to update the `DATABASES` setting in `redlight/settings.py` accordingly.
    
4. Install the project dependencies:

    Run the following command to install the dependencies:
    > **Note:** If you are using Pipenv, you can install the dependencies with `pipenv install`.

    > **Note 2:** If you plan to use a virtual environment, make sure to activate it before running the command below.
    ```
    pip install -r requirements.txt
    ```

    or

    ```
    python -m pip install -r requirements.txt
    ```
    

5. Javascript dependencies:

    Run the following command to install the dependencies:

    ```
    npm install
    ```

6. Run the migrations:

    ```
    python manage.py migrate
    ```

    Now, your database should be set up and ready to go.




## Usage

1. Run the development server:
    > **Note:** If you are using Pipenv, make sure to activate the virtual environment `pipenv shell` before running the command below.

    ```
    python manage.py runserver
    ```

    Now, you can access the application at [`http://localhost:8000/`](`http://localhost:8000/`).


## References

- [Django Documentation](https://docs.djangoproject.com/en/3.2/)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [Flowbite Documentation](https://flowbite.com/docs/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Pipenv Documentation](https://pipenv.pypa.io/en/latest/)
