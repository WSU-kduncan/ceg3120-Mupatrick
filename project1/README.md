                     CEG-3120 Project 1 

		Initialize git repository

	command: git init project1repo 
	this command will create a new repository "project1repo" including .git repository, workspace and some files to manipulate
		

		Create a user Account

	command: sudo adduser projectS
	-Enter password
	-Retype password
	-type y



			Permission 


	To see file permissions use commend : ls -lah ("ls" which allow us to list file and directory, 
	flags "lah" will force system to list all files and directory human can read even the hidden one)  

	and when you run command you will see somethings like -rwxrw-rw- or drwxrwxrwx
	if is starting with "-" character means is a file
	but if starting with "d" means is a directory, rwx are for permission

	r = read permission
	w = write permission
	x = execute permission
	– = no permission	 

	The first three letter is for the user or the own of the file, next three is for group and the last is for other

	Usage: of clone, add, commit, and push

	-git Clone is a repository into a new directory.

	- git add: Add file contents to the index.

	-git commit:is for Recording changes to the repository.

	-git push is for Update remote refs along with associated objects.

	-The last I also like to use "git status" whish show the working tree status  
