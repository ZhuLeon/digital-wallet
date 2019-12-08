# Table of Contents

1. [Summary] (README.md#summary)
2. [Details of Implementation] (README.md#details-of-implementation)
3. [Description of Data] (README.md#description-of-data)

# Summary
Suppose a "digital wallet" company called PayMo allows users to easily request and make payments to other PayMo users. The team at PayMo has decided they want to implement features to prevent fraudulent payment requests from untrusted users. While PayMo is a fictional company, the dataset is quite interesting -- it's inspired by a real social network, includes the time of transaction, and the messages come from real Venmo transactions

# Details of Implementation
### Feature 1
When anyone makes a payment to another user, they'll be notified if they've never made a transaction with that user before.

* "unverified: You've never had a transaction with this user before. Are you sure you would like to proceed with this payment?"

### Feature 2
The PayMo team is concerned that these warnings could be annoying because there are many users who haven't had transactions, but are still in similar social networks. 

For example, User A has never had a transaction with User B, but both User A and User B have made transactions with User C, so User B is considered a "friend of a friend" for User A.

For this reason, User A and User B should be able to pay each other without triggering a warning notification since they're "2nd degree" friends. 

<img src="./images/friend-of-a-friend1.png" width="500">

To account for this, PayMo would like you to also implement this feature. When users make a payment, they'll be notified of when they're not "a friend of a friend".

* "unverified: This user is not a friend or a "friend of a friend". Are you sure you would like to proceed with this payment?"


### Feature 3
More generally, PayMo would like to extend this feature to larger social networks. Implement a feature to warn users only when they're outside the "4th degree friends network".

<img src="./images/fourth-degree-friends2.png" width="600">

In the above diagram, payments have transpired between User

* A and B 
* B and C 
* C and D 
* D and E 
* E and F

Under this feature, if User A were to pay User E, there would be no warning since they are "4th degree friends". 

However, if User A were to pay User F, a warning would be triggered as their transaction is outside of the "4th-degree friends network."

(Note that if User A were to pay User C instead, there would be no warning as they are "2nd-degree" friends and within the "4th degree network") 

Generally, my solution to the problem was to create a undirected graph and then search through it using breadth first search.
Using the data from `batch_payment.txt` I parsed each line using the ", " deliminator in order to track `id1` and `id2`. To implement all the features that were required, some connection between all the ids had to be made. To make this connection, I envisioned a graph/tree would be a good way in terms of time and space complexity to represent the data. In order to do this, the data structure I choose to use was a dictionary with the `key` being `id1` and `value` being `id2`.

In order to handle the transactions in `stream_payment.txt` there needed to be an efficient way to search through the graph/tree I just created. Since feature 3 would require the maximum depth to search through to be 4, breadth first search was the algorithm implemented.

## Test files
In the ./insight_testsuite/my-own-test there are two folders; `test1-small` and `test2-large`. `test1-small` was a relatively small data set I created in order to test the functionality of my program. The ids are simple numbers from 1 to 15. 
Here is an visual representation of the data I created. Please excuse my poor drawing.

<img src="./images/batch_payment.png" width="500">

In `stream_payment1.txt`, I designed it to test functionality for all 3 features as well as edge cases such as searching for a path where id1 has never been linked to id2 and searching for a path from id1 to an nonexisitng id2.

In `test2-large` I took partial data from the csv files provided and ran it through my program to see how it would handle large files. Of course, since I can not know the solution to that particular data set, this test was not to check for correctness. One thing to note here is that, I think that definietly the time complexity of my implementation can be improved.

### Notes
In handling the transactions in `stream_payment.txt` I was not sure if a value of `trusted` meant I should update the database and so I did not implement that feature. I only processed the transaction and did not change the database regardless of the value returned.
