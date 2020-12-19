

# Big Data Privacy using Fully Homomorphic Non-deterministic Encryption

![](https://github.com/Mayur-Debu/Homomorphic_Encryption/blob/main/System%20Architecture.png "System Architecture of the Homomorphic Encryption")


#### Briefing of the project:
client.py sits with the customer and includes methods to generate and store a private/public key pair and methods to help decrypt the answer onces received from the Server.server.py and MachineLearningModel.py sit with the Machine Learning Model that provides Machine Learning services. These files would receive a json object with encrypted data and use the weights from the model in MachineLearningModel.py and do the explicit calculations in the server.py file. This file also includes method to package up the answer and return it back to the client; where, the file can be further decrypted.

*****
# Run in Gitpod

You can also run Homomorphic_Encryption in Gitpod, a free online dev environment for GitHub:

<img src="https://media0.giphy.com/media/VGiAk8CLVqlFF4N2Mi/giphy.gif" alt="drawing" width="50"/></img>
[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://b6fc9e42-a51c-4db6-a338-e2d852c9e8e2.ws-us03.gitpod.io/#/workspace/Homomorphic_Encryption)

Please Note: The GUI is a little glithcy in GitPod. For best results expand the VNC window to be full screen.
