# CITS5505Project2
## Introduction
0 We made a responsive and easy-use website for the Sudoku game to complete the CITS5505 project 2. We built 6 pages: Intro page(main page), game page, ranking page, log in, and sign up page, respectively. We use HTML, CSS, Flask, AJAX, JQuery, and Bootstrap. Also, there is not any additional technology applied. For the color scheme,  we use light purple, blue, and white as our primary colors and other similar additional colors.
1.1 Intro page
There are three main parts to the intro page: the title part aims to distribute the purpose of our website and make the website attractive at first glance. The part right below the title is the advantages of the Sudoku game, which promotes the theme and the positive words to users. The last part is for explaining the rules of the Sudoku game.

1.2 game page
 There are two main parts for this section: the board on the left-hand side and the other is the start and submit button for the game on the right side. Also, the user can check the result of the wrong steps in the right section. In addition, our design is that the user must log in to get access to the game page, or this page will display the login page instead.
1.3 ranking page: 
This page aims to show all users' results to give them feedback and create a competitive atmosphere to reserve long-term users.
1.4 login page
1.5 sign up page
1.6 Once a user logs in, the login and sign-up tag in the navbar should be placed by the log-out tag.
## How to set up

2.1 set up MySQL  
create a table named "cits5505", with charset utf8
```MySQL
CREATE SCHEMA `cits5505` DEFAULT CHARACTER SET utf8 ;
```
2.2. Configure your Mysql username and password in config.py
2.3. Database migrate  
```shell
flask db init
flask db migrate
flask db upgrade
```
After that, you will see some tables in your database.  
2.4. Run the application  
```shell
flask run
```
