import os
import json
import requests
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

from pinata import pin_file_to_ipfs, pin_json_to_ipfs, convert_data_to_json

load_dotenv()

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

# Create contract dictionary to store info
concert_database = {
    "General Admission": ["General Admission", "SMART_CONTRACT_ADDRESS_GA", 50, './contracts/compiled/general_admission.json', "https://gateway.pinata.cloud/ipfs/QmUnEEC1U22XpEmzT7E8St96984CPVDRYkN6qH4yxUKptF","QmUnEEC1U22XpEmzT7E8St96984CPVDRYkN6qH4yxUKptF"],
    "Pit": ["Pit", "SMART_CONTRACT_ADDRESS_PIT", 150, './contracts/compiled/pit.json', "https://gateway.pinata.cloud/ipfs/Qmb8qk1XRziBQ7yqof8aE6Mb8HtVa6oNFXavrPPmbauiXX", "Qmb8qk1XRziBQ7yqof8aE6Mb8HtVa6oNFXavrPPmbauiXX"],
    "Back Stage": ["Back Stage", "SMART_CONTRACT_ADDRESS_BS", 300, './contracts/compiled/back_stage.json', "https://gateway.pinata.cloud/ipfs/QmY95o4C3R4Tuto183ZzXc35Pq52QTad6bXPTTFwVCDiSz", "QmY95o4C3R4Tuto183ZzXc35Pq52QTad6bXPTTFwVCDiSz"]
}

################################################################################
# The Load_Contract Function
################################################################################

@st.cache(allow_output_mutation=True)
def load_contract():
   
    with open(Path(concert_database[ticket_tier][3])) as f: 
        artwork_abi = json.load(f)
    contract_address = os.getenv(concert_database[ticket_tier][1])

    # Load the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=artwork_abi
    )

    return contract


################################################################################
# Register New Ticket
################################################################################
st.title("Enter Your Festival Experience")
accounts = w3.eth.accounts
tiers = ["General Admission", "Pit", "Back Stage"]
concert_name_list = ["Generic Concert 1", "Generic Concert 2", "Generic Concert 3"]
concert_details_list = ["Slip Knot - 5/9/21", "The Contortionist - 8/16/22", "Weezer - 11/21/22", "Pearl Jam - 12/14/22"]

# Use a Streamlit component to get the address of the artwork owner from the user
address = st.selectbox("Select Ticket Owner", options=accounts)

# Use a Streamlit component to get correct ticket tier and concert details from the user
st.markdown("# Choose Your Pass")
concert_name  = st.selectbox("Name of Event", options=concert_name_list)
concert_details = st.selectbox("Event Details", options=concert_details_list)
ticket_tier = st.selectbox("Select Your Ticket Option", options=tiers)

# Register New Ticket
################################################################################
ETH_data = requests.get("https://api.alternative.me/v2/ticker/Ethereum/?convert=USD").json()
ether_exchange_rate = ETH_data['data']['1027']['quotes']['USD']['price']
ticket_cost_ether_display = round(concert_database[ticket_tier][2] / ether_exchange_rate, 6)
ticket_cost_ether = concert_database[ticket_tier][2] / ether_exchange_rate
ticket_cost_wei = w3.toWei(ticket_cost_ether, 'ether')
st.write(f"Ticket cost is ${concert_database[ticket_tier][2]} = {ticket_cost_ether_display} ETH")
contract = load_contract()

# Get Artwork URI from initial dictionary up top
artwork_uri = concert_database[ticket_tier][4]
total_token_supply = contract.functions.totalSupply().call()

if st.button("Purchase Ticket"):

    # Use the contract to send a transaction to the registerArtwork function and send a transaction that transfers the cost of the ticket to the company
    if total_token_supply < 3:
        tx_hash = contract.functions.registerEventArt(
            address,
            concert_name,
            concert_details,
            concert_database[ticket_tier][2],
            artwork_uri
            ).transact({'from': address, 'gas': 1000000})
        receipt = w3.eth.waitForTransactionReceipt(tx_hash)
        w3.eth.send_transaction({'to': '0x8F97dC517a112df5F1Fc8fb5b81907f929991a4B', 'from': address , 'gas': 1000000, 'value': ticket_cost_wei})
        st.write("Transaction receipt mined:")
        st.write(dict(receipt))
    if total_token_supply >= 3:
        st.write("THIS PASS IS SOLD OUT")
st.markdown("---")


################################################################################
# Display a Token
################################################################################
st.markdown("## Check Balance of an Account")

selected_address = st.selectbox("Select Account", options=accounts)

tokens = contract.functions.balanceOf(selected_address).call()

st.write(f"This address owns {tokens} tokens")

st.markdown("## Check  Ownership and Display Token")

total_token_supply = contract.functions.totalSupply().call()

token_id = st.selectbox("Ticket Tokens", list(range(total_token_supply)))

if st.button("Display"):

    # Get the ticket token owner
    owner = contract.functions.ownerOf(token_id).call()
    
    st.write(f"The ticket is registered to {owner}")

    # Get the ticket token's URI
    token_uri = contract.functions.tokenURI(token_id).call()

    st.write(f"The tokenURI is {token_uri}")
    st.image(token_uri)

################################################################################
# Helper functions to pin files and json to Pinata
################################################################################

def pin_artwork(artwork_name):
    # Pin the file to IPFS with Pinata
    ipfs_file_hash = concert_database[ticket_tier][6]

     # .getvalue() is a streamlit function that gets the file data

    # Build a token metadata file for the artwork
    token_json = {
        "name": artwork_name,
        "image": ipfs_file_hash
    }
    json_data = convert_data_to_json(token_json)

    # Pin the json to IPFS with Pinata
    json_ipfs_hash = pin_json_to_ipfs(json_data)

    return json_ipfs_hash, token_json


def pin_appraisal_report(report_content): 
    json_report = convert_data_to_json(report_content)
    report_ipfs_hash = pin_json_to_ipfs(json_report)
    return report_ipfs_hash


