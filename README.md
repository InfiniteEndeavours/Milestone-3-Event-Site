# Event Finder

Event Finder is a website where users can look for events, register for events, and where event coordinators can post
events.

The live website can be found [here](#)

![AmIResponsive]()

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
    * [Languages Used](#languages-used)
    * [Frameworks, Programs, Libraries and APIs used](#programs-libraries-frameworks-and-apis-used)
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
The base colours, `nord0` and `nord3` have not been modified and are to be used for styling the background of elements.

I have modified `nord7` and `nord8` to be slightly lighter to ensure they pass the WebAIM Contrast Checkers AAA
standards.

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