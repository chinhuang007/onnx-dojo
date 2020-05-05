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

    - Next create a commit
        - ``` git commit ```
        - You should be in the editor you specified earlier.
        - The first line is the commit title, such as “Add John Doe”.
        - Put an empty line and the text below will be the commit message, describing why the commit exists
        - Once done exit the editor with a normal save and exit        
    - Check branch status. ``` git status ``` should show you are on your branch with nothing to commit
4. Push up a commit
    - Now you need to push the commit up to the remote repo.
        ```
        git push origin add-your-name-profile        
        ```
    - Enter your git user name and password when prompted
    - Check your commit is pushed up and ready for a pull request
        - In a browser, go to https://github.com/chinhuang007/onnx-dojo and your branch should appear as ready for a pull request
        - Next go to https://github.com/<user-rname>/onnx-dojo and click on Branch: master and switch to “add-your-name-profile” branch
        - Navigate to profiles folder and your newly added file should be there

    
# Git Hands-on Unit 4: Create and merge pull request

Goal of unit 4: At the end of unit 4, you will learn how to create, review and merge a pull request

1. Create a pull request
    - In a browser, go to https://github.com/chinhuang007/onnx-dojo and click “compare & pull request” button for your branch
    - You could add more detailed message, screen shots, links to issues and other PRs. Let's add a person mention so he/she will get an email notification for the change.
    - Type ‘@chinhuang007 Check this out” in the text field.
    - Click “Create pull request” button.
    - Verify: The pull request is created. Notification is sent to the person you specified earlier. If there is Continuous Integration (CI) configured for the repo, CI tasks will be run (not in this example).
    - Verify: You should see “This branch has no conflicts with the base branch”.
2. Review a pull request (instructors walk-through)
    - In a browser, go to https://github.com/chinhuang007/onnx-dojo and click “Pull Requests” tab.
    - Find the pull request with title “Add John Doe”
    - Associate with an issue (need permissions)
    - Review the changes and run tests if needed
    - Leave a comment
    - Provide final review and approval (need permissions)
    - Verify: The pull request has one approval.
    - Verify: The “merge pull request” button is green for the users with merge permissions.
3. Merge a pull request (instructors walk-through)
    - Click “Merge Pull Request”
    - Click “Confirm Merge”
    - Verify: The pull request status is changed from “Open” to “Closed”
    - Verify: The associated issue is also changed from “Open” to “Closed”
    - Verify: The repo is updated with the changes.
4. Delete working branch and rebase master (optional)
    - Once a pull request is merged, the working branch can be deleted.
      ```
      git checkout master
      git branch -D add-your-name-profile
      ```
    - Verify: ``` git branch ``` should show master only
    - You can delete the remote branch from UI, either from upstream or your repo
    - Rebase your master branch so you are in sync with upstream master.
      ```
      git fetch upstream
      git rebase upstream/master
      git push origin master
      ```
    - Enter your git user name and password when prompted
    - Your remote repo master should be updated now.
    - Verify: go to https://github.com/<user-name>/onnx-dojo and check your master branch is even with upstream master
    - Verify: navigate through https://github.com/<user-name>/onnx-dojo to see the latest contents
    - Now you are good to go, working on next PR!
