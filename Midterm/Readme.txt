Stack Exchange Data Analysis

This exercise analyses data retrived from Stack Exchange API and presents five cases based on the data analyzed

The data retrieved are as follows
1. Questions
2. Answers
3. Users
4. Badges

These are the following cases that have been analyzed
Case 1: Finding user specialization based on answers posted

Case 2:Top questions posted by users (based on user badge counts)

Case 3:Top and bottom ten users based on reputation over last one year( Percentage change of user reputation calculated)

Case 4:Find the most active and popular questions and topics

Case 5: Top characteristics of user (badge characteristics)
This case analyses the ratio of each badge characteristic with respect to the badge category it belongs to (Gold,Silver or Bronze)

Runing the scripts:
1. Run the 'gatheringdata.py' file to get the data from the API
2. Run the 'analysis_midterm.py' file to run the analysis you want

Steps to run
1.Navigate to required folder and type

python gatheringdata.py

2. To run the analysis
python analysis_midterm.py

This will prompt you with the case you want to analyze

The output is generated as .csv files and found in the Reports folder (under the specific case you have run)
