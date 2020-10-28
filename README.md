# atbAssessment

Steps to follow to run and test the code:
Open any IDE of your choice or open CLI/Terminal on your local machine.
Clone the repository on the local machine by typing the command "git clone https://github.com/ashwani227/atbAssessment" or Users can directly enter the URL provided on the browser.
Transit from current directory to the location where new repo is downloaded.
Make sure you have Python3 installed in your system.
Go to the folder and type python3 semver_comparison.py and press enter. User will see a boolean result as True or False.
If user is using IDE then simply Run the semver_comparison.py file.
User can change the input in the main function which is Line 54 of semver_comparison.py file and observe the results.

Run Testcases:
For unittest, you have to use Conda environment in your machine.
Go to the IDE and look for file test_sem.py
Run the file from the IDE and observe the result. 
Please note, as per the description, all the semvers to be tested are valid semvers.
If the user wants to run multiple tests and check if the program is performing appropriately, please route to the sample_input.py file and can add other objects in the array or modify the existing data.
v1, v2 should be valid semvers and should be in string format. The expected_result is the number value, where 0 means both are equal; 1 means v1 has higher precedence over v2 and -1 means v2 has higher precedence over v1
If all the sample_input computes the exact value as corresponding expected_results, TestCase will not return any error.
