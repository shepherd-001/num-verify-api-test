# NumVerify API Test Documentation

This project tests the NumVerify API (a public API that helps you validate phone number

at the point of entry into your system).   

### System Requirements
  - Python: 3.5 or latest
  - IDE (VSCode or Pycharm)
  - Git for version control
  - Internet connection to make request to the NumVerify API endpoint.
  
### Clone the repository
  - Type the following command on your system terminal to clone the repo:
  ```bash
   git clone https://github.com/shepherd-001/num-verify-api-test
  ```
Enter the project directory
  ```bash
   cd <repo-directory>
  ```
  
### Install dependencies
  - Run the following command to install the dependencies required for the project:
  ```bash
   npm install -r requirements.txt
  ```
  
### Set up environment variables
  - Create a .env file in the project root directory.
  - Add the NumVerify base url as a variable
  - Click [here](https://numverify.com/) to get an access key from the NumVerify API site.
  - Add the access_key as a variable in the .env file. 
  
### To run the test,
  - Run the following command on your terminal: 
  ```bash
    python -m python -m pytest ./tests/
  ```
  - The above command will execute all the tests in the project as predefined without 
generating a test report. To generate a test report, run: 
  ```bash
   python -m python -m pytest ./tests/
  ```
  - The result of the test can be found in report.html file.