# Define the registry path
$regPath = "HKLM:\SOFTWARE\Natus\XLTEK"

# Retrieve the registration information
$serialNumber = (Get-ItemProperty -Path $regPath -Name "SerialNumber").SerialNumber
$optionPack = (Get-ItemProperty -Path $regPath -Name "OptionPack").OptionPack
$requestCode = (Get-ItemProperty -Path $regPath -Name "RequestCode").RequestCode
$activationKey = (Get-ItemProperty -Path $regPath -Name "ActivationKey").ActivationKey

# Output the information
Write-Output "Serial Number: $serialNumber"
Write-Output "Option Pack: $optionPack"
Write-Output "Request Code: $requestCode"
Write-Output "Activation Key: $activationKey"