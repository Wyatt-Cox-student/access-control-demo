Project Description

This is a basic Python program that is meant to demonstrate authentication, user roles, and access control. The program uses hardcoded usernames and assigns each username a specific role.

The program has two hardcoded users:

admin_user has the admin role
regular_user has the user role

When the program runs, it checks the username and finds the role connected to that user. The role then decides which part of the program they are allowed to access.

How Access Works

There are two protected actions in the program.

The admin_action() function is only for the admin role, while the user_action() function is only for the regular user role.

If someone tries to use an action that does not match their role, the program gives them an "Access denied" message. For example, a regular user will not be able to open the admin area.

CIA Triad

This program mainly shows Confidentiality, which is one part of the CIA triad.

Confidentiality is about making sure people can only access information or areas they are supposed to have access to. In this program, the user's role controls what they can open. This keeps a regular user from getting into the admin section.


In order to use this, please make sure Python is installed, and then run:

python app.py

You can test the admin account by using:

current_username = "admin_user"

You can also test the regular user by changing it to:

current_username = "regular_user"

Run the program again and you should see that each role has different access.
