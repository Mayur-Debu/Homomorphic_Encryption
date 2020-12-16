# Big Data Privacy using Fully Homomorphic Non-deterministic Encryption

![](https://github.com/Mayur-Debu/Homomorphic_Encryption/blob/main/System%20Architecture.png "System Architecture of the Homomorphic Encryption")


## This code has three files. 
#### client.py sits with the customer and includes methods to generate and store a private/public key pair and methods to help decrypt the answer onces received from the Server.
#### server.py and MachineLearningModel.py sit with the Machine Learning Model that provides Machine Learning services. 
#### These files would receive a json object with encrypted data and use the weights from the model in MachineLearningModel.py and do the explicit calculations in the server.py file. This file also includes method to package up the answer and return it back to the client; where, the file can be further decrypted.

