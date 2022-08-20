# Access_Token
NFT that gives you access to events 

## Table of Contents
- [Background](#background)
- [Overview of the project](#overview-of-the-project)
- [Project Notes](#project-notes)
- [Files](#files)
- [Software](#software)
- [Installs](#installs)
- [Instructions](#instructions)
- [Software version control](https://github.com/majikthise911/Access_Token)
    - [GitHub Work](https://github.com/majikthise911/Access_Token)
    - [Installation Notes](https://github.com/majikthise911/Access_Token)
    - [Setup Notes](https://github.com/majikthise911/Access_Token)



# Background 
Have you ever gone to an event that held special meaning to you and required a ticket to get in? Often one might keep such a ticket as memorabilia to look back on at a future point in time, however, the small piece of paper that the words and images are printed on is delicate and easy to lose. Also, once the event is over with the ticket no longer has value outside of the sentimental value that you have attached to it. 

# Overview of the project 

## Objective 
The objective of this project is to create an NFT collection for various events which can be used as a ticket. These NFT's would be exchangeable during and after the event and become collectibles. There will be a three-tier access system in which the token supply for each tier will be based on the limits set by the event that is being held.


## Distribution 
Our goal for distribution is to create a Market Place where our collection of Access Tokens is available from various events. The initial token price would be set to the value of the event ticket and can be used to enter the event. Information such as the event name, event details, and ticket value will be inputed and attached to the NFT. Ultimately, our end goal is to be able to exchange the tokens if tickets are no longer available or if the date of the event has passed using our Market Place.

Alternative options to distribution include the use of prexisting NFT exchanges such as OpenSea and Rarible. Another potential option is the use of "Air Drops".
"Air Drops" are very common and popular occurence in the crypto world and is an easy way to distribute the Access Token purchased if bought through a thrid party such as TicketMaster, StubHub, SeatGeek, etc. This would require that the purchaser provide their wallet address so that the token can be sent directly to their wallet. "Air Drops" are also a easy way to advertise our services through various social media outlets and create hype about the collection that is being released.
# Project notes 
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

# Instructions 

1.	Open Ganache test blockchain 
2.	Set up Ganache test environment
3.	Open remix and connect Metamask to remix 
4.	Import all three contracts into remix 
5.	Compile each contract 
6.	Deploy each contract 
7.	Confirm gas in Metamask 
8.	Copy the meta data for each deployed contract 
9.	Create a directory within the contracts directory called “compiled” 
10.	Paste that meta data for each deployed contract into corresponding .json files in the compiled folder
11.	Copy the hash function for each contract and paste into the corresponding variable within the .env file 
12.	 Copy the wallet address for the receiving account and paste into the app.py file 
13.	Open terminal and navigate to the folder that the app.py folder is in
14.	Make sure you are in the correct dev environment
15.	Type Streamlit run app.py


![step 2](https://raw.githubusercontent.com/majikthise911/Access_Token/devFork-JC/Images/set%20up%20ganache%20network%20on%20metamask.png)






                 