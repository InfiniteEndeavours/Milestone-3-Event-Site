# Event Finder

Event Finder is a website where users can look for events, register for events, and where event coordinators can post
events.

The live website can be found [here](https://ci-ms3-event-finder.herokuapp.com/)

![AmIResponsive](docs/images/am_I_responsive.png)

# Content

* [User Experience](#user-experience)
    * [Project Discussion](#project-discussion)
    * [User Stories](#user-stories)
* [Design and User Interface](#design-and-user-interface)
    * [Color Palette](#color-palette)
    * [Typography](#typography)
    * [Features](#features)
    * [Images](#images)
    * [Structure](#structure)
    * [Accessibility](#accessibility)
* [Technologies](#technologies)
    * [Languages Used](#languages)
    * [Frameworks, Programs, Libraries and APIs used](#programs-libraries-frameworks-and-apis)
* [Deployment & Development](#development-and-deployment)
    * [Local Development](#local-development)
    * [Deployment](#deployment)
* [Testing](#testing)
    * [Bugs](#bugs)
    * [Validation](#validation)
    * [Testing User Stories](#testing-user-stories)
    * [Lighthouse](#lighthouse-testing)
    * [Manual Testing](#manual-testing)
* [Credits](#credits)

# User Experience

## Project Discussion

The aim of this for individuals is;

- To view events being held in their area.
- To Register their interest for an event.
- See which events they have registered for.

The aim of this project for coordinators is;

- To allow them to perform CRUD functions for events.
- See who is coming to an event.
- Promote Events.

## User Stories

### Site Designer Goals

As the site designer, I want to be able to allow users to do the following:

- Register.
- Login.
- Create Events.
- Register interest for events.
- View which events they have created/have interest in.
- Allow event coordinators to promote events to the front page of the site.
- Have an administration page for administration of the site without needing to access the backend.

### Individual

As an individual, I want to be able to:

- View events in my area.
- Create an account.
- View which events I have registered for.

### Event Coordinator

As an event coordinator, I want to be able to:

- Create events.
- Update events.
- Delete Events.
- Promote my event.

# Design and User Interface

## Color Palette

![Color-Palette](docs/images/color_palette.png)

The palette I have chosen is based on the [Nord](https://www.nordtheme.com/docs/colors-and-palettes) palette.
The base colours, `#2e3440` and `#4C566A` have not been modified and are to be used for styling the background of
elements.

I have modified `#88C0D0` to be lighter to ensure it passes the WebAIM Contrast Checkers AAA
standards. It's new value is `#A1D5E0`.

I feel the Nord colour scheme is a very smooth palette, and doesn't create too much visual disturbance colour wise.

## Typography

The font selection I have chosen is similar to [Raycast's](https://www.raycast.com/) website design.

I personally find 'JetBrains Mono' easy to read and a nice universal font.

- 'JetBrains Mono' from Google Fonts. This is a Monospace font and will be used for most content (Headings, links,
  navigation, buttons)
- 'Inter' from Google Fonts. This is a Sans Serif font and will be used for paragraphs, strong and italicised text.

## Features

This site will contain multiple pages, where some content is static (such as the login/register pages), and where
content is dynamic (events page).
All pages will be responsive, for use on Mobiles, Tablets and Desktops.

#### Base Template

- Navigation Bar
- Footer

#### Home Page

- Jumbotron
    - Contain image of an event
    - Button to view events
- Cards
    - Feature promoted events

#### Event Page

- List Events from Users
    - Show information of event (brief overview)
- Filter events based on category

#### Profile Page

- Display Name/Username/Email
- Display events user is interested in
- Display events user is hosting
- Option to change password

#### Add Event Page

- Form
    - Event Title
    - Event Location
    - Maximum amount of Attendees
    - Entry Price (optional)
    - User who organized event

#### Login Page

- Form
    - Email address
    - Password
    - Submit button

#### Register Page

- Form
    - Email Address
    - Password
    - Password confirmation
    - Submit button

#### Administration Page

- Table
    - List of Events with details and delete button

## Images

Any images used for this project will be sourced from [Unsplash](https://unsplash.com/).
They will also be related to the theme of the site, which is events.

## Structure

### Website Structure

The structure for the site can be found [here](docs/wireframes/Wireframe.pdf). It's possible that this may
change in the future.

### Database Structure

The schema for the database can be found [here](docs/images/db_schema.png).

The User model has been defined as follows:

| Column Name | Schema                                                           |
|-------------|------------------------------------------------------------------|
| ID          | Primary Key                                                      |
| uuid        | Varchar(36), Unique, Not Nullable, default value of uuid.uuid4() |
| username    | varchar(50), Unique, Not Nullable                                |
| password    | varchar(255)                                                     |
| admin       | Boolean, default value of False                                  |
| profile     | One-to-one relationship with the Profile model.                  |
| events      | One-to-many relationship with the Event model.                   |

The Profile model has been defined as follows:

| Column Name | Schema                           |
|-------------|----------------------------------|
| ID          | Primary Key                      |
| first_name  | Varchar(50), Not Nullable        |
| last_name   | Varchar(50), Not Nullable        |
| uuid        | Foreign Key to User UUID, Unique |

The Event model has been defined as follows:

| Column Name | Schema                                                |
|-------------|-------------------------------------------------------|
| ID          | Primary Key                                           |
| title       | Varchar(100), Not Nullable                            |
| description | Varchar(500), Not Nullable                            |
| date        | DateTime, Not Nullable, default value of today's date |
| start_time  | Time, Not Nullable, default value of 9(am)            |
| end_time    | Time, Not Nullable, default value of 17(5PM)          |
| location    | Varchar(255), Not Nullable                            |
| creator_id  | Foreign Key to User UUID, Not Nullable                |

The Attendance model has been defined as follows:

| Column Name | Schema                                |
|-------------|---------------------------------------|
| id          | Primary Key                           |
| user_id     | Foreign Key to User ID, Not Nullable  |
| event_id    | Foreign Key to Event ID, Not Nullable |

The [Models](event_finder/event/models.py) were created using SQLAlchemy, and the tables were then created again with
SQLAlchemy using `db.create_all()`.

## Accessibility

The site will be accessible to all users, regardless of disability.

Any colors used will be checked to ensure they pass the WebAIM Contrast AAA standards.

I'll also include the following:

- Aria labels where needed.
- Semantic HTML.
- Bootstraps visually hidden classes for elements are meant to only be seen by Screen Readers.

# Technologies

## Languages

For this project, I will be using the following languages:

- HTML
- CSS
- JavaScript
- Python

## Programs, Libraries, Frameworks and APIs

During this project, I will use the following programs:

- Git
- GitHub
- JetBrains PyCharm
- Google Chrome
- Google Chrome DevTools
- Firefox
- Polypane

I will use the following libraries and frameworks:

- Bootstrap 5.2
- Font Awesome Icons
- Google Fonts
- jQuery (Relied on by Bootstrap)
- Flask
- Flask-SQLAlchemy
- Faker (Fake data generation for testing)

For Faker, I used [this file](event_finder/event/data/fake_data_generator.py) to generate the helper functions for the
fake data.

A function was then created in __init__.py called `fake_data` which combined all the helper functions into one function.

This function was then imported into app.py and called in combination with db.drop_all() and db.create_all() to prep the
database and generate clean fake data for testing.

The database I have chosen to use is PostgresSQL, which is a relational database.
I will use both SQL and SQLAlchemy to interact with the database.

These sites were also used:

- Am I Responsive - for the document title image.
- Compressor.io - for compressing images.
- Converti.co - for converting images to webp.
- Unsplash - for images.

# Development and Deployment

For this project, I developed on my workstation using PyCharm.

### Local Development

To develop this repository locally, you will need to do the following:

1. Install PostgreSQL (Version 15), though with modification to the DB_URI env key you can use another relational
   database.
2. Install Python (Version 3.10).
3. Clone this repository.
    - This can be done by either using `git clone https://github.com/InfiniteEndeavours/Milestone-3-Event-Site.git` in
      the terminal, or by using GitHub Desktop.
4. Create a virtual environment.
    - This can be done by using `python -m venv venv` in the terminal.
    - The purpose of a virtual environment is to keep the dependencies for this project separate from other projects.
5. Activate the virtual environment.
    - This can be done by using `source venv/bin/activate` in the terminal.
6. Install program requirements.
    - This can be done by using `pip install -r requirements.txt` in the terminal.
7. Create a `.gitignore` file and add `env.py` to it.
8. Create the env.py file in the root of your project directory.
9. Add the following to env.py

- ```python
   import os

   # Set IP for Flask Server - 0.0.0.0 uses all IPs on Device
   os.environ.setdefault("IP", "0.0.0.0")
        
   # Set Port for Flask Server - 5000 is common but interferes with Airport on macOS
   os.environ.setdefault("PORT", "5555")
        
   # Set Debug to True - Enables development server for Flask
   # Remove this key before deploying to production
   os.environ.setdefault("DEBUG", "True")
        
   # Set SECRET_KEY for Flask Flashes
   os.environ.setdefault("SECRET_KEY", "<SECRET_KEY>")
        
   # Database Connection String
   os.environ.setdefault("DB_URI", "postgresql://user:password@hostname/database_name")

10. Run the app.py file.
    - This can be done by using `python app.py` in the terminal.

For browser and CSS testing, I used Google Chrome, FireFox and Polypane for testing.

To fill my database with data, so I could build web pages etc. properly, I used Faker to create fake data.

The data generator can be found at `event_finder/event/data/fake_data_generator.py`.

This file was run after the database schema was created and only ran once at the start of the project.

At time of deployment, the database had all tables dropped and recreated using SQLAlchemy.

#### Cloud Development

While it is an option to develop using a Cloud IDE, I chose not to do this.

If you wish to use one, such aas CodeAnywhere, please copy all files
from [this](https://github.com/Code-Institute-Org/ci-full-template) repository to the current one.

You can then use CodeAnywhere to create a workspace based off of this repository.

You will still need to do the following:

- Create a virtual environment.
- Activate the virtual environment.
- Install program requirements.
- Create a `.gitignore` file and add `env.py` to it.
- Create the env.py file in the root of your project directory.
- Add environemnt variables from above.

### Deployment

I deployed this project on Heroku, with the use of ElephantSQL for database hosting. This was done by doing the
following:

#### ElephantSQL

1. Logged into ElephantSQL via GitHub.
2. Selected 'Create New Instance'.
3. Named DB 'event_finder' and selected 'Tiny Turtle' plan.
4. Selected Region.
5. Confirm creation.

#### Heroku

1. Creating a file named 'Procfile' in the root of my project directory.
2. Adding ` web: python app.py` to the 'Procfile'.
3. Exporting requirements of app to a txt.
    - This was done by running `pip3 freeze --local > requirements.txt` in the terminal.
4. Creating a Heroku Account.
5. Creating a new application, then naming it and selecting region.
6. Followed [this document](https://devcenter.heroku.com/articles/github-integration).
7. Enable Automatic Deploys on 'main' branch.
8. Added the environment variables from local `env.py`file to the 'Config Vars' in Application settings.

# Testing

During the project, I have tested using Google Chrome, Firefox and Polypane. These helped me trouble shoot styling
issues.

The terminal was also used extensively to troubleshoot errors with Flask and SQLAlchemy.

## Bugs

During development and testing, a number of bugs were discovered. Where a fix has not been applied, a reason is given.

1. Conflict between relationships User and Event relationships in Models.py.
    - Resolved - Removed unnecessary relationship from Models.py
2. Registration form clears if validation of password fails.
    - Unresolved - No fix has yet been put in place. Based on research, this would require a reconstruction of the
      route.
3. Table on Administration page does not scale with mobile devices.
    - Unresolved - As this is only visible to the site admin (or creator of the DB), that this feature doesn't need to
      be prioritised. If time is available then a fix will be looked at.
4. Featured Events on Home page can sometimes display the same event.
    - Unresolved - This event has a low chance of happening and is more prominent when there are only a handful of
      entries in the database.
5. When creating or editing an event, using more than 500 characters in the description would cause an overflow error.
    - Resolved - Added a maxlength attribute to the textarea element in the form.
6. An issue would appear where the database would attempt to create two users with the same UUID.
    - Steps to reproduce
        - Attempt to create a user with an invalid password
        - Attempt to create a user with a valid password
        - Another user then attempts to create a new account, with a valid password and is presented with an error.
            - Duplicate Entry for Key 'user_uuid'
    - Resolved - The issue was caused by the database having a default cell value for the uuid. When a user was created
      the first time, the session was not emptied and the uuid was not reset. This meant that when a new user was
      created, the uuid was already in use. To resolve this, I set the UUID to be generated on insert in the
      Registration route.

## Validation

To validate the HTML, CSS and Python the following sites were used:

- [HTML Validator](https://validator.w3.org/) by W3C
- [CSS Validator](https://jigsaw.w3.org/css-validator/) by W3C
- [CI Python Linter](https://pep8ci.herokuapp.com/)

## HTML Validation

Below are links to screenshots of the HTML Validation results.
Please note, that due to the use of Font Awesome Icons, an unavoidable error is created.

- [base.html](docs/validation/html/index.png) and [index.html](docs/validation/html/index.png)
- [events.html](docs/validation/html/events.png)
- [event_info.html](docs/validation/html/event_info.png)
- [create_event.html](docs/validation/html/create_event.png)
- [edit_event.html](docs/validation/html/edit_event.png)
- [profile.html](docs/validation/html/profile.png)
- [register.html](docs/validation/html/register.png)
- [login.html](docs/validation/html/login.png)
- [admin.html](docs/validation/html/admin_page.png)

[Here](docs/validation/css/css.png) is a link to the CSS Validation.

[This folder](docs/validation/python) contains screenshots of all Python files passing Code Institutes PEP8 Linter.

The code was also checked using `pycodestyle` and `pydocstyle` through PyCharm, which all scripts passed.

[This](https://mariasoria.dev/en/2022-07-27-how-to-configure-a-linter-formatter-in-pycharm) guide was used to set this
up validation.

## Testing User Stories

### Site Designer Goals

As a site designer, I have been able to provide the following to users:

- Registration Function
    - When a user submits the registration form with valid information, an entry is created in the database.
      ![User Example](docs/user_stories/db_user_entry.png)
- Login Function
    - When a user submits the login form with valid credentials, then a session cookie is added to indicate they are
      logged in.
      ![Session Token](docs/user_stories/session_cookie.png)
- Ability to create events
    - Users are able to create events, which are then stored in the database.
      ![Event Example](docs/user_stories/db_event_entry.png)
- Ability to register interest in an event
    - Users are able to register interest in events, which then stores the user_id and event_id in the `attendance`
      table.
      ![Session Token](docs/user_stories/db_attendance_entry.png)

### Individual Goals

As an individual I can perform the following:

- View events
    - I am able to view events on the events page.
      ![Events Example](docs/user_stories/user_events.png)
- Create an account
    - I am able to create an account and view it on the profile page.
      ![Profile Example](docs/user_stories/user_profile.png)
- View which events I have registered for.
    - I can view which events I have registered for on the profile page.
      ![Attending Events Example](docs/user_stories/user_attending_events.png)

### Event Coordinator

As an event coordinator, I can perform the following:

- Create Events
    - I can create an event when logged in.
      ![Event Creation](docs/user_stories/create_event.png)
- Update Events
    - I can update the event I created.
      ![Event Update](docs/user_stories/update_event.png)
- Delete Events
    - I can delete the event I created. After pressing confirm, the event is deleted.
      ![Event Deletion](docs/user_stories/delete_event.png)
- Promote my Event
    - I can see events are promoted on the home page.
      ![Event Deletion](docs/user_stories/random_event.png)

## Lighthouse Testing

During the Lighthouse Testing, I saw consistently lower scores on the mobile tests. I believe this is due to Chrome
emulating a device from 2016. While testing on my mobile, an iPhone 12 Pro Max, and on a Samsung S20, I saw no
performance issues.

Another probable cause of the poor performance during the mobile test score is the amount of unused CSS being imported
by Bootstrap, which I am
currently unable to minimise properly. While trying to get the Bootstrap file minimised to use only the styles my site
uses, I was able to reduce the file from 190KB to roughly 30KB.

Below are links to lighthouse tests for each page on the site:

- index.html/base.html
    - [Mobile](docs/lighthoust_testing/index_mobile.png)
    - [Desktop](docs/lighthoust_testing/index_desktop.png)
- events.html
    - [Mobile](docs/lighthoust_testing/events_mobile.png)
    - [Desktop](docs/lighthoust_testing/events_desktop.png)
- create_event.html
    - [Mobile](docs/lighthoust_testing/create_event_mobile.png)
    - [Desktop](docs/lighthoust_testing/create_event_desktop.png)
- edit_event.html
    - [Mobile](docs/lighthoust_testing/edit_event_mobile.png)
    - [Desktop](docs/lighthoust_testing/edit_event_desktop.png)
- event_info.html
    - [Mobile](docs/lighthoust_testing/event_info_mobile.png)
    - [Desktop](docs/lighthoust_testing/event_info_desktop.png)
- profile.html
    - [Mobile](docs/lighthoust_testing/profile_mobile.png)
    - [Desktop](docs/lighthoust_testing/profile_desktop.png)
- admin.html
    - [Mobile](docs/lighthoust_testing/admin_mobile.png)
    - [Desktop](docs/lighthoust_testing/admin_desktop.png)
- register.html
    - [Mobile](docs/lighthoust_testing/register_mobile.png)
    - [Desktop](docs/lighthoust_testing/register_desktop.png)
- login.html
    - [Mobile](docs/lighthoust_testing/login_mobile.png)
    - [Desktop](docs/lighthoust_testing/login_desktop.png)

## Manual Testing

For manual testing, I used three devices;

- Desktop - 3440 x 1440 - Google Chrome, Safari, Firefox
- Laptop - 2560 x 1600 - Google Chrome, Safari, Firefox
- Mobile - 1284 x 2778 (Portrait) and 2778 x 1284 (Landscape) - Google Chrome, Safari, Firefox

### Testing Process

### Responsiveness

While testing the responsiveness of the site, I noticed no issues with responsiveness or any elements being moved out of
place.

As I don't have a tablet, I used Polypanes device emulation to simulate a tablet and noticed no issues there
either.

On mobile, two issues were discovered, on the profile page, and administration page.

On the profile page, the user information banner and 'Events Attending' section were not moving correctly. On smaller
devices each section should be in its on column. I resolved this by updating the column sizes in the containing divs.
Fixed in commit `c38bc883`.

On the administration page, with devices smaller than 770px in width, the table doesn't resize correctly. I resolved
this by making the `location`, `start time` and `end time` visible only on large breakpoints and above. This was fixed
in commit `89574543`.

There is still an issue where on devices lower than 348px in width, the table will still break formatting. I have left
this as it is, as the average mobile device is wider than this.

### Hyperlinks

I visited each page on the site and tested all hyperlinks that were present. Links which navigate to different pages on
the site worked fine, along with links to external sites in the footer. All external links opened in a new tab.

# Credits

## Code

- Bootstrap 5.2: THis library was used to make the site responsive.

## Content

- Example events were created by friends and family.

## Acknowledgements

- Andrew Buncombe (Colleague) for advice on the Database Schema.
- Jack Wachira - My Code Institute Mentor for his feedback on the project.
- Stephen Dawson for his feedback on the project around the styling of some elements