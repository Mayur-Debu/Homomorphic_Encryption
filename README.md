# Big Data Privacy using Fully Homomorphic Non-deterministic Encryption

![](https://github.com/Mayur-Debu/Homomorphic_Encryption/blob/main/System%20Architecture.png "System Architecture of the Homomorphic Encryption")


This code has three files. 
Cust.py sits with the customer and includes methods to generate and store a private/public key pair and methods to help decrypt the answer onces received from the company
servercalc.py and linmodel.py sit with the ML company that provides ML services. They would receive a json object with encrypted data and use the weights from the model in linmodel.py and do the calculations in servercalc.py. This file also includes method to package up the answer and return it bak to the customer.

