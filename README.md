# Final Project for Course "Programming in Data Science" UPM 2nd Semester 2024
Members:
 - Sigrid Festoy
 - Sebastian Montenius
 - Yu Xindi
 - Huang Tongyi
 - Moritz Trieu

 Python Version: 3.11.4

Further documentation and results, not contained in this repo can be found under:
https://docs.google.com/document/d/16j4VfSlvhqssUdWIX4S-B2k7sDmYypXg7qdXDZHerwY/edit?usp=sharing

# Coding Rules and VS Code Tips
## Documentation Guidelines
Every module, class, function, etc. should have a docstring where sensible (e.g. not for obvious setter, getter functions)
Docstring format is the **Google** style: https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings
Use autogen tools for docstring creation where possible (e.g. autoDocstring).
## Cooperation Guidelines
The main branch is locked, meaning nobody can push changes directly to the main branch. This is done so no unreviewed code can break the stable code base.
In order to change the code:
1. Branch of the main branch. You can either
    - Create an indiviual branch for each task (e.g. mtr_working_scrape-class)
    - Create one working branch which you will sync with the main branch on a regular bases (e.g mtr_working)
2. Create your changes in your local repo, commit and push your working branch to the remote repo (GitHub)
3. Once your remote branch has been pushed, you can create a pull request on GitHub. Detail your changes and create PR.
Currently the PR has to be approved by at least one person and the code owner (@Moritz). The last step is only to make sure everything is ok in the beginning and is subject to change later so you can merge w/o me. 
Once your PR is requested, ping the group to request a code review. Everybody that wants to can clone your working branch and leave commments on the PR. If any changes have to be made, make them on your local working branch and push them to remote, they will automaticially be included in your PR. Once approved my enough people (or code owner), you can merge the branch to main, where you potentially have to resolve merge conflicts,
4. Once merged don't forget to either create a new working branch or sync your current one (see 1.)

## Coding "Styleguide"
Good reference for coding/ Python style guide: https://google.github.io/styleguide/pyguide.html (if you want further information)
Most important: Respect naming style, keep your code legible by using white spaces, keep your code abstract/ maintainable by refactoring where possible.

## Useful VS Code Add-Ons
- Python and Jupyter
- autoDocstring: Automatic Docstring generation when typing """ . Make sure to configure docstring format "google"
- Black Formatter: Auto formats your code. Configure: Editor: Default Formatter: Black Formatter, Editor: Format on Save, Editor: Format on Save mode, Black-formmater: args: --line-length 80
- Pylance: Linter for Python, displays potential problems

# Git Setup and Workflow
If you are not comfortable with git, you can use visual tools such as GitKraken, GitLens or even the default VS Code source control tool
## Git/ Github Setup, Cloning
In order to be able to push to the repo, you will need to add an SSH key to your GitHub account.
Refer to 
- https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
- https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account

Clone the main branch into your working folder by 
 - git clone git@github.com:motrieu/prog-data-sci.git 

You might need to configure your git with name and email by 
 - git config --global user.name "John Doe"
 - git config --global user.email johndoe@example.com
## Branching, Commiting, Pushing
Create a branch from main by
- git branch new-branch-name

Use
 - git checkout new-branch-name

to start working on the new branch
Commit with
 - git status
 - git add file-names
 - git commit

Keep your commits granular, keep your commit titles short. If you need more detail you can write that in the commit msg body.
Once your done with your local changes you can push to remote by

 - git push origin branch-name
## Creating Pull Requests

# Venv/ Python Packages
Venv is a python tool to create virtual python environments. This is useful to have multiple python instances, for example you can install all required packages for this project (which could potentially be large) w/o trashing your systems python instance and slowing it down. For us it is also helpful to have a common environment so our code runs reliably on every machine.

There is a venv folder in the repo, containing the entire python instance (a bit expensive but simpler for our purposes).

Make sure your VS code interpreter is set to this python bin. If you use the command line make sure to activate the environment before running any python operations by
- Linux/ Mac: ./venv/scripts/activate
- Win: ./venv/scripts/Activate.ps1

If you install any new packages, make sure to push the venv folder as well and detail new packages in PR
