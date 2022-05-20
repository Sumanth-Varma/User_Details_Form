1. Extract all files from Zip folder including env folder
2. activate the virtual environment by using "env\Scripts\activate"
3. Open a terminal or command prompt and go into project folder.
4. install all packages using requirements.txt by using "pip install -r requirements.txt" or install packages listed in requirements.txt manually.
5. Go to myWebPage folder
6. Run the migrations commands as follows:
	- python manage.py makemigrations
	- python manage.py migrate
7. Create a superuser by using following command (Optional)
	- python manage.py createsuperuser
8. Run the server using following command
	- python manage.py runserver
9. Place the following url at end of localhost "/registerDetails"