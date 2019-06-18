Name: Andrew Myers
UTA EID: 100116613
Email: andrew.myers@mavs.uta.edu
Department: Department of Physics
University: The University of Texas at Arlington
Level: graduate Junior (3rd year)
MAPCP-Class Title: Student
Course Webpage: https://www.cdslab.org/MAPCP2019U/

Commands for First Homework:
Andrew@Andrew-PC MINGW64 ~/PhysicsClass_Summer2019 (master)
$ git add homework/
warning: LF will be replaced by CRLF in homework/1/readme.md.
The file will have its original line endings in your working directory.

Andrew@Andrew-PC MINGW64 ~/PhysicsClass_Summer2019 (master)
$ git commit -m "commit readme.md"
[master (root-commit) 16f0b62] commit readme.md
 1 file changed, 8 insertions(+)
 create mode 100644 homework/1/readme.md

Andrew@Andrew-PC MINGW64 ~/PhysicsClass_Summer2019 (master)
$ git branch test1

Andrew@Andrew-PC MINGW64 ~/PhysicsClass_Summer2019 (master)
$ git branch test2

Andrew@Andrew-PC MINGW64 ~/PhysicsClass_Summer2019 (master)
$ git branch
* master
  test1
  test2

Andrew@Andrew-PC MINGW64 ~/PhysicsClass_Summer2019 (master)
$ git checkout test1
Switched to branch 'test1'

Andrew@Andrew-PC MINGW64 ~/PhysicsClass_Summer2019 (test1)
$ touch homework/1/test.txt

Andrew@Andrew-PC MINGW64 ~/PhysicsClass_Summer2019 (test1)
$ vi homework/1/test.txt

Andrew@Andrew-PC MINGW64 ~/PhysicsClass_Summer2019 (test1)
$ git add homework/1/test.txt
warning: LF will be replaced by CRLF in homework/1/test.txt.
The file will have its original line endings in your working directory.

Andrew@Andrew-PC MINGW64 ~/PhysicsClass_Summer2019 (test1)
$ git commit -m "Commit on branch test1"
[test1 fb5b321] Commit on branch test1
 1 file changed, 1 insertion(+)
 create mode 100644 homework/1/test.txt

Andrew@Andrew-PC MINGW64 ~/PhysicsClass_Summer2019 (test1)
$ git checkout test2
Switched to branch 'test2'

Andrew@Andrew-PC MINGW64 ~/PhysicsClass_Summer2019 (test2)
$ ls homework/1/
readme.md

# I don't see the text file anymore because that file is specific to the test1 branch

Andrew@Andrew-PC MINGW64 ~/PhysicsClass_Summer2019 (test2)
$ touch homework/1/text.txt

Andrew@Andrew-PC MINGW64 ~/PhysicsClass_Summer2019 (test2)
$ vi homework/1/text.txt

Andrew@Andrew-PC MINGW64 ~/PhysicsClass_Summer2019 (test2)
$ git checkout test1
Switched to branch 'test1'

# Did not see an error message

Andrew@Andrew-PC MINGW64 ~/PhysicsClass_Summer2019 (test1)
$ git checkout master
Switched to branch 'master'

Andrew@Andrew-PC MINGW64 ~/PhysicsClass_Summer2019 (master)
$ git merge test1
Updating 16f0b62..fb5b321
Fast-forward
 homework/1/test.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 homework/1/test.txt

Andrew@Andrew-PC MINGW64 ~/PhysicsClass_Summer2019 (master)
$ ls homework/1/
readme.md  test.txt  text.txt

Andrew@Andrew-PC MINGW64 ~/PhysicsClass_Summer2019 (master)
$ git merge test2
Already up to date.

#Did not get a warning or error message.  Just a message saying up to date

Andrew@Andrew-PC MINGW64 ~/PhysicsClass_Summer2019 (master)
$ git checkout test2
Switched to branch 'test2'

#I was able to switch to test2

Andrew@Andrew-PC MINGW64 ~/PhysicsClass_Summer2019 (test2)
$ git status
On branch test2
Untracked files:
  (use "git add <file>..." to include in what will be committed)

        homework/1/text.txt

nothing added to commit but untracked files present (use "git add" to track)

Andrew@Andrew-PC MINGW64 ~/PhysicsClass_Summer2019 (test2)
$ vi homework/1/text.txt

Andrew@Andrew-PC MINGW64 ~/PhysicsClass_Summer2019 (test2)
$ git status
On branch test2
Untracked files:
  (use "git add <file>..." to include in what will be committed)

        homework/1/text.txt

nothing added to commit but untracked files present (use "git add" to track)

Andrew@Andrew-PC MINGW64 ~/PhysicsClass_Summer2019 (test2)
$ git add homework/1/text.txt
warning: LF will be replaced by CRLF in homework/1/text.txt.
The file will have its original line endings in your working directory.

Andrew@Andrew-PC MINGW64 ~/PhysicsClass_Summer2019 (test2)
$ git commit
[test2 a6076a3]  On branch test2  Changes to be committed:      new file:   homework/1/text.txt
 1 file changed, 1 insertion(+)
 create mode 100644 homework/1/text.txt

Andrew@Andrew-PC MINGW64 ~/PhysicsClass_Summer2019 (test2)
$ git branch -D test1
Deleted branch test1 (was fb5b321).

#I was able to delete it

Andrew@Andrew-PC MINGW64 ~/PhysicsClass_Summer2019 (test2)
$ git checkout master
Switched to branch 'master'

Andrew@Andrew-PC MINGW64 ~/PhysicsClass_Summer2019 (master)
$ git branch
* master
  test2
# I was able to delete it so I'm sure why I'm not getting the error messeages

Andrew@Andrew-PC MINGW64 ~/PhysicsClass_Summer2019 (master)
$ git checkout test2
Switched to branch 'test2'

Andrew@Andrew-PC MINGW64 ~/PhysicsClass_Summer2019 (test2)
$ git branch -D test2
error: Cannot delete branch 'test2' checked out at 'C:/Users/Andrew/PhysicsClass_Summer2019'

Andrew@Andrew-PC MINGW64 ~/PhysicsClass_Summer2019 (test2)
$ git checkout master
Switched to branch 'master'

Andrew@Andrew-PC MINGW64 ~/PhysicsClass_Summer2019 (master)
$ git branch -D test2
Deleted branch test2 (was a6076a3).

Andrew@Andrew-PC MINGW64 ~/PhysicsClass_Summer2019 (master)
$ git add homework/1/test.txt

Andrew@Andrew-PC MINGW64 ~/PhysicsClass_Summer2019 (master)
$ git commit
On branch master
nothing to commit, working tree clean
