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
    * [Online Development](#online-development)
    * [Deployment](#deployment)
* [Testing](#testing)
    * [Bugs](#bugs)
    * [Validation](#validation)
    * [Testing User Stories](#testing-user-stories)
    * [Lighthouse](#lighthouse-testing)
    * [Testing Methodologies](#testing-methodologies)
    * [Manual Testing](#manual-testing)
    * [Automated Testing](#automated-testing)
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

As an individual, want to be able to:

- View events in my area.
- Filter events based on categories.
- Create an account.
- View which events I have registered for.

### Event Coordinator

As an event coordinator, want to be able to:

- Create events.
- Update events.
- Delete Events.
- View who is interested in a specific event.
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

## Images

Any images used for this project will be sourced from [Unsplash](https://unsplash.com/).
They will also be related to the theme of the site, which is events.

## Structure

The structure for the site can be found [here](docs/wireframes/Wireframe.pdf). It's possible that this may
change in the future.

## Accessibility

The site will be accessible to all users, regardless of disability.

Any colors used will be checked to ensure they pass the WebAIM Contrast AAA standards.

I'll also include the following:

- Alt tags for images.
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

I will use the following libraries and frameworks:

- Bootstrap 5.2
- Font Awesome Icons
- Google Fonts
- jQuery (Relied on by Bootstrap)
- Flask
- Faker (Fake data generation for testing)

The database I have chosen to use is PostgresSQL, which is a relational database.
I will use both SQL and SQLAlchemy to interact with the database.

These sites were also used:

- Am I Responsive
- Compressor.io
- Converti.co

# Development and Deployment

For this project, I developed on my workstation using PyCharm.

### Local Development

Before being able to develop on my local machine, prerequisites needed to be met. These were:

* Git - Installed via XCode CLI - Provides Version Control.
* PyEnv - Installed via HomeBrew - Provides ability to manage Python Versions.
* PyEnv Venv - Installed via HomeBrew - Provides ability to manage Virtual Environments through PyEnv.
* Python 3.10 - Installed via PyEnv.
* PostgreSQL@15 - Installed via HomeBrew and activated with HomeBrew services

With these installed, I was able to begin local development, I performed this by:

1. Opening Pycharm and creating a new Project.
2. Initialising a new Git Repository.
3. Logging into GitHub through PyCharm.
4. Create initial commit and push the repository to GitHub.
5. Add `env.py` to `.gitignore` to prevent Flask secret key and Database URI from being exposed to public.
6. Add following to `env.py`:
   ```python
    import os

    # Set IP for Flask Server - 0.0.0.0 uses all IPs on Device
    os.environ.setdefault("IP", "0.0.0.0")
    
    # Set Port for Flask Server - 5000 is common but interferes with Airport on macOS
    os.environ.setdefault("PORT", "5555")
    
    # Set Debug to True - Enables development server for Flask
    os.environ.setdefault("DEBUG", "True")
    
    # Set SECRET_KEY for Flask Flashes
    os.environ.setdefault("SECRET_KEY", "SECRET_KEY_VALUE")
    # Generated using randomkeygen.com
    
    # Database Connection String
    os.environ.setdefault("DB_URI", "postgresql://user:password@hostname/database_name")
    # Obtained from ElephantSQL dashboard
   ```

7. Installing [requirements](requirements.txt) in a Virtual Environment (Default with PyCharm).

For Development, I used Google Chrome, FireFox and Polypane for testing.

To fill my database with data, so I could build web pages etc. properly, I used Faker to create fake data.

The data generator can be found at `event_finder/event/data/fake_data_generator.py`.

This file was run after the database schema was created and only ran once at the start of the project.

At time of deployment, the database had all tables dropped and recreated using SQLAlchemy.

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