# Design doc for Grocery List

I am going to create a program that curates a list of grocery items and tracks which user added the items to help keep track of each person's items.

- Be able to clearly tell who added which items to the list

- Not allow duplicates of items in list

- Repeat back entire list once user is ready to shop

### First Part: 
The items to be included in the list:
- users 
- specified grocery item
- quantity of specified items

Create a class to identify these items

### Second Part:
#### The empty list:

create an empty list that follows the class for the items and is on standby for user input

### Third Part:
Create a main area where all the seperate parts can be combined to help the list run

#### In this section include:

#### Requests:
- add to the list (y/n)
- enter name
- enter grocery item
- enter quantity of items

#### Duplicate Checker:
- use if/else statements to determine whether item has already been added to list
- inform user item has already been added and reapply original prompt
- if item is new add item and confirm item addition to list

#### Complete List:
- completely print entire list after while function has ended
- include the user, item, and quantity for each piece of the list printed



