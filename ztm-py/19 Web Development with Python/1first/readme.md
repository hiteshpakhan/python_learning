to create the flask app ypu have to use following command in the terminal

        python -m venv app_name


now you have to activate the enviroment

        app_name\Scripts\activate

now you have to install flask by following command

        pip install Flask

then go to the folder of the app by : 

        cd app_name

create a basic python file there 
and paste the basic structure of flask file

        from flask import Flask
        app = Flask(__name__)

        @app.route('/')
        def hello_world():
            return 'Hello, World!'

then to run that file you have to set it to the enviroment by following command

        set FLASK_APP=file_name.py

and now you are good to go for running the flask app by following command

        flask run

now if you want to see your changes emiditely on the app you can on the debug mode by following command

        set FLASK_ENV=development

