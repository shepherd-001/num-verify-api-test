# NumVerify API Test Documentation

This project is designed to tests the **NumVerify API**, a public API that allows you to validate phone numbers at the point of entry into your system.   

at the point of entry into your system).

---

### System Requirements
  - **Python**: 3.5 or latest
  - **Code Editor or IDE**: VSCode or Pycharm
  - **Version Control**: Git
  - **Internet Connection**: to make request to the NumVerify API endpoint.

---
  
### Clone the Repository
  - To get started, clone the repository by running the following terminal in your terminal: 
  ```bash
   git clone https://github.com/shepherd-001/num-verify-api-test
   cd <repo-directory>  #Navigate to the project directory
  ```
---
  
### Install Dependencies
  -  Install the required dependencies by running:
  ```bash
    pip install -r requirements.txt
  ```

---

### Set Up Environment Variables
  - Create a .env file in the root directory of the project.
  - Add the NumVerify base URL as a variable in the .env file.
  - Obtain your access key from the [NumVerify API site.](https://numverify.com/)
  - Add the access key as a variable in the .env file. 
  

---

### To run the test,
To execute the tests, use the following command: 
  ```bash
    python -m python -m pytest ./tests/
  ```
  This will run all predefined tests in the project.

To generate a test report, use the following command instead:
  ```bash
   python -m python -m pytest ./tests/ --html-report.html
  ```
  The result will be saved in the report.html file.