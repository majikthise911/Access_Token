# Access_Token
NFT that gives you access to events 

## Table of Contents
- [Background](#background)
- [Overview of the project](#overview-of-the-project)
- [Files](#files)
- [Software](#software)
- [Installs](#installs)
- [Imports](#imports)
- [Instructions](#instructions)




# Background 
Have you ever gone to an event that held special meaning to you and required a ticket to get in? Often one might keep such a ticket as memorabilia to look back on at a future point in time, however, the small piece of paper that the words and images are printed on is delicate and easy to lose. Also, once the event is over with the ticket no longer has value outside of the sentimental value that you have attached to it. 

# Overview of the project 

## Objective 
The objective of this project is to create an NFT collection for various events which can be used as a ticket. These NFT's would be exchangeable during and after the event and become collectibles. There will be a three-tier access system in which the token supply for each tier will be based on the limits set by the event that is being held.


## Distribution 
Our goal for distribution is to create a Market Place where our collection of Access Tokens is available from various events. The initial token price would be set to the value of the event ticket and can be used to enter the event. Information such as the event name, event details, and ticket value will be inputed and attached to the NFT. Ultimately, our end goal is to be able to exchange the tokens if tickets are no longer available or if the date of the event has passed using our Market Place.

Alternative options to distribution include the use of prexisting NFT exchanges such as OpenSea and Rarible. Another potential option is the use of "Air Drops".
"Air Drops" are very common and popular occurence in the crypto world and is an easy way to distribute the Access Token purchased if bought through a thrid party such as TicketMaster, StubHub, SeatGeek, etc. This would require that the purchaser provide their wallet address so that the token can be sent directly to their wallet. "Air Drops" are also a easy way to advertise our services through various social media outlets and create hype about the collection that is being released.

# Files
- [app.py](https://github.com/majikthise911/Access_Token)
- [pinata.py](https://github.com/majikthise911/Access_Token)
- [backStageToken.sol](https://github.com/majikthise911/Access_Token/tree/main/contracts)
- [generalAdmissionToken.sol](https://github.com/majikthise911/Access_Token/tree/main/contracts)
- [pitToken.sol](https://github.com/majikthise911/Access_Token/tree/main/contracts)
- [back_stagel.json](https://github.com/majikthise911/Access_Token/tree/main/contracts/compiled)
- [general_admission.json](https://github.com/majikthise911/Access_Token/tree/main/contracts/compiled)
- [pit.json](https://github.com/majikthise911/Access_Token/tree/main/contracts/compiled)

# Software
- Ganache – used as a private blockchain that runs locally on the machine being tested on. All interacting wallet addresses are simulated using Ganache.
- Metamask – we are interacting with the smart contract and test blockchain using Metamask browser wallet.  
- VsCode – used to run the app.py and pinata.py files that run the interface on Streamlit. 

# Installs
- Streamlit 
- Web3 

# Imports 
- import os
- import json
- import requests
- from web3 import Web3
- from pathlib import Path
- from dotenv import load_dotenv
- import streamlit as st

- from pinata import pin_file_to_ipfs, pin_json_to_ipfs, convert_data_to_json

# Instructions 

1.	Open Ganache test blockchain 
2.	Set up Ganache test environment 

![Step 2a](https://raw.githubusercontent.com/majikthise911/Access_Token/main/Images/02a_set%20up%20ganache%20network%20on%20metamask.png)
* * *
![Step 2b](https://raw.githubusercontent.com/majikthise911/Access_Token/main/Images/02b_import%20ganache%20accounts%20to%20metamask1.png)
* * *
![Step 2c](https://raw.githubusercontent.com/majikthise911/Access_Token/main/Images/02c_import%20ganache%20accounts%20to%20metamask2.png)
* * *
3.	Open remix and connect Metamask to remix  
![Step 3](https://raw.githubusercontent.com/majikthise911/Access_Token/main/Images/03_import%20contracts%20to%20remix.png)
* * *

4.	Import all three contracts into remix  
5.	Compile each contract 

![Step 5](https://raw.githubusercontent.com/majikthise911/Access_Token/main/Images/05_compile.png)
* * *

6.	Deploy each contract
![Step 6a](https://raw.githubusercontent.com/majikthise911/Access_Token/main/Images/06a_deploy.png)
* * *
7.	Confirm gas in Metamask
![Step 6b](https://raw.githubusercontent.com/majikthise911/Access_Token/main/Images/06b_confirm%20gas.png)
* * *
![Step ca](https://raw.githubusercontent.com/majikthise911/Access_Token/main/Images/06c_transaction%20data.png)
* * *
8.	Copy the meta data for each deployed contract
![Step 8](https://raw.githubusercontent.com/majikthise911/Access_Token/main/Images/08_copy%20meta%20data.png)
* * *
9.	Create a directory within the contracts directory called “compiled” 
10.	Paste that meta data for each deployed contract into corresponding .json files in the compiled folder
11.	Copy the hash function for each contract and paste into the corresponding variable within the .env file 

![Step 11](https://raw.githubusercontent.com/majikthise911/Access_Token/main/Images/11_copy%20contract%20hash.png)
* * *
12.	 Copy the wallet address for the receiving account and paste into the app.py file 
13.	Open terminal and navigate to the folder that the app.py folder is in
14.	Make sure you are in the correct dev environment
15.	Type Streamlit run app.py in the terminal 








                 