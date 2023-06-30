from pyzabbix import ZabbixMetric, ZabbixSender 

  
ZABBIX_SERVER_URL = "zabbix.verbis.dkfz.de"  
packet = [
			ZabbixMetric(" Serv-05-Test-BK", "blazehealth.item", "OK"),
            ZabbixMetric(" Serv-05-Test-BK", "blazeversion.item", "0.21.0"),
            ZabbixMetric(" Serv-05-Test-BK", "blazeresouces.item", "0")
		]
result = ZabbixSender(ZABBIX_SERVER_URL).send([packet])
print(result)