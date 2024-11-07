$remoteComputer = "VTHHEEG-1"
$scriptPath = "C:\Users\napienc2\code\GetNatusInfo.ps1"
$credential = Get-Credential

Invoke-Command -ComputerName $remoteComputer -FilePath $scriptPath -Credential $credential

