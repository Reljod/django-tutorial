# Contribution Guide

## Commit Rules
1. Use `[feat|chore|bugfix]: <short description starting with present verb>`
	E.g. `feat: fix view issue#12`
2. Add more comments in commit on things that might require more explanations like answering some `Why` questions.
3. Delete the remote branch after merging to main.



## Run Locally
1. Git clone the repo.
2. Go to nftree folder and create a Python Virtual Environment using the requirements.txt. Guide to do this is in [here](#create-virtual-environment).
3. Install PostgreSQL locally and run it. Make sure to use the default configurations (HOST: localhost, POST: 5432).
4. Export PostgreSQL user and password to DB_USER and DB_PASS, respectively before running the app. It's better if we can just put those in an ```.env``` file.

	**.env file example**
	```env
	DB_USER=<username>
	DB_PASS=<password>
	```
5. Run migration. This command runs queries in your local PostgresSQL based on the model that the project set. The instructions are the Python files under ```migrations/``` folder.
	```
	python manage.py migrate
	```
6. Finally, run the App. In vscode, we can also do ```Run without debugging``` to run the app within the vscode. Then open the app in ```localhost:8000``` as the default. 
	```
	python manage.py runserver
	```
7. (Optional) We can easily debug/test the state of the app by running django shell.
	```
	python manage.py shell
	```

<br>

## Update CSS
We are using Tailwind in our stylings, so check our https://tailwindcss.com/ for documentation.

1. Go to ```nftree/css/tailwind```, and run ```npm install```. This will install all the packages required to build and compile the App's CSS bundle.
2. For Dev mode, we can just run ```npm run dev``` to automatically hot reload the static css that the App is using.
3. For Production mode, we want to run ```npm run build``` to build and compile our css to minified file in static css that the App is using.

<br>

## Create virtual environment
1. Go to nftree folder. ```cd <root-directory>/nftree```
2. Create a virtual environment and activate it.

	*For Mac/Unix:*
	```sh
	python -m venv venv
	source venv/bin/activate
	```

	*For Windows (powershell):*
	```powershell
	python -m venv venv
	.\venv\Scripts\Activate.ps1
	```

3. *(Optional)* For IDEs (e.g. VSCode), select the Python interpreter pointing to the python of the created Virtual Environment.