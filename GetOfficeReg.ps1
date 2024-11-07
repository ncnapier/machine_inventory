
########################################################################################################
# Define the registry path for Microsoft Office
$regPath = "HKLM:\SOFTWARE\Microsoft\Office\ClickToRun\Configuration"

# Retrieve the registration information
$clientVersion = (Get-ItemProperty -Path $regPath -Name "ClientVersionToReport").ClientVersionToReport
$productReleaseIds = (Get-ItemProperty -Path $regPath -Name "ProductReleaseIds").ProductReleaseIds
$platform = (Get-ItemProperty -Path $regPath -Name "Platform").Platform

# Output the information
Write-Output "Client Version: $clientVersion"
Write-Output "Product Release IDs: $productReleaseIds"
Write-Output "Platform: $platform"