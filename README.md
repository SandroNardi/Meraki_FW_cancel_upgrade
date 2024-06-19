# Mass FW Status

## Disclaimer

The content provided is for inspiration and educational purposes only, not for production use. It is an example to spark ideas, not optimized for real-world environments. Use it as a starting point, but review and test thoroughly before considering it for live applications.

Not tested for staged upgrade
Some unexpected results when dealing with MS/CS firmwares

## Description

The script scope all Meraki Oraganization and Network and attemp to cancel any FW upgrade by setting "Next FW version" = "Current FW version"

## API KEY

An API KEY (API_KEY) must be provided, write permission are required.

https://developer.cisco.com/meraki/api-v1/authorization/#obtaining-your-meraki-api-key

## API endpoint used

[Get Organizations](https://developer.cisco.com/meraki/api-v1/get-organizations/)

[Get Organization Networks](https://developer.cisco.com/meraki/api-v1/get-organization-networks/)

[Get Organization Firmware Upgrades](https://developer.cisco.com/meraki/api-v1/get-organization-firmware-upgrades/)

[Get Network Firmware Upgrades](https://developer.cisco.com/meraki/api-v1/get-network-firmware-upgrades/)

[Update Network Firmware Upgrades](https://developer.cisco.com/meraki/api-v1/update-network-firmware-upgrades/)
