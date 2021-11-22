# windows_server_scripts
Python scripts to check against Windows 2022 host


Requires for local administrator (testing only)
winrm set winrm/config/client/auth '@{Basic="true"}'
winrm set winrm/config/service/auth '@{Basic="true"}'
winrm set winrm/config/service '@{AllowUnencrypted="true"}'
Restart-Service WinRM
