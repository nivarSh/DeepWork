# Productivity App
#### Description: Productivity system that has a timer and a to-do list. Option to view your work session history (if you logged in) and data visualizations to view the user's study habits.

---

#### Details
This app is run on Flask, SQLite3, HTML, CSS (Bootstrap), and JavaScript (JINJA 2). App has a login/register feature to store data for each user. Password hashing has been implemented for security purposes. Once a user has registered for an account their username and (hashed) password have been stored in an SQLite3 database. To track which user is using the app in the browser, the app has imported sessions and keeps track of the user. The user system tracks their study/work sessions over the entire course of their time using the app. Once registered, the user is redirected to set a timer in a form. Then they are sent to a page where the timer is displayed and active. Additionally, that page has a feature to add tasks for your work session. The tasks will be displayed on that page alongside the timer. The user has the option to check off the tasks and to clear their task list. Once a work session has been completed an announcement/popup will appear congratulating them and asking them to "log" the session. Essentially, if that "log" button is pressed, the app will store the duration of the work session and the timestamp of when it was completed in a database. Finally, the user has the option to look at their total work session history for the entire period of using this app. This history page displays a table of that information. And of course, the user has the option to log out. Finally, the ZenQuotes.io API was accessed to display a quote of the day.

---

#### Frontend Details
Starting with styling, the app is implemented in a dark mode with green accents. Bootstrap is being used to simplify announcements, buttons, and forms. Moving on to HTML/JavaScript, jinja 2.0 was a necessity for displaying backend information. JavaScript was used for the implementation of the timer and the events that happened after the time went off. A song plays when the timer goes off and an announcement shows up to log the session. Lastly, JS was used to create the checkmark feature on the tasks.

---

#### Backend Details
Once a user has registered/logged in, the app immediately takes note of their user ID and tracks it as they use the browser. This is necessary for finding the exact information to display in the history tab of the website. In addition to tracking the user ID by sessions, the app also temporarily tracks the current duration of the work session they selected. The reason the app tracks the duration is so it is easier to redirect to different pages while passing that information. The tasks are stored in a Python list and are not linked/stored with the user. In total, the app has a database with two tables: users and history.

---
