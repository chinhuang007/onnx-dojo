# Git Hands-on Unit 1: Overview and setup 

Goal of unit 1: At the end of unit 1, you will learn git, github, repo, and setup your git environment for remaining labs

1. Install git
    - ``` sudo apt install git ``` 
    - Verify: ``` git --help ```
    
2. Configure git
    - Setup your user name and email
        ```
        git config --global user.name "John Doe"
        git config --global user.email johndoe@example.com
        ```
    - Setup a default text editor when git needs you to type in a message
        ```
        git config --global core.editor vi
        ```
    - Setup a push default option to simple
        ```
        git config --global push.default simple
        ```
    - Verify: ``` git config --list ```
        
# Git Hands-on Unit 2: Fork and clone ONNX-Dojo repo

Goal of unit 2: At the end of unit 2, you will learn the onnx-dojo repo and how to create a fork, clone, and setup an upstream

1. Fork the repo
    - In a browser, go to https://github.com/chinhuang007/onnx-dojo, and click ‘Fork’ on the upper right hand corner. When prompted, make the fork go to your user account.
    - Verify: Check in browser, you should have a repository https://github.com/<user-name>/onnx-dojo

2. Clone the repo
    - Clone repo to your local file system
        ```
        git clone https://github.com/<user-name>/onnx-dojo.git
        ```
    - Verify: a folder ‘onnx-dojo’ is created
    - Verify: the following should return 2 entries with URLs for your remote repository origin
        ```
        cd onnx-dojo
        git remote -v
        ```
3. Setup the upstream
    - Setup upstream repo
        ```
        git remote add upstream https://github.com/chinhuang007/onnx-dojo.git
        ```
    - Verify: the following should return 4 entries with 2 each for origin and upstream
        ```
        git remote -v
        ```   
      
# Git Hands-on Unit 3: Create branch and commit

Goal of unit 3: At the end of unit 3, you will learn how to create a branch, make changes, and push a commit

1. Create a branch
    - Check the current branch. ``` git branch ``` should show just the master branch
        
    - To make changes and later create commits, we need to create a local branch to work on.
        ```
        git checkout –b add-your-name-profile 
        ```
    - Verify: ``` git branch ``` should show two branches now and the active one with * mark

2. Create your profile
    - Create a file under profiles folder. You could use .md or simple text file.
    - Check branch status. ``` git status ``` should show you are on your branch with an untracked file
3. Create a commit
    - First need to add the changes to be committed.
        ```
        git add your-file-name        
        ```
    - Check branch status. ``` git status ``` should show a new file as changes to be committed

    - Next create a commit with ``` git status ```
        - You should be in the editor you specified earlier
        - The first line is the commit title, such as “Add John Doe”
        - Put an empty line and the text below will be the commit message, describing why the commit exists
        - Once done exit the editor with a normal exit and save
        
    - Check branch status. ``` git status ``` should show you are on your branch with nothing to commit
    
