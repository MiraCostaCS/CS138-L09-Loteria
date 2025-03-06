# Loteria

_Learning Objective: Demonstrate list manipulation and file output._

## Introduction:
Loteria is a game of chance that is extremely popular within hispanic households. The game originated in Italy but eventually traveled to Latin America in the 18th century where it was cemented into Mexican tradition.

[Watch this video about Loteria](https://youtu.be/QbAuUVe0W9c?si=EEvrw__MGePcL7B4)

To play Loteria, each player has a **tabla** that contains different arrangements of named drawings in Spanish. One player is chosen as the cantor (caller). This person randomly chooses from a deck of cards and calls out the name of the card. Once the card is called players must search for this card on their tabla, if they have the symbol it is traditional to place a raw bean on top of this symbol to show that you have the card called. To win Loteria you must fill your entire tabla, once you have accomplished this you call out “Loteria!”.

This week we will be working with lists from a file. This lab will focus on creating a program that creates Loteria tabla and calls on random cards from the list.

Step 1: Create list from file
------------------------------

You are provided a function to create a list from a file. This file contains every name from a traditional Loteria deck of cards. Call the function in your main program to create your deck of cards.

Step 2: Replace problematic names
---------------------------------

Throughout Loteria's journey to Mexico the symbols in the deck and their significance have changed frequently depending on the culture of the people playing but the most well known deck was created by Don Clemente who lived in Querétaro, Mexico. However, there are symbols that could be offensive and need to be changed. For this step write Python code to replace the following names on the list with the given replacements.

*   El Barracho → El cantante
*   El Apache → El caléndulas
*   El Negrito → El bailarín

Do **not** change the LoteriaList.csv file.

_hint_: Use a list comprehension for each name you want to replace.

Step 3: Create tabla
--------------------

Now it is time to make ten tablas (game boards). Each one should have a 4x4 grid of 16 distinct random names from the loteria list. Each one should also be saved in its own file. To make this more modular and decompose the problem a bit, start by writing a function that generates **one** 4x4 game tabla of distinct random elements of the given list. The function must write the tabla to the given file name.

There is an example tabla in the files on the left so you can see out to format the output.

_Hint_: use the `sample` method from the [Random](https://docs.python.org/3/library/random.html) library to get your 16 names.

In `main`, call the function to create 10 tabla, each saved in a unique file.

Step 4: Play game
-----------------

The last step of this lab is to write the code for game play. Your program should randomly call one card from the deck. Prompt the user to choose to select another random card or to exit the program. Ensure that once a card is called, the name will not be repeated. If the user chooses to exit, write the final message “Thank you for playing!” and end the program.

Submit
------

There are no automatic tests for this lab, so submit when you believe you are done or when ready for feedback.