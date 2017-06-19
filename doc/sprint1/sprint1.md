Scrum Meeting:
 
 Date: June 16, 2017 13:00-14:00
 Attendees: Nathan, Osaru, Aiyaz, Salman, Omid, Venkada, Ewen
 
 Date: June 19, 2017 17:00-18:00
 Attendees: Nathan, Osaru, Aiyaz, Salman, Omid, Venkada, Ewen
 
Conclusions:
  
  - Needed a way to split work to develop essential yet basic software
  - One question was how to make front end portion for the user (a student) to see,
    so we decided to plan some concepts of what someone may see when entering the site
    for the first time, and broke it down what features to code
  - The other aspect we wanted to start is having a database, therefore we were considering
    different applications to use, and agreeing to use Mongo
  - We needed the database to be filled with fictitious job postings so that we could see
    these postings in the front-end portion of our website
  - Problem was raised later on that Mongo was too difficult to set up in the given time
    for the sprint, so we decided to move to SQL
  - Created database in SQL by second scrum meeting and we needed to (1) use UI to create jobs
    on the site and (2) Add the job to the datebase table. We plan to do (1) by using a script
    instead of getting data via command line, and (2) by doing more research on Django and
    continually test until we can successfully add jobs

Backlog:

  Overview: Implement the ability for students to view available job postings. The core idea that we
  want to develop is to populate the database with job post objects and be available to take requests to
  display the job(s).
  
  User Stories:
  - Priority: 30, Size: 5 
    As a Student, I want to be able to login to a student account, so that I can perform student functions.
  
  - Priority: 110, Size: 8
    As an Employer, I want to be able to post open positions for students to view.
   
   - Priority: 60, Size: 2
    As a Student, I want to be able to sort the job postings by required skill level so that I can
    apply to jobs suited for me.
    
     Task Breakdown:
     - Documentation: Osaru, Venkada, Omid, Salman, Ewen
     - Database(Mongo/SQL)/Python/Desining Structure: Nathan, Osaru
     - Prototype/Concepts/Design: Salman, Omid
     - HTML/CSS/Javascript: Aiyaz, Venkada
