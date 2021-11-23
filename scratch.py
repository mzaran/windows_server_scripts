from winrm import Session

session = Session('192.168.2.155', auth=('Administrator','SOME-long-P@$$WORD'))

# Show all DNS records with full details
#result = session.run_ps('Get-DnsServerResourceRecord -ZoneName "mzaran.local" -RRType "A"')

# Show each DNS record for zone mzaran.local by HostName only
result = session.run_ps('Get-DnsServerResourceRecord -ZoneName "mzaran.local" -RRType "A" | Select HostName | foreach { $_.HostName }')

# Bytes output
print(result.std_out)

# Split each hostname to a string in a list
print(result.std_out.decode("utf-8").splitlines())
