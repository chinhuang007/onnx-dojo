# Git Hands-on Unit 1: Overview and Setup 

Goal of unit 1: At the end of unit 1, you will learn git, github, repo, and setup your git environment for remaining labs

1.1 Install git
    - ``` sudo apt install git ``` 
    - Verify ``` git --help ```

2. Identify the potential TensorFlow operator to support the new changes in Constant-12
    - https://www.tensorflow.org/api_docs/python/tf/constant

3. Create your PR development workspace

4. Create a branch under your fork as your development workspace
    ```
    git checkout -b <your-branch-name>
    git branch
    ```
5. Use your branch to build onnx-tf
    ```
    pip install -e .
    pip list | grep onnx-tf
    ```
6. Update test_constant unit test in onnx-tensorflow/test/backend/test_node.py
    ```
    cd onnx-tensorflow/test/backend
    vi test_node.py
    # When you are ready to test run your updated test_constant run the following
    # command
    python test_node.py TestNode.test_constant
    ```
13. Wait for review and address comment

      - If changes is required in your PR, modify code in your branch then run the
    following git commands
        ```
        git status
        git add *
        git commit --amend
        git push -f origin <your-branch-name>
        ```
      - If rebase is required, then run the following git commands
        ```
        git stash # if there is uncommitted changes on the current branch then stash it else skip to next step
        git fetch upstream
        git checkout master 
        git merge upstream/master
        git push origin master
        git checkout <your-branch-name>
        git rebase origin/master
        git stash pop # if there is a stash then pop it now else skip to next step
        git commit --amend # if there is no change to the commit then skip to next step
        git show -1
        git push -f origin <your-branch-name>
        ```
