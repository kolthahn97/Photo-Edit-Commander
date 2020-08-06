function Test-Install {
    Param (
        [Parameter (Mandatory = $true)]
        [object] $ApplicationName
    )
	
	$application = Invoke-Expression "$ApplicationName --version"
	
	If($application.Length -gt 0) {
		Write-Output "`r`n$ApplicationName :`r`n"
		Write-Output $Application
		Write-Output "`r`nRequirement Satisfied: True`r`n"
	} Else {
		Write-Output "`r`nRequirement Satisfied: False"
		Write-Output "Installing now... "
		
		Invoke-Expression "python -m pip install $ApplicationName"
	}
}

Test-Install "jupyter"

Invoke-Expression "python -m pip install Pillow"
Invoke-Expression "python -m pip install numpy"
Invoke-Expression "python -m pip install argparse"
Invoke-Expression "jupyter nbconvert --to script *.ipynb"