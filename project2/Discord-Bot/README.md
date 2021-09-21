Name: Patrick Mujambere
Course: CEG-3120
Lab: Project 2

			In the Discord-Bot folder, add a README.md file. Document the following:

						Setup

					how to get an API

API is under OAuth2 (after creating a server, you head back to the “Developer Portal” 
and select the OAuth2 from navigation. From that window you will see the OAuth2 URL Generator
which generates API  

				where to put it to work with the code

into browser

				dependencies (what packages need to be installed to run the code)

discord.py (which is a python library)
dotenv (is also library which loads environment variable from a .env file )
 
						Usage

				with your changes to the code in place, describe

Code looks good. I didn’t make a lot of changes in my code besides adding a few string, change quote massage 
and adding a new environment variable in the file called .env where my bot token and my guild name are located. 

			what commands you can type in your Discord server

fun! (for display fun quote)

favority! (for display some of my favority quote)

Notice: make sure those two words  “fun! and a favority!” Are in lowercase 

				what response this will provide (from your bot)

fun! Will respond one randomly quote from  my_favority_quotes (which I happen to have 4 quotes)

favority! Will respond randomly quote from  fun_quotes (there  are 4 quotes to choice from)

					Research

you may have realized that it is lame that it only runs when you run the program.In the real world, 
things are "always on", not waiting for Bob to turn his PC on and make sure the program is running.
Research some possible solutions that would solve this, and discuss why you think it would work.

There is some possible way to run the server without connection, 
one is to use screen or tmux. Another option is running the server as a service/daemon
(doemon is Unix/Linux program that executes in the background ready to perform an operation when required), 
the reason I think they will work is because screen and tmux keep programs and 
scripts running even when the network get disrupted

