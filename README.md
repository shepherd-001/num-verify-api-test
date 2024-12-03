NumVerify API Test Documentation
- 
- System Requirement
  - Git for version control
  - IDE (vscode or pycharm)
  
- Clone the repository
  - type the following command on your pc to clone the repo: git clone https://github.com/shepherd-001/num-verify-api-test
  - cd <repo-directory>
  
- Install dependencies
  - Run the following command to install the dependencies required for the project: pip install - r requirements.txt
  
- Set up environment variables
  - Create a .env file and add the base url of the project as a variable
  - Get an access-key from the num-verify public api page and add it as another variable to the .env file.
  
- To run the test,
  - Type the following in you terminal: python -m python -m pytest ./tests/
  - The above command will execute all the tests in the project as predefined.
  - To generate the result, in a report.html file, run: python -m python -m pytest ./tests/
  - The result of the test can be found in report.html file.