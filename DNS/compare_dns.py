from winrm import Session

session = Session('192.168.2.155', auth=('Administrator','SOME-long-P@$$WORD'))

# Show each DNS record for zone mzaran.local by HostName only
result = session.run_ps('Get-DnsServerResourceRecord -ZoneName "mzaran.local" -RRType "A" | Select HostName | foreach { $_.HostName }')

# Split DNS entries into a set of values
win_dns_set = set(result.std_out.decode("utf-8").splitlines())

# Set of values to compare - Can also be a function to compare a file or another source 
some_set = {"value1", "value2", "somehost"}


if __name__ == "__main__":
    # What doesn't exist in some_set but does in win_dns_set
    print(f"The servers that do not exist in list {win_dns_set.difference(some_set)}")
    # What exists in some_set and in win_dns_set
    print(f"The servers that do exist in list {win_dns_set.intersection(some_set)}")
