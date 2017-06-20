# Cover Page
### System Design for InternHub
###### Created on June 19th 2017

# Table of Contents
1. [CRC Cards](#crc-cards)
2. [Software Architecture](#software-architecture)

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
- Collaborators:   
  * Handler
  
  **Handler**
- Superclass: N/A
- Subclass: N/A
- Responsibilities: 
  * Updates database
  * Creates new job postings
  * Displays job postings based on skill level
  * Displays all job postings
  * Communicates with controllers
- Collaborators:   
  * User
  * Student
  * Employer
  * Admin
  
Note: More responsibilities and classes to be added in future sprints.
  
## Software Architecture 

![Software Architecture Diagram](https://github.com/UTSCCSCC01/Better-Jobs/blob/master/images/design/systemarch.png "Software Architecture Diagram")
