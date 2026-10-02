 # Programming Project - "Dude, Where's my cat"

### Description

Dude Where's My Cat? is a text-based adventure game written in Python.

The player comes home after a long day of classes and discovers that their cat is missing. The goal of the game is to search the apartment, find the cat, get the cat settled, collect the player's Hot Cheetos and TV remote, and finally relax on the couch and watch their favorite show.

The cat's location is randomly selected when starting a new game, so the player may have to solve a different puzzle depending on where the cat is hiding.

### How to Play

At the beginning of a new game, the player enters:

Their name , if there is a save file with the same name it will load and not ask for age and cat name 
Their age
Their cat's name

The player must be at least 12 years old to play.

The player starts in the hallway and can choose from four main actions:

Search the room
Check your inventory
Go to another room
Quit and Save

The player can move between the different rooms in the apartment and search different locations for useful items.

### Game Objective

To win the game, the player must:

Find the missing cat.
Get the cat settled.
Find the Hot Cheetos.
Find the TV remote.
Return to the couch.
Turn on the TV and watch the show.

Once all requirements are completed, the game displays the YOU WIN! message.

The cat can be in 3 locations. the kitchen when you interact with the fridge , the bathroom when you interact with the sink or in the bedroom when you interact with the bed

### File descriptions

Main.py -  Contains the main game logic, menus, game progression, save/load system, and win condition.
items.py - Contains the Item class.
player.py - Contains the player class and inventory functions.
rooms.py - Contains the Room class, room movement, and room searching menus.
searchable.py - Contains the Searchable class used for searchable locations inside rooms.
savegame.json - Stores the player's saved game data.

### Libraries Used
-random,time,json,os,colorama


### Author
Created as a Python programming project.
Game: Dude Where's My Cat?
Language: Python
Name:Richard Nasef

### Possible improvments
 Update save system to have the ablity to save more than one file at a time
 seperate save functions onto its own file
 