## The Neighborhood
>[mwendwa](https"//github.com/Morces)

## Description
 This is a web application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts.

 ## Screenshot
 ### Homepage

![Screenshot from 2022-06-20 15-35-44](https://user-images.githubusercontent.com/97943808/174603258-f3c87eec-f722-4de9-9e54-b37c64ec4177.png)

### All Neighborhoods
![Screenshot from 2022-06-20 15-36-05](https://user-images.githubusercontent.com/97943808/174603355-f873e2f8-94ba-435e-9893-746aa71a5618.png)

 ## User Story
As a user, I would like to:
- Sign in with the application to start using.
- Set up a profile about me and a general location and my  neighborhood name.
- Find a list of different businesses in my neighborhood.
- Find Contact Information for the health department and Police authorities near my neighborhood.
- Create Posts that will be visible to everyone in my neighborhood.
- Change My neighborhood when I decide to move out.
- Only view details of a single neighborhood.

## SetUp instructions
Clone the repo
```bash
https://github.com/Morces/the-neighborhood.git
```
Navigate into the cloned repo
```bash
cd the-neighborhood 
```
Install and activate venv
```bash
- python3 -m venv virtual - source virtual/bin/activate
- pip install -r requirements.txt
```
Set up database, host the and migrate.
```bash
python3 manage.py makemigrations 
```
Migrate
```bash
python3 manage.py migrate
```

Run the application
```bash
python3 manage.py runserver
```

### Technologies Used
- Django4.0 - for development of the application.
- Heroku -  for deployment.
- Git - for version control

### Contibutions and Support
Pull Requests are welcomed

### Contact information 
Reach me through email [mwendwapk8@gmail.com]

### License
[MIT license](https://github.com/Morces/the-neighborhood/blob/master/LICENSE)
