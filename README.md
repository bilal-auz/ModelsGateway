# Deployment Steps

First clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/bilal-auz/ModelsGateway.git
    $ cd ModelsGateway
    
Activate the virtualenv.
    
Install project dependencies:

    $ pip install -r requirements.txt
    
Run the development server:

    $ python manage.py runserver

Test the API:

    $ http://127.0.0.1:8000/api
