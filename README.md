#Introduction
The website is of two pages: upload page and list page
 - It is created using Django framework with CSS, BootStrap, HTML in the front-end with SqlLite3 database. It is hosted on AWS on EC2 instance.
 
###File Structure
 1. calculai - stores the website views, models, URLs and settings for the project.
 2. templates - contains the templates for the two webpages
 3. UploadedMedia - stores the images from the webpages. 
 
###Working Process
 - I created the website and got it to work locally using localhost:8000.
 - Later on, I tried to host it on Google Cloud Platform and it worked well only if I saved the image in the database. But it would not allow write operations on Google Cloud storage for protection reasons. Even `chmod 777 <file>` would not work. 
 - But I thought that storing the file in the database is a bad practice for many reason, esp. if the file is greater than 5 MB. 
 - Therefore, I tried to host on AWS using EC2 instance.
 
###URL : http://52.87.201.161:8000
 
###Link to the source code: https://github.com/pradhanmanva/calculai.git

###Tests:
- Testing with large files and small files.
- It only fails if the file is empty. 

###Challenges:
1. I had to learn Django, GCP and AWS in a day to figure out how to create a web application using those. 
2. Working with Django was a bit slow to grasp due to the multitude of components to handle.
3. Working with GCP was very enriching but again had to learn a lot about its functioning.



