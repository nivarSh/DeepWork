# Simple Productivity App
#### Video Demo: https://youtu.be/X5Au2fZ16tw
#### Description: Simple productivity system that has a timer and a to do list. Option to view your work session history (if you logged in)

---

#### Details
This app is run on Flask, SQLite3, HTML, CSS (Bootstrap), JavaScript (JINJA 2). App has a login/register feature to store data into each user. Password hashing has been implemented for security purposes. Once user has registered for an account their username and password(hash) has been stored in a SQLite3 database. To track which user is using the app in the browser, the app has imported sessions and is keeping track of the user. The reason the app has a user system is to track their study/work sessions over the entire course of their time using the app. Once logged/registered in the user is redirected to set a timer in a form. Then they are sent to a page where the timer is displayed and active. Additionally, that page has a feature to add tasks for your work session. The tasks will be displayed on that page alongside the timer. The user has the option to check off the tasks and to clear their task list. Once a work session has been completed a announcement/popup will appear congratulationing them and asking to "log" the session. Essentially, if that "log" button is pressed then the app will store the duration of the work session and the timestamp of when it was completed into a database. Finally, the user has the option to look at their total work session history of the entire period of using this app. This history page displays a table of that information. And of course the user has the option to log out.

---

#### Frontend Details
Starting off with styling, the app is implement in a dark mode with green accents. Bootstrap is being used to simplify announcements, buttons, and forms. Moving on to HTML/JavaScript, jinja 2.0 was a necessity for displaying backend information. JavaScript was used for the actual implementation of the timer and the events that happened after the time went off. A song plays when the timer goes off and an announcement shows up to log the session. Lastly, JS was used for creating the checkmark feature on the tasks.

---

#### Backend Details
Once a user has registered/logged in the app immediately takes note of their user id and tracks it as they use the browser. This is necessary for finding the exact information to display in the history tab of the website. In addition to tracking the user id by sessions the app also temporarily tracks the current duration of the work session they selected. The reason the app tracks the duration is so it is easier to redirect to different pages while passing that information. The tasks are stored in a python list and are not linked/stored with the user. In total the app has a database with two tables: users and history. 

---

#### Additional Notes:
I was purposefully avoiding diving deep in AJAX and Javascript because it seemed like a large jump.
So I made a v1 of my website just basic functionality. In the future I want to improve this app by 
adding AJAX to dynamically do things with having to redirect pages.