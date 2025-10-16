# ============================================
# PowerShell script to build server-ready PLC logger .exe
# ============================================

# Navigate to your project folder
cd "H:\PLC Programs\plc_logger"

# --- Step 1: Clean previous builds ---
if (Test-Path .\build) { Remove-Item -Recurse -Force .\build }
if (Test-Path .\dist) { Remove-Item -Recurse -Force .\dist }

# --- Step 2: Ensure required folders exist ---
$requiredFolders = @("logs", "charts")
foreach ($folder in $requiredFolders) {
    if (-not (Test-Path $folder)) {
        New-Item -ItemType Directory -Path $folder
        Write-Host "Created folder: $folder"
    }
}

# --- Step 3: Ensure config template exists ---
if (-not (Test-Path "config_template.py")) {
    Write-Host "Warning: config_template.py not found. Copy manually if needed."
}

# --- Step 4: Build .exe with PyInstaller using hooks ---
# Hooks folder ensures all local modules (email_outlook, plc_comm, alerts, etc.) are included automatically
pyinstaller --onefile --name plc_logger main.py `
--additional-hooks-dir hooks `
--noconfirm

# --- Step 5: Notify user ---
Write-Host "Build complete. Executable located in dist\plc_logger.exe"
Write-Host "Remember to copy your local config.py to the server folder before running."
Write-Host "Logs and charts folders will be used/created automatically by the executable."
