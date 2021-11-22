from winrm import Session

session = Session('192.168.2.155', auth=('Administrator','SOME-long-P@$$WORD'))

result = session.run_ps('Get-DnsServerResourceRecord -ZoneName "mzaran.local" -RRType "A"')

print(result.std_out.decode("utf-8"))
