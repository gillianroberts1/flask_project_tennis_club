#### BRIEF

I have been asked by a new local tennis club to design a booking system to keep track of all members and courts.


#### MVP

* The app should allow the user to create and edit courts
* It should allow the user to create and edit members
* it should allow the user to book members onto courts
* it should allow the user to view all bookings, by member, by court and view all.

#### Extensions
 
 * Courts should have a maximum capacity (singles and doubles) and additional users    can only be added whilst there are spaces remaining
 * the club could be able to give members premium or standard membership. 
 * memberships should be able to be upgraded or downgraded.
 * add more details about member, address, dob, contact details

#### Advanced Extensions
* create time slots for each court
* Standard members can only be signed up for off peak courts. 
* add ability to rent out equipment such as racquets and balls 
* add profile photo of each member
* allow court to be booked for one hour or two hours
* be able to record the winner of each match
* The club could mark its members as acitive/deactivated. Deactivated members will not show in the create bookings.

#### Set Up

## Requires - Flask, Python3, PostgreSQL to run.

1. In the terminal, create db tennis_club on psql
2. in the terminal, psql -d tennis_club -f db/tennis_club.sql
3. In the terminal, psql -d tennis_club to connect to db   (quit to exit)
3. In new terminal - python3 console.py   (ctrl+ d to exit)
4. in new terminal - flask run - open link to port 4999  (ctrl +c to exit)




#### Learnings
 
1. The importance of fully understanding what tables will be required at the start.
to achieve my advanced extensions, i should have had another table for members_courts. This would have allowed me to add several members to a court and then add that court to the booking. Currently, although i can add up to 4 members to a court, the back end creates 4 seperate booking ids. This also gave me an issue when viewing courts booked.

However, DISTINCT sql in the court repository allowed me prevent the court from creating duplicate entries when booking more than one member on. It was technically a hack and i would in future make a seperate table.

2. Booking more than one member onto a court and limiting no of members per court depending on whether is was a singles or doubles or game - i handled this initially in html, creating a form with a conditional statement, meaning that if singles was selected then it would present a placeholder to select 2 members. If doubles was selected then 4 members could be selected. I then had to manage the rendering of this in the controller as it didnt know how to deal with it otherwise. I added further python logic to this as a work aorund along side the html.

3. CSS - although an after thought, i have learned that i need to set up my html better with more thought through approach to style things such as buttons, forms etc in more consistent way avoiding repeat code.



#### Process

1. Brief - this allowed me to gather my thoughts on what i wanted my app to do. I found myself going back to update it when i had a new idea, adding them to the extensions.
2. All class, object, wireframe and site map diagrams were set up.
3. Models completed, followed by the  3 tables.
4. I created the console.py and entered some test data based on my models.
5. I wrote the repositories for members and courts, testing each function using pdb
6. This was followed by the controllers and html as I wanted to see this working before setting up the foreign table - bookings.
7. I then set up the foreign table, created some more test data along with the repository and carried out further testing of each function.
8. The html for this was created along with the bookings controller.
9. At this point, i realised i was only able to add one member to a booking. I also wanted to add time slots for each court.
10. I researched how i would do this and was presented with a couple of options. I could make a new table for member-courts and a new table for slots. Or i could try to manage the extra members within html and only have one extra table for slots. 
11. i decided to on one extra table - slots. I created the table and model.
12. the test test data in the console proved difficult and took more time tan i coudl afford. However i got it working to a degree and the table linked up. 
13. This required me to change my controller and some of the many many to functiosn within the court and member repository no longer worked.
13. i then worked on html to provide the drop down box for slots which wasnt working correctly.
14. After speaking with the instructors, it was agreed that slots were not required for this project and it may prove too dufficult, so the app was returned to its original workign state with 3 tables.
15. I then worked on adding more members to a booking, limiting how many members can be booked on to a court, and also preventing a court from being booked if it was already booked.
16. this was handled with jinja and the controller - albeit not a perfect solution sql wise as mentioned in the Learnings section of this brief.
17. i wanted to show courts booked via the members show, i wanted to show what members were booked via the courts show. I also wanted to show if a court was available and if it was then it could also be booked via courts. I added a link to redirect to the new bookings. 
18. I wanted to show an option to book singles or doubles. I had to create an additional html page to do this and then move onto the next page to select members for singles or doubles.
19. CSS - i covered the home page first of all as i wanted the nav options to be part of the body. I found an image that i wanted to use the background. This then allowed me to decide on colour palette and also gave me an idea for the nav links to llok like tennis balls and to zoom when hovered over. 
20. I sampled the colours from image using colour picker extension on dev tools, and created a logo using this palette. As the home page was dark, i learned how to remove the background colour, whilst keeping the theme.
21. I found images for court surfaces and set the app up so that when a new court was added, it would automatically select the correct image.








