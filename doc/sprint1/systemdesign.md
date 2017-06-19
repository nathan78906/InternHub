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
  
  
  
## Software Architecture 

![Software Architecture Diagram](https://github.com/UTSCCSCC01/Better-Jobs/blob/master/images/design/systemarch.png "Software Architecture Diagram")
