fwlog = "loc=4375104|time=2019-01-28 14:50:57|orig=192.0.2.18|i/f_dir=inbound|i/f_name=|has_accounting=0|logId=-1|log_type=log|log_sequence_num=758|is_first_for_luuid=131072|log_version=5|origin_sic_name=CN=TLV-UNI_44K,O=TLV-UNI-Smart-1..vubqrv|product=SmartDefense|src=198.20.99.130|attack=Scanner Enforcement Violation|Attack Info=Shodan Scanner BACNET Request|SmartDefense Profile=Optimized (Clone)|Protection Name=Shodan Scanner BACNET Request|Protection ID=asm_dynamic_prop_SHODAN_BACNET|Severity=3|Confidence Level=5|Performance Impact=3|Protection Type=IPS|Description URL=SHODAN_BACNET_help.html".replace("origin_sic_name=CN=TLV-UNI_44K,O=TLV-UNI-Smart-1..vubqrv", "origin_sic_name=TLV-UNI_44K")

# print([x.split('=') for x in fwlog.split('|')])

fwlogDict = dict(x.split('=') for x in fwlog.split('|'))

print(fwlogDict)

print(fwlogDict['origin_sic_name'])
