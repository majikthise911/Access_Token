pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract EventRegistry is ERC721Full {
    constructor() public ERC721Full("EventRegistryToken", "EVE") {}

    struct eventTicket {
        string eventName;
        string artistList;
        uint64 startDate;
        uint64 expireDate;
    }

    mapping(uint256 => eventTicket) public ticketCollection;

    event ticket (uint256 tokenId, uint64 startDate, uint64 expireDate);

    function registerEventArt(
        address owner,
        string memory eventName,
        string memory artistList,
        uint64 startDate,
        uint64 expireDate,
        string memory tokenURI
    ) public returns (uint256) {
        uint256 tokenId = totalSupply();
    
        _mint(owner, tokenId);
        _setTokenURI(tokenId, tokenURI);

        ticketCollection[tokenId] = eventTicket(eventName, artistList, startDate, expireDate);

        return tokenId;
    }

}
