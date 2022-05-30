# My_Gallery_App
This app enables user to view various images that I have posted from my gallery 


* User Story

User can view all photos on index page ordered by the date they were posted
Hovering on an image will reveal more information about it; the title, description, location and time posted.
User can click on the copy button on an image to copy its url for sharing purposes
Clicking an image will toggle a lightbox with an expanded view of the image
User can navigate to other images while on the lightbox view.
User can search photos based on their categories
User can browse photos based on the location they were taken


#### Author
* Brian 

Description
A photo gallery web application made using Django.

Technologies Used
Python 3.7.4
Django 1.11.23
SQLite3
HTML5
CSS3
Javascript
jQuery 3.4.1
Bootstrap 4.3.1
Owl carousel 2.3.4
Baguettebox.js 1.10.0
Google Font API

Requirements
This program requires python3.+ (and pip) installed, a guide on how to install python on various platforms can be found here
Once python is installed, install the folowing external libraries provided in the requirements.txt file using pip
Example:
pip install django==1.11.23
This project requires you to have a secret key from Uploadcare to facilitate cloud storage of uploaded images.
The secret key can be gotten by creating a free uploadcare account, starting a new project and navigating to the dashboard
The key should be stored as an environmental variable in an .env file as shown below
SECRET=<your secret key here>

* Installation and Set-up

To view the app, open the live site link provided below on the README. Here is a run through of how to set up the application:

* Step 1 : Clone this repository using git clone https://github.com/Wambuilucy/-Urban-Gallery, or downloading a ZIP file of the code.
* Step 2 : The repository, if downloaded as a .zip file will need to be extracted to your preferred location and opened
* Step 3 : Go to the project root directory and install the virtualenv library using pip an afterwards create a virtual environment. Run the following commands respectively:
pip install virtualenv
virtualenv venv
source venv/bin/activate
Note that you can exit the virtual environment by running the command deactivate
* Step 4 : Download the all dependencies in the requirements.txt using pip install -r requirements.txt
* Step 5 : You can now launch the application locally by running the command python manage.py runserver and copying the link given on the termnal on your browser.
To post photos, run the command python manage.py createsuperuser to create an admin account in order to post. Access to the admin panel is by adding the path /admin to the address bar.
Known Bugs
None at the momment, report any by contacting me
Support and contact details
You can provide feedback or raise any issues/ bugs through the following means:



* MIT License
License MIT Copyright (c) 2022 Brian otieno Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

