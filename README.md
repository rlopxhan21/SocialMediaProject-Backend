# Social Media Project - Backend

The goal of this project is to create a social media platform where users can create profiles, connect
with friends, share posts, and interact with each other.

## Tech Stacks:
- Backend: Django & Django REST Framework
- Frontend: ReactJS & Material-UI 

## Functionality included:
- JSON Web Token Authentication with Email Verification functionality to activate account and to reset password.
- Users can add like, comment and posts.
- User can change basic settings and add profile picture.
- User can add image in post and comment.

## How to install:
In terminal:

```
git clone https://github.com/rlopxhan21/SocialMediaProject-Backend.git
```


After the clone is successful, open one terminal in /Backend folder:
Run the following command for creating virtual env and installing all the required dependencies.

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

And also create a file .env in /Backend folder and store SECRET_KEY, EMAIL_HOST_USER & EMAIL_HOST_PASSWORD.


If you want to add Frontend as well.
```
git clone https://github.com/rlopxhan21/SocialMediaProject-Frontend.git
```

Open another terminal in /Frontend folder and run the following command for installing all the required dependencies. Also make sure to change baseURL from use api.js and useAxios.js.

```
npm install
```
To run:

On /Backend folder terminal:

```
python manage.py runserver
```

On /Frontend folder terminal:

```
npm start
```
