# atbAssessment
# determinePrecedence get_highest_precedence
Steps to follow to run and test the code:
Open any IDE of your choice or open CLI/Terminal on your local machine.
Clone the repository on the local machine by typing the command "git clone https://github.com/ashwani227/atbAssessment" or Users can directly enter the URL provided on the browser.
Transit from current directory to the location where new repo is downloaded.
Make sure you have Python3 installed in your system.
Go to the folder and type python3 semver_comparison.py and press enter. 
User will see a boolean result as True or False. Along with the boolean value, user will see an additional piece of information which will show the most precedent version from a list of versions.
If user is using IDE then simply Run the semver_comparison.py file.
User can change the input in the main function which is Line 68 of semver_comparison.py file and observe the results.
User can change the list of semvers in Line 65 and feed in the semvers as string in any order and will get an output of Most precedent semver.



# Testcases:
For unittest, you have to use Conda environment in your machine.
Go to the IDE and look for file test_sem.py
Run the file from the IDE and observe the result. 
Please note, as per the description, all the semvers to be tested are valid semvers.
If the user wants to run multiple tests and check if the program is performing appropriately, please route to the sample_input.py file and can add other objects in the array or modify the existing data.
v1, v2 should be valid semvers and should be in string format. The expected_result is the number value, where 0 means both are equal; 1 means v1 has higher precedence over v2 and -1 means v2 has higher precedence over v1
User can make changes to version_list in sample_output.py and has to provide a solution for that.
If all the sample_input computes the exact value as corresponding expected_results, TestCase will not return any error.
Both the test cases will be passed if expected output turns out to be same as of computed output
