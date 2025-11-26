# Simple server to serve the docs folder
# This allows the website to load properly with fetch API

Write-Host "🚀 N8N Workflows Documentation Server" -ForegroundColor Cyan
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host ""

$port = 8080
$docsPath = Split-Path -Parent $MyInvocation.MyCommand.Path

Write-Host "Starting server on port $port..." -ForegroundColor Yellow
Write-Host "Open your browser to: http://localhost:$port" -ForegroundColor Green
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Gray
Write-Host ""

# Start Python's built-in HTTP server
Set-Location $docsPath
python -m http.server $port
