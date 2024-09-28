# Code stability

## The types of mechanisms
- There are two types of mechanisms, that is, pull-based and push-based. 
- In the **pull-based** mechanism, our CI server will **continuously poll** the git repository of the application to see if there are any new changes. 
- But in the **push-based** mechanism, we will configure a **webhook** in our git repository that will **send an event** to our CI server for every commit or action in the repository.

## Explanation
- In the **pull-based** method, there would be **unnecessary load** on our CI server for continuously polling the repository at certain times. 
- Moreover, the change is happening at the repository end, so it would only be logical for **the repository** to **trigger** an event instead of the other way