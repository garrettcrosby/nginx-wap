Get-WebApplicationProxyApplication | Select-Object -Property BackendServerUrl,ExternalUrl,Name | Export-Csv -NoTypeInformation -Path 'INSERT\PATH\HERE'
