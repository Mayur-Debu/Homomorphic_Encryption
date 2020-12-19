# Big Data Privacy using Fully Homomorphic Non-deterministic Encryption

<img src="https://github.com/Mayur-Debu/Homomorphic_Encryption/blob/main/System%20Architecture.png" align="center"  />

#### Briefing of the project:
client.py sits with the customer and includes methods to generate and store a private/public key pair and methods to help decrypt the answer onces received from the Server.
server.py and MachineLearningModel.py sit with the Machine Learning Model that provides Machine Learning services. 
These files would receive a json object with encrypted data and use the weights from the model in MachineLearningModel.py and do the explicit calculations in the server.py file. 
This file also includes method to package up the answer and return it back to the client; where, the file can be further decrypted.

*****
# Run in Gitpod
You can also run Homomorphic_Encryption in Gitpod, a free online dev environment for GitHub:<br><br>
[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://b6fc9e42-a51c-4db6-a338-e2d852c9e8e2.ws-us03.gitpod.io/#/workspace/Homomorphic_Encryption)
<br>Please Note: The GUI is a little glithcy in GitPod. For best results expand the VNC window to be full screen.

*****
# Acknowledgement:
>Research Paper: Big Data Privacy Using Fully Homomorphic Non-Deterministic Encryption.<br>
>Submitted By: Tejashree P. SSBT's COET (Alumni), Girish P. SSBT's COET (HOD. Computer Engineering Department).<br>
>INSPEC Accession Number: 17030423<br>
>DOI: 10.1109/IACC.2017.0041<br>
>Date of Conference: 5-7 Jan, 2017.<br>
>Publisher: IEEE<br>
>Date Added to IEEE Xplore: 13 July, 2017.<br>
><img src="https://media3.giphy.com/media/VGiAk8CLVqlFF4N2Mi/giphy.gif" width=30/>  https://ieeexplore.ieee.org/document/7976775

