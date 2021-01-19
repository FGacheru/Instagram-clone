# Instagram-Clone

#### Author: [Francis Gacheru]


* Link to live site: [Instagram-Clone]()

## Description
The application allows users to sign up, upload images,view other user's pictures,like them, comment on them and also follow the other users.
   |


| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| Login	if already have an account |if you dont have , click on the sign up link and fill the form  | If login is successful, user is navigated to home page | 
| Edit profile | On the account link, click on the  update profile | Redirected to the home page |
| Click on profile | Redirects to the profile page | User adds bio and profile picture |
|Comment and like on a post|Click on the comment and like icon and add a comment and like|The comment and like will be added to the post's
|Add a new post|Click on the New Profile icon to be redirected to the new post form|the post will be rendered to the home page
| Click on log Out in the accounts| Redirects to the login form | Logs out user  |

## Setup and installations
* Fork the data onto your own personal repository.
* Clone Project to your machine
* Activate a virtual environment on terminal: `. virtual/bin/activate`
* Install all the requirements found in requirements file.
* On your terminal run `python3.6 manage.py runserver`
* Access the live site using the local host provided



## Getting started

### Prerequisites
* python3.6
* virtual environment
* pip

#### Clone the Repo and rename it to suit your needs.
```bash
git clone https://github.com/FGacheru/Instagram-clone
```
#### Initialize git and add the remote repository
```bash
git init
```
```bash
git remote add origin <your-repository-url>
```

#### Create and activate the virtual environment
```bash
python3 -m venv virtual
```

```bash
source virtual/bin/activate
```

#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Make and run migrations
```bash
python3.6 manage.py check
python manage.py makemigrations news
python3.6 manage.py sqlmigrate news 0001
python3.6 manage.py migrate
```

#### Run the app
```bash
python3.6 manage.py runserver
```
Open [localhost:8000](http://127.0.0.1:8000/)



## Testing the Application
`python manage.py test insta`
        
## Built With

* [Python3.6](https://docs.python.org/3/)
* Django 2.2.8
* Postgresql 
* Boostrap4
* HTML


## Support and contact details
 Incase you come across errors, have questions, ideas ,concerns, or want to contribute to the application you can feel free to reach : francisgacheru2001@gmail.com


### License

* [[License: MIT]](Licence.md) <francisgacheru2001@gmail.com>
