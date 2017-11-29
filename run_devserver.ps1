<#
    .DESCRIPTION
        This script builds the Python runtime environment within a Docker container.
        The Flask web app is started with the development server.

    .NOTES
        Don't use this development server in production.
        The script is only for a development environment at Windows.
        It requires Docker for Windows installed on the local computer.
#>
$ErrorActionPreference = "Stop"
docker build . -t sermonwebapp
docker run --rm -it -p 5000:5000 -v "$($PSScriptRoot):c:/App" sermonwebapp