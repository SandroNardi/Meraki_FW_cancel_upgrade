import os
import meraki
from prettytable import PrettyTable

API_KEY = os.getenv("MK_TEST_API")

dashboard = meraki.DashboardAPI(API_KEY, suppress_logging=True)

# get all arganization
organizations = dashboard.organizations.getOrganizations()

for org in organizations:
    upgrades = dashboard.organizations.getOrganizationFirmwareUpgrades(
        org["id"], total_pages="all", status="Scheduled"
    )
    print(f"> Organization {org['name']}")
    if len(upgrades) == 0:
        print(f">> No upgrades scheduled for Organization {org['name']}")
        continue

    networks = dashboard.organizations.getOrganizationNetworks(
        org["id"], total_pages="all"
    )


    for net in networks:
        net_updates = dashboard.networks.getNetworkFirmwareUpgrades(net["id"])

        upgradeWindow = net_updates["upgradeWindow"]
        timezone = net_updates["timezone"]
        products_to_cancel = {}
        more_than_zero_to_cancel = False
        print(f">> Parsing: {net['name']}")
        for k, product in net_updates["products"].items():
            if product["nextUpgrade"]["time"] == "":
                continue

            more_than_zero_to_cancel = True

            if product["currentVersion"] not in product["availableVersions"]:
                print(f">>> Can't cancel {k}, destination version not available")
                continue

            products_to_cancel[k] = {
                "nextUpgrade": {
                    "time": product["nextUpgrade"]["time"],
                    "toVersion": {"id": product["currentVersion"]["id"]},
                },
                "participateInNextBetaRelease": False,
            }

            print(
                f">>> {k}, scheduled upgrade {product['nextUpgrade']['time']}, from {product['currentVersion']['shortName']} to from {product['nextUpgrade']['toVersion']['shortName']}"
            )

        if more_than_zero_to_cancel:
            response = dashboard.networks.updateNetworkFirmwareUpgrades(
                net["id"],
                upgradeWindow=net_updates["upgradeWindow"],
                timezone=net_updates["timezone"],
                products=products_to_cancel,
            )
        else:
            print(f">>> Nothing to cancel for network {net['name']}")
