# Cover Page
### System Design for InternHub
###### Created on July 17th 2017

# Table of Contents
1. [CRC Cards](#crc-cards)
2. [Software Architecture](#software-architecture)
3. [System Decomposition](#system-decomposition)

## CRC Cards
**User**  
- Superclass: N/A 
- Subclass: Employer, Student, Admin
- Responsibilities: 
  * Knows it's user details (name, email, password, etc.)
  * Provides information to handler
- Collaborators:   
  * Handler
  
**Student**
- Superclass: User
- Subclass: N/A
- Responsibilities: 
  * Knows it's school
  * Knows it's qualifications(skill level)
- Collaborators:     
  * Handler  
  
**Employer**
- Superclass: User
- Subclass: N/A
- Responsibilities: 
  * Knows company info and position within company
- Collaborators:   
  * Handler  
  
**Admin**
- Superclass: User
- Subclass: N/A
- Responsibilities: 
  * Knows administrative details
- Collaborators:   
  * Handler  
  
**Job**
- Superclass: User
- Subclass: N/A
- Responsibilities: 
  * Knows skill level and other job details
  * Knows Job ID
- Collaborators:   
  * Handler  
  
**Documents**
- Superclass: User
- Subclass: N/A
- Responsibilities: 
  * Knows corresponding Job ID
  * Knows what student uploaded the documents
  * Knows upload time
  * Knows location(path) of resume and cover letter on disk
- Collaborators:   
  * Handler
  * Job
  * Student
    
  
 **Handler**
- Superclass: N/A
- Subclass: N/A
- Responsibilities: 
  * Updates database
  * Creates new job postings
  * Displays job postings based on skill level
  * Displays job postings based on application deadline
  * Displays all job postings
  * Associates user and documents with job application
  * Displays job applications to employers
  * Displays prior job description applications to students
  * Communicates with controllers
- Collaborators:   
  * User
  * Student
  * Employer
  * Admin 
  * Job  
  * Documents
   
## Software Architecture 

![Software Architecture Diagram](https://github.com/UTSCCSCC01/Better-Jobs/blob/master/images/design/systemarchv3.png "Software Architecture Diagram")

SQLite: used for persistant data  
Django: used for the backend to process information from the controller and to communicate with the database  
HTML/CSS/Views(in Django)/ListJS/jQuery/: used to get requests from users and communicate with the backend and display info on webpage

### System Decomposition
Users will interact with the UI and we will use views in Django to send information needed to our Python/Django backend, which will then reteieve information and/or update the database if needed. Next, data is transferred back to the frontend and displayed for the user to see, using views in Django. Invalid user input will be taken care of at all steps in our process, through the frontend, backend, and even the database attribute restrictions. Any errors or further failures will be reported to the user in the form of a user friendly message. The JavaScript library called ListJS as well as some jQuery is used for job table searching and sorting. 