# T3A3 (ASEAN HUB) - Implement a System with Data and Application Layers

### **R2 Discuss how the application will handle the privacy of user data within the system, and how security features of the frameworks you are utilising will assist to mitigate security concerns.**

The privacy of the application will be in many ways protected from both accidental and malicious attacks.

The first protected object will be the user's information when signing up on the web app. The information will be sent into a database which is launched separately from the main application itself. The benefit of having the database separate from the application is that malicious attackers would not be able to steal data from the main application as the application is separated from the database.

 This also works against SQL injections as it is again unable to request any SQL queries from the web application directly to the database. In terms of accessing the database through other means, the attacker will have to go through multiple barriers before being able to access the database.
 
  The database will be placed into an ec2 instance, which would also then be placed in its VPC (virtual private cloud). Having it in its VPC network will make accessing the database a bit harder, as the attacker will have to go through multiple barriers to access it.

### **R3 Discuss how you will address the following obligations as a developer:
- **professional obligations (delivering the project on time, being explicit about ongoing maintenance of the system)**
- **ethical obligations: ensuring that the application conforms with ethical codes of conduct approved by industry**
- **legal obligations: that you have assessed whether the application is subject to any legal regulation, if none, consider any privacy implications**

Professional obligations: For this project, it will be done under several hours in many days of the week. To ensure completion of project, due dates and tasks will be set out in the week and must be completed. During development stage the project will continuously be saved and backed up by multiple storage components. 

One of the storage component will be a physical portable ssd (solid state drive) hard drive, the second storage component will be done remotely using the service 'Github'. 

Ethical obligations: The ethical obligations, are to make sure for every git push to github is to name every push with details of what has changed. Having this done periodically either timely based or event based. Having it done repeatedly will show great integrity and rollbacks if the projects break and is unable to be fixed easily.

Legal obligations: Creating database where user will have to enter personal information will be taken highly serious. User's information has the rights to be protected, secure and maintain for any mishaps or malicious events in present or future.

For developers, in the occasion of user's information being exposed, developers will not under any circumstance use user's information for any personal endeavors, or any actions that is not believed to be assisting the development process.

## EC2 Instance

**54.153.227.234**