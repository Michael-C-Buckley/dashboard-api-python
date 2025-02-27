from meraki.common import prepare_url_item as prepare


class CellularGateway(object):
    def __init__(self, session):
        super(CellularGateway, self).__init__()
        self._session = session
        


    def getDeviceCellularGatewayLan(self, serial: str):
        """
        **Show the LAN Settings of a MG**
        https://developer.cisco.com/meraki/api-v1/#!get-device-cellular-gateway-lan

        - serial (string): Serial
        """

        metadata = {
            'tags': ['cellularGateway', 'configure', 'lan'],
            'operation': 'getDeviceCellularGatewayLan'
        }
        resource = f'/devices/{prepare(serial)}/cellularGateway/lan'

        return self._session.get(metadata, resource)
        


    def updateDeviceCellularGatewayLan(self, serial: str, **kwargs):
        """
        **Update the LAN Settings for a single MG.**
        https://developer.cisco.com/meraki/api-v1/#!update-device-cellular-gateway-lan

        - serial (string): Serial
        - reservedIpRanges (array): list of all reserved IP ranges for a single MG
        - fixedIpAssignments (array): list of all fixed IP assignments for a single MG
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['cellularGateway', 'configure', 'lan'],
            'operation': 'updateDeviceCellularGatewayLan'
        }
        resource = f'/devices/{prepare(serial)}/cellularGateway/lan'

        body_params = ['reservedIpRanges', 'fixedIpAssignments', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getDeviceCellularGatewayPortForwardingRules(self, serial: str):
        """
        **Returns the port forwarding rules for a single MG.**
        https://developer.cisco.com/meraki/api-v1/#!get-device-cellular-gateway-port-forwarding-rules

        - serial (string): Serial
        """

        metadata = {
            'tags': ['cellularGateway', 'configure', 'portForwardingRules'],
            'operation': 'getDeviceCellularGatewayPortForwardingRules'
        }
        resource = f'/devices/{prepare(serial)}/cellularGateway/portForwardingRules'

        return self._session.get(metadata, resource)
        


    def updateDeviceCellularGatewayPortForwardingRules(self, serial: str, **kwargs):
        """
        **Updates the port forwarding rules for a single MG.**
        https://developer.cisco.com/meraki/api-v1/#!update-device-cellular-gateway-port-forwarding-rules

        - serial (string): Serial
        - rules (array): An array of port forwarding params
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['cellularGateway', 'configure', 'portForwardingRules'],
            'operation': 'updateDeviceCellularGatewayPortForwardingRules'
        }
        resource = f'/devices/{prepare(serial)}/cellularGateway/portForwardingRules'

        body_params = ['rules', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkCellularGatewayConnectivityMonitoringDestinations(self, networkId: str):
        """
        **Return the connectivity testing destinations for an MG network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-cellular-gateway-connectivity-monitoring-destinations

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['cellularGateway', 'configure', 'connectivityMonitoringDestinations'],
            'operation': 'getNetworkCellularGatewayConnectivityMonitoringDestinations'
        }
        resource = f'/networks/{prepare(networkId)}/cellularGateway/connectivityMonitoringDestinations'

        return self._session.get(metadata, resource)
        


    def updateNetworkCellularGatewayConnectivityMonitoringDestinations(self, networkId: str, **kwargs):
        """
        **Update the connectivity testing destinations for an MG network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-cellular-gateway-connectivity-monitoring-destinations

        - networkId (string): Network ID
        - destinations (array): The list of connectivity monitoring destinations
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['cellularGateway', 'configure', 'connectivityMonitoringDestinations'],
            'operation': 'updateNetworkCellularGatewayConnectivityMonitoringDestinations'
        }
        resource = f'/networks/{prepare(networkId)}/cellularGateway/connectivityMonitoringDestinations'

        body_params = ['destinations', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkCellularGatewayDhcp(self, networkId: str):
        """
        **List common DHCP settings of MGs**
        https://developer.cisco.com/meraki/api-v1/#!get-network-cellular-gateway-dhcp

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['cellularGateway', 'configure', 'dhcp'],
            'operation': 'getNetworkCellularGatewayDhcp'
        }
        resource = f'/networks/{prepare(networkId)}/cellularGateway/dhcp'

        return self._session.get(metadata, resource)
        


    def updateNetworkCellularGatewayDhcp(self, networkId: str, **kwargs):
        """
        **Update common DHCP settings of MGs**
        https://developer.cisco.com/meraki/api-v1/#!update-network-cellular-gateway-dhcp

        - networkId (string): Network ID
        - dhcpLeaseTime (string): DHCP Lease time for all MG of the network. Possible values are '30 minutes', '1 hour', '4 hours', '12 hours', '1 day' or '1 week'.
        - dnsNameservers (string): DNS name servers mode for all MG of the network. Possible values are: 'upstream_dns', 'google_dns', 'opendns', 'custom'.
        - dnsCustomNameservers (array): list of fixed IPs representing the the DNS Name servers when the mode is 'custom'
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['cellularGateway', 'configure', 'dhcp'],
            'operation': 'updateNetworkCellularGatewayDhcp'
        }
        resource = f'/networks/{prepare(networkId)}/cellularGateway/dhcp'

        body_params = ['dhcpLeaseTime', 'dnsNameservers', 'dnsCustomNameservers', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkCellularGatewaySubnetPool(self, networkId: str):
        """
        **Return the subnet pool and mask configured for MGs in the network.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-cellular-gateway-subnet-pool

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['cellularGateway', 'configure', 'subnetPool'],
            'operation': 'getNetworkCellularGatewaySubnetPool'
        }
        resource = f'/networks/{prepare(networkId)}/cellularGateway/subnetPool'

        return self._session.get(metadata, resource)
        


    def updateNetworkCellularGatewaySubnetPool(self, networkId: str, **kwargs):
        """
        **Update the subnet pool and mask configuration for MGs in the network.**
        https://developer.cisco.com/meraki/api-v1/#!update-network-cellular-gateway-subnet-pool

        - networkId (string): Network ID
        - mask (integer): Mask used for the subnet of all MGs in  this network.
        - cidr (string): CIDR of the pool of subnets. Each MG in this network will automatically pick a subnet from this pool.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['cellularGateway', 'configure', 'subnetPool'],
            'operation': 'updateNetworkCellularGatewaySubnetPool'
        }
        resource = f'/networks/{prepare(networkId)}/cellularGateway/subnetPool'

        body_params = ['mask', 'cidr', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkCellularGatewayUplink(self, networkId: str):
        """
        **Returns the uplink settings for your MG network.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-cellular-gateway-uplink

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['cellularGateway', 'configure', 'uplink'],
            'operation': 'getNetworkCellularGatewayUplink'
        }
        resource = f'/networks/{prepare(networkId)}/cellularGateway/uplink'

        return self._session.get(metadata, resource)
        


    def updateNetworkCellularGatewayUplink(self, networkId: str, **kwargs):
        """
        **Updates the uplink settings for your MG network.**
        https://developer.cisco.com/meraki/api-v1/#!update-network-cellular-gateway-uplink

        - networkId (string): Network ID
        - bandwidthLimits (object): The bandwidth settings for the 'cellular' uplink
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['cellularGateway', 'configure', 'uplink'],
            'operation': 'updateNetworkCellularGatewayUplink'
        }
        resource = f'/networks/{prepare(networkId)}/cellularGateway/uplink'

        body_params = ['bandwidthLimits', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getOrganizationCellularGatewayUplinkStatuses(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the uplink status of every Meraki MG cellular gateway in the organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-cellular-gateway-uplink-statuses

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): A list of network IDs. The returned devices will be filtered to only include these networks.
        - serials (array): A list of serial numbers. The returned devices will be filtered to only include these serials.
        - iccids (array): A list of ICCIDs. The returned devices will be filtered to only include these ICCIDs.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['cellularGateway', 'monitor', 'uplink', 'statuses'],
            'operation': 'getOrganizationCellularGatewayUplinkStatuses'
        }
        resource = f'/organizations/{prepare(organizationId)}/cellularGateway/uplink/statuses'

        query_params = ['perPage', 'startingAfter', 'endingBefore', 'networkIds', 'serials', 'iccids', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', 'serials', 'iccids', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        
