# CRM-App-Project
This is a Flask based CRM application
currently being set-up for real-estate agents. :city_sunrise:

## Sections
  1. [Usage](#usage)
  2. [Current Set-Up](#current-set-up)
  3. [Stretch Features](#stretch-features)
  4. [Issues](#)
  5. [Next Up](#)

## Usage
  The goal of this app is to allow a real estate team to track clients, properties shown, and properties under contract by agent.
  Agents should be able to share feedback about properties with other agents.
  
### Current Set-up
  MVP Goal: Basic CRUD app with infrastructure to allow cross sharing of properties and information between agents (users) within a team.
  
### Status:
| # | Project | API | GUI |
|---|---------|-----|-----|
|1|Create|||
|2|Read|:heavy_check_mark:||
|3|Update|||
|4|Destroy|||
  
### Stretch features: 
1. Automated emailing to Clients when an important date is arriving (closing, check due, reply to inspection, etc).
2. Agents can track each touch point with a client and sort clients by least contacted, or most contacted.

### :coffee: Issues
Work on Front End Design. Considering React.
Currently breaks when add same client twice.

### :snail: Next Up
  1. Set-up layout of CRM Dashboard.
  2. Automate testing.
  3. Cache logged in users.
  4. Log in process to use API w/o web app.


### :beers: Work in Progress

  1. [API set-up](https://github.com/mrcrnkovich/CRM-App-Project/blob/master/app/API.py)
  2. [Queries module for access to SQL database](https://github.com/mrcrnkovich/CRM-App-Project/blob/master/app/query.py)
  3. [SqlAlchemy Objects](https://github.com/mrcrnkovich/CRM-App-Project/blob/master/app/models.py)
