import os
import json
import requests
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

################################################################################
# The Load_Contract Function
################################################################################

concert_database = {
    "General Admission": ["General Admission", "SMART_CONTRACT_ADDRESS_GA", 50, './contracts/compiled/general_admission.json', "https://raw.githubusercontent.com/majikthise911/Access_Token/devFork-JC/Screenshot%202022-08-11%20213953.png"],
    "Pit": ["Pit", "SMART_CONTRACT_ADDRESS_PIT", 150, './contracts/compiled/pit.json', "https://raw.githubusercontent.com/majikthise911/Access_Token/devFork-JC/Screenshot%202022-08-11%20213742.png"],
    "Back Stage": ["Back Stage", "SMART_CONTRACT_ADDRESS_BS", 300, './contracts/compiled/back_stage.json', "https://raw.githubusercontent.com/majikthise911/Access_Token/devFork-JC/Screenshot%202022-08-11%20214135.png"]
}


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
concert_name  = st.selectbox("Select Your Venue", options=concert_name_list)
concert_details = st.selectbox("Select Your Artist", options=concert_details_list)
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
    if total_token_supply < 10:
        tx_hash = contract.functions.registerEventArt(
            address,
            concert_name,
            concert_details,
            concert_database[ticket_tier][2],
            artwork_uri
            ).transact({'from': address, 'gas': 1000000})
        receipt = w3.eth.waitForTransactionReceipt(tx_hash)
        w3.eth.send_transaction({'to': '0x1Cde67bB7Dc95153EC27e833eB6Be0BfED471C86', 'from': address , 'gas': 1000000, 'value': ticket_cost_wei})
        st.write("Transaction receipt mined:")
        st.write(dict(receipt))
    if total_token_supply >= 10:
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

