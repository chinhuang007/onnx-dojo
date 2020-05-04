# Update Constant handler to support opset 12

1. Study the specification of Constant in ONNX to identify changes in opset 12
    - Compare Constant-12 with Constant-11
    - https://github.com/onnx/onnx/blob/master/docs/Operators.md#Constant
    - https://github.com/onnx/onnx/blob/master/docs/Changelog.md#Constant-11

2. Identify the potential TensorFlow operator to support the new changes in Constant-12
    - https://www.tensorflow.org/api_docs/python/tf/constant

3. Create your PR development workspace

    - Verify your ONNX package location is point to your ONNX directory not to an egg file
      ```
      pip list | grep onnx
      # If the location is point to an egg file, then please reinstall it by the
      # following commands
      cd <your-onnx-directory>
      pip install -e .
      ```
    - If you didn’t create a fork of ONNX-Tensorflow yet, please create one by go
  to https://github.com/onnx/onnx-tensorflow and click the “fork” button on the
  top right corner
    - Clone your fork
      ```
      git clone https://github.com/<your-git-user-name>/onnx-tensorflow.git
      cd onnx-tensorflow ; ls
      ```
    - Setup the upstream remote
      ```
      git remote add upstream https://github.com/onnx/onnx-tensorflow.git
      git remote -v
      ```
    - Verify your fork master is up-to-date
      ```
      git checkout master
      # If your master is out-of-date then run the following commands
      git fetch upstream
      git merge upstream/master
      git push origin master
      ```
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
7. Update Constant handler in onnx-tensorflow/onnx_tf/handlers/backend/constant.py

    - Edit constant.py
      ```
      cd ../../ onnx_tf/handlers/backend
      vi constant.py
      ```
    - When you are ready to test your handler, please register your updated handler
  to onnx-tensorlfow/onnx_tf/opset_version.py by the following command
      ```
      python ../../gen_opset.py
      cat ../../opset_version.py | grep Constant
      ```
    - Test/debug your updated handler by running your updated Constant unit test
  in onnx-tensorflow/test/backend/TestNode.py on step 6
      ```
      python ../../../test/backend/test_node.py TestNode.test_constant
      ```
8. After successfully run the unit test of Constant in test_node.py then please
verify all the other tests under onnx-tensorlfow/test/backend folder are pass
too.
    ```
    cd ../../../test/backend
    python test_node.py
    python test_dynamic_shape.py
    python test_model.py
    python test_onnx_backend.py
    cd ../
    python test_cli.py
    ```
9. Update support status report for Constant
    ```
    cd ../../onnx_tf
    python gen_status.py –v master
    cat ../doc/support_status.md | grep Constant
    ```
10. Verify all changed files follow the recommended code format on
    https://github.com/onnx/onnx-tensorflow#code-standard
11. Commit all the changes to your branch in your fork
    ```
    git status
    git add *
    git commit
    git push origin <your-branch-name>
    ```
12. Create Pull Request(PR) in ONNX-Tensorflow Repository
  - Navigate your browser to https://github.com/onnx/onnx-tensorflow
  - Click on the “Compare and pull request” button
  - Click on the “Create pull request“ button
  - Type a title and description of your pull request
  - Click on the “Create pull request“ button to submit it
  - Note:  If you can’t find the “Compare and pull request” button then run the
  following steps:
      - Click on the “Pull requests” tab on the top of the page
      - Click on the “New pull request” button
      - Click on the “compare across forks” link
      - Leave the base repo as the master branch and change the head repo to
      your fork and your branch
      - Click on the “Create pull request“ button
      - Type a title and description of your pull request
      - Click on the “Create pull request“ button to submit it
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
