# Assignment 3 - CS-534 Fall'18 README
By Surya Vadivazhagu

#### Re: Chronic Kidney Disease Pre-Processing
I made some personal changes to the provided chronic kidney disease dataset to make parsing it easier. I changed the values of all the strings in each data column to represent its status.
For example, `No` = `0`, `Good` = `1`, `Normal`  = `1`
The purpose of this binary simplification was to make parsing the dataset easier. If we are able to convert the strings to a binary integer, we do not need worry about string comprehension and translation into a binary value in the data parsing function. At the end of the day, the machine will only understand (for now) and be able to analyze a yes/no decision as 1/0.


#### Re: Problem 2 Lack of Implementation
There were some issues I ran into while doing this assignment. One primarily was the lack of time due to undergraduate final exams coupled with some situations on my travel home and an inability to access the Internet until I returned to Worcester on Sunday, 10/21. I was able to complete Problems 1, 3, and 4 successfully but was unable to make any noteworthy progress on Problem 2, the logistic regression with regularization implementation. I made a few functions but that was it. I acknowledge my failure due to not prioritizing the problem. 