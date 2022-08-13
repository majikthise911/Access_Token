pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract GeneralAdmissionRegistry is ERC721Full {
    constructor() public ERC721Full("GeneralAdmissionToken", "GAT") {}

    struct eventTicket {
        string eventName;
        string artistList;
        string eventDetails;
        uint256 ticketValue;
    }

    mapping(uint256 => eventTicket) public ticketCollection;

    event ticket (uint256 tokenId, uint256 ticketValue, string reportURI);

    function registerEventArt(
        address owner,
        string memory eventName,
        string memory artistList,
        string memory eventDetails,
        uint256 initialTicketValue,
        string memory tokenURI
    ) public returns (uint256) {
        uint256 tokenId = totalSupply();
    
        _mint(owner, tokenId);
        _setTokenURI(tokenId, tokenURI);

        ticketCollection[tokenId] = eventTicket(eventName, artistList, eventDetails, initialTicketValue);
        
        return tokenId;
    }

    function ticketPrice(
        uint256 tokenId,
        uint256 newTicketValue,
        string memory reportURI
    ) public returns (uint256) {
        ticketCollection[tokenId].ticketValue = newTicketValue;

        emit ticket(tokenId, newTicketValue, reportURI);

        return ticketCollection[tokenId].ticketValue;
    }
}
