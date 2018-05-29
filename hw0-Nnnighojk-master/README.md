Welcome to ECE 29595, Introduction to Data Science. In this course, we will cover a wide variety of topics related to data analysis -- histograms, estimation, regression, clustering, classificaiton, etc. -- all explored through writing Python programs to implement these analyses.

This first homework assignment will ask you to set up your environment correctly -- both the Python environment and the submission infrastructure that we will be using.

Goals
=====

In this assignment you will:
* Set up your GitHub account
* Use git to clone the homework 0 account
* Set up your Python environment
* Use git to submit your assignment

Background
==========

Version Control
---------------

This class uses git for version control. Git is a distributed version
control system. That means there are two repositories: local and
remote. When you commit changes, only the local repository is
changed. This makes commits fast and independent of network
connections.  If your computer is damaged, you still lose the local
repository. 

To change the remote repository, you need to push the changes.  If
your computer is damaged, you can retrieve the code from the remote
repository.

Please read the guide at github about how to use version control.

https://guides.github.com/

Please push your code to GitHub often. Not only does that prevent you from
losing any code if you accidentally delete anything, it helps us help you
debug, by giving us access to your latest code.

Python
------

We will use Python in this class to implement our various analyses. Python is
a scripting language that has extensive library support for data science, in
the form of the [SciPy](https://www.scipy.org) module stack: NumPy provides
many basic mathematical operations on lists and arrays of data; pandas
provides higher-level data structures that facilitate managing data sets;
Matplotlib is a library for simple visualizations of data; and IPython (plus
Jupyter) provides a way of using Python interactively.

In this class, we will use **python 2.7.10** (this is the version of python installed on the ecegrid machines). Many of the modules we will use in this class are already installed on the ecegrid machines, as well, but you can use the `pip` package manager to install the latest versions:

```
python -m pip install --user [package name]
```

Note that the `--user` flag installs the package locally (i.e., in your home directory). This is useful to install packages that might override the default packages on the ecegrid machines. If the package is already installed, you can also upgrade to the latest version:

```
python -m pip install --user --upgrade [package name]
```

The package versions that we will use in this class are:

* `scipy` version 1.0.0
* `numpy` version 1.14.0
* `pandas` version 0.22.0
* `matplotlib` version 2.1.1

These are the latest versions of these libraries. If you are using older
versions of these libraries during development, it is your responsibility to
ensure that your code works with the above versions.

You may also want to install Jupyter notebook (package name `jupyter`) -- this
will allow you to write python scripts interspersed with text and plots (in
later homeworks, we will expect a short writeup of your results in addition to
any code).

Python modules
--------------

Python does not have a large number of built-in commands. Instead, Python relies on a wide range of modules to provide additional functionality. These modules can be used in your script by `import`ing them (this is like using `#include` in C). For example, to import `numpy`, you would use the line:

```
import numpy as np
```

This tells Python two things: first, that you want to use the `numpy` module. Second, whenever you invoke methods of the `numpy` module, they will be part of the `np` "namespace" -- any functions will be preceded by `np`:

```
input = np.random.randint(0, 10, 100, 'i')
```

Will invoke the `random.randint` method from the `numpy` module.

Instructions
============

We recommend that you take these steps while logged in to an ecegrid machine
(from a terminal). If you want to work on your homework on a different
machine, you are free to, though you may have to slightly modify some of the
instructions below.

> If you have not logged in to ecegrid before, you can connect using
> [ThinLinc](https://ecegrid.ecn.purdue.edu/main/) from any web
> browser. You may be asked to choose a Gnome or KDE desktop (pick
> either).  From there, you can open a terminal window to execute these
> commands.


1) Set up your Github account
-----------------------------

Create a Github account (if you do not already have one). This is the account
you should use to create and submit all of your assignments this semester.

Fill out this [Google form](https://docs.google.com/forms/d/16KwyengTYr45q6nhKuIYqBB2OS38xo1_fAyvn_ZFzk8/edit) to let us link your GitHub username with your Purdue account.
  
2) Create a git repository for the assignment
---------------------------------------------

Make sure you are logged in to your GitHub account. On Blackboard, click on the HW0 GitHub Classroom link. This link will set up a repository for
homework 0 at `https://github.com/ECEDataScience/hw0-<your username here`. 
This repository contains starter code for your assignment (in this case, 
this README, plus the file `hw0.py`).
  
3) Set up an SSH key with GitHub
--------------------------------

Set up a public SSH key in your GitHub account (if you haven't already). To do this, first generate a new ssh key:
  
```
> ssh-keygen
```

Hit enter three times (to accept the default location, then to set and confirm an empty passphrase). This will create two files: `~/.ssh/id_rsa` (your private key) and `~/.ssh/id_rsa.pub` (your public key)

Then print out your public key:

```
> cat ~/.ssh/id_rsa.pub
```

And copy it to the clipboard. Then follow steps 2-8 [here](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/).
  
4) Clone the repository to develop your assignment
--------------------------------------------------

Cloning a repository creates a local copy. Change your directory to
whichever directory you want to create your local copy in, and type:

```
> git clone git@github.com:/ECEDataScience/hw0-<your username here> hw0
```

This will create a subdirectory called PA01, where you will work on your code. 

In this command: `git clone` copies a
repository. `git@github.com:/ECEDataScience/hw0-<your username here>`
tells `git` where the server (remote copy) of your code is. `hw0` tells
  git to place the code in a local directory named `hw0`

If you change to directory `hw0` and list the contents, you should see the
files you will need for this assignment:

```
> cd hw0
> ls
```

You should see `README.md` (this file) and `hw0.py`.
  
As you develop your code, you can commit a *local* version of your
changes (just to make sure that you can back up if you break
something) by typing:

```
> git add <file name that you want to commit>
> git commit -m "<describe your changes>"
```

`git add <filename>` tells git to "stage" a file for
committing. Staging files is useful if you want to make changes to
several files at once and treat them as one logical change to your
code.  You need to call git add every time you want to commit a file that you have changed.

`git commit` tells git to commit a new version of your code including
all the changes you staged with `git add`. Note that until you execute
`git commit`, none of your changes will have a version associated with
them.
  
To copy your changes back to Github (to make sure they are saved if
your computer crashes, or if you want to continue developing your code
from another machine), type

`> git push`

If you do not push, the teaching staff cannot see your solutions.
  
5) Write a simple test program to print out module version numbers
------------------------------------------------------------------

In this assignment, all you need to do is write a simple Python script that will print out the module version numbers for the modules we will be using in this course: `scipy`, `numpy`, `pandas`, and `matplotlib`.

To do this, you should import the module, then print the `__version__` variable. `hw0.py` shows how to do this for `numpy`:

```
import numpy as np

print np.__version__
```

You can run this program from the command line as follows:

```
> python hw0.py
```

What you need to submit
=======================

You should modify `hw0.py` to also print out the version numbers for `scipy`, `pandas`, and `matplotlib` (in that order) after the version number for `numpy`. This is the only file you need to create or modify for this assignment.

**Don't forget to push the updated version of `hw0.py` to GitHub!**

Submitting your code
====================

You will use git's "tagging" functionality to submit
assignments. Rather than using any submission system, you will use git
to *tag* which version of the code you want to grade. To tag the
latest version of the code, type:

`> git tag -a <tagname> -m "<describe the tag>"`

This will attach a tag with name <tagname> to your latest commit. Once
you have a version of your program that you want to submit, run the
following commands:

```
> git tag -a submission -m "Submission for hw0"
> git push --tags
```

This will create a tag named "submission" and push it to the remote server.
The grading system will check out *whichever* version you have tagged
"submission" and grade that.

If you want to update your submission (and tell the grading system to
ignore any previous submissions) type:

```
> git tag -a -f submission -m "Submission for hw0"
> git push --tags
```

This will overwrite any other tag named submission with one for the current
commit.

Please be careful about the following rules:

* For each assignment, you should tag only one version with
   "submission".  It is your responsibility to tag the correct
   one. You CANNOT request regrading if the grading program retrieves
   the version that you do not want to submit.

* After tagging a version "submission", any modifications you make to
   your program WILL NOT BE GRADED (unless you update the tag, as
   described above).

* The grading program starts retrieving soon after the submission
   deadline of each assignment.  If your repository has no version
   tagged "submission", it is considered that you are late.

* The time of submission is the time when you push the code to the
   repository, not the time when the grading program retrieves your
   code.  If you push the code after the deadline, it is late. Even though
   you push before the grading program starts retrieving your program,
   it is still considered late.

* You should push at least fifteen minutes before the deadline.  Give
   yourself some time to accommodate unexpected situations (such as
   slow networks).

* You are encouraged to tag partially working programs for submission
   early. In case anything occurs (for example, your computer is
   broken), you may receive some points.  Please remember to tag
   improved version as you make progress.

* Do not send your code for grading. The only acceptable way for
  grading is to tag your repository.
