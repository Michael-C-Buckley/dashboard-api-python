from meraki.common import prepare_url_item as prepare


class Insight(object):
    def __init__(self, session):
        super(Insight, self).__init__()
        self._session = session
        


    def getNetworkInsightApplicationHealthByTime(self, networkId: str, applicationId: str, **kwargs):
        """
        **Get application health by time**
        https://developer.cisco.com/meraki/api-v1/#!get-network-insight-application-health-by-time

        - networkId (string): Network ID
        - applicationId (string): Application ID
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 7 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. The default is 2 hours.
        - resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 60, 300, 3600, 86400. The default is 300.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['insight', 'monitor', 'applications', 'healthByTime'],
            'operation': 'getNetworkInsightApplicationHealthByTime'
        }
        resource = f'/networks/{prepare(networkId)}/insight/applications/{prepare(applicationId)}/healthByTime'

        query_params = ['t0', 't1', 'timespan', 'resolution', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getOrganizationInsightApplications(self, organizationId: str):
        """
        **List all Insight tracked applications**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-insight-applications

        - organizationId (string): Organization ID
        """

        metadata = {
            'tags': ['insight', 'configure', 'applications'],
            'operation': 'getOrganizationInsightApplications'
        }
        resource = f'/organizations/{prepare(organizationId)}/insight/applications'

        return self._session.get(metadata, resource)
        


    def getOrganizationInsightMonitoredMediaServers(self, organizationId: str):
        """
        **List the monitored media servers for this organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-insight-monitored-media-servers

        - organizationId (string): Organization ID
        """

        metadata = {
            'tags': ['insight', 'configure', 'monitoredMediaServers'],
            'operation': 'getOrganizationInsightMonitoredMediaServers'
        }
        resource = f'/organizations/{prepare(organizationId)}/insight/monitoredMediaServers'

        return self._session.get(metadata, resource)
        


    def createOrganizationInsightMonitoredMediaServer(self, organizationId: str, name: str, address: str, **kwargs):
        """
        **Add a media server to be monitored for this organization**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-insight-monitored-media-server

        - organizationId (string): Organization ID
        - name (string): The name of the VoIP provider
        - address (string): The IP address (IPv4 only) or hostname of the media server to monitor
        - bestEffortMonitoringEnabled (boolean): Indicates that if the media server doesn't respond to ICMP pings, the nearest hop will be used in its stead.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['insight', 'configure', 'monitoredMediaServers'],
            'operation': 'createOrganizationInsightMonitoredMediaServer'
        }
        resource = f'/organizations/{prepare(organizationId)}/insight/monitoredMediaServers'

        body_params = ['name', 'address', 'bestEffortMonitoringEnabled', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getOrganizationInsightMonitoredMediaServer(self, organizationId: str, monitoredMediaServerId: str):
        """
        **Return a monitored media server for this organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-insight-monitored-media-server

        - organizationId (string): Organization ID
        - monitoredMediaServerId (string): Monitored media server ID
        """

        metadata = {
            'tags': ['insight', 'configure', 'monitoredMediaServers'],
            'operation': 'getOrganizationInsightMonitoredMediaServer'
        }
        resource = f'/organizations/{prepare(organizationId)}/insight/monitoredMediaServers/{prepare(monitoredMediaServerId)}'

        return self._session.get(metadata, resource)
        


    def updateOrganizationInsightMonitoredMediaServer(self, organizationId: str, monitoredMediaServerId: str, **kwargs):
        """
        **Update a monitored media server for this organization**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-insight-monitored-media-server

        - organizationId (string): Organization ID
        - monitoredMediaServerId (string): Monitored media server ID
        - name (string): The name of the VoIP provider
        - address (string): The IP address (IPv4 only) or hostname of the media server to monitor
        - bestEffortMonitoringEnabled (boolean): Indicates that if the media server doesn't respond to ICMP pings, the nearest hop will be used in its stead.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['insight', 'configure', 'monitoredMediaServers'],
            'operation': 'updateOrganizationInsightMonitoredMediaServer'
        }
        resource = f'/organizations/{prepare(organizationId)}/insight/monitoredMediaServers/{prepare(monitoredMediaServerId)}'

        body_params = ['name', 'address', 'bestEffortMonitoringEnabled', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def deleteOrganizationInsightMonitoredMediaServer(self, organizationId: str, monitoredMediaServerId: str):
        """
        **Delete a monitored media server from this organization**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-insight-monitored-media-server

        - organizationId (string): Organization ID
        - monitoredMediaServerId (string): Monitored media server ID
        """

        metadata = {
            'tags': ['insight', 'configure', 'monitoredMediaServers'],
            'operation': 'deleteOrganizationInsightMonitoredMediaServer'
        }
        resource = f'/organizations/{prepare(organizationId)}/insight/monitoredMediaServers/{prepare(monitoredMediaServerId)}'

        return self._session.delete(metadata, resource)
        
