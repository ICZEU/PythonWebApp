<#
    .DESCRIPTION
        This script builds a docker container for this application and runs it.
        You need to have docker installed on this computer.
        This script is only intended to be used for development.
#>
$ErrorActionPreference = "Stop"
$old = docker images sermonwebapp -q
docker build . -t sermonwebapp
if ($old -ne $(docker images sermonwebapp -q)) {
    Write-Output "Deleting previously built image $old..."
    docker rmi $old
}
docker run --rm -p 5000:5000 -v "$($PSScriptRoot):/app" -it sermonwebapp
