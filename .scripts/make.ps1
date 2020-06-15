param(
  [Parameter(Mandatory = $True)][System.String]$Action = '',

  [System.String]$Py = 'pip',
  [System.String]$Pip = 'python',

  [System.String]$Project = 'python_template',

  [System.String]$Mode = 'mod', # can be app|mod
  [System.String]$Path = '', # used for mkdir
  [System.String]$ArgumentList = '',
  [System.String]$Command = '',
  [System.String]$GoOs = 'linux',
  [System.String]$GoArch = 'amd64',
  [System.String]$LdFlags = '',
  # [System.String[]]$LdFlags = @(),
  [System.String]$O = '',
  [System.String]$Src = '.\main.o'
)

# function GoBuild() {
#   param(
#     [Parameter(Mandatory = $True)][System.String]$Command,
#     [Parameter(Mandatory = $True)][System.String]$GoOs,
#     [Parameter(Mandatory = $True)][System.String]$GoArch,
#     [Parameter(Mandatory = $True)][System.String]$LdFlags,
#     [Parameter(Mandatory = $True)][System.String]$O,
#     [Parameter(Mandatory = $True)][System.String]$Src
#   )

#   $env:GOOS = $GoOs;
#   $env:GOARCH = $GoArch;

#   $GoCommand = "$Command"
#   $GoCommandArray = $GoCommand.Split(' ')

#   Write-Host -ForegroundColor Green "`$env:GOOS = $GoOs; `$env:GOARCH = $GoArch; $GoCommand -ldflags=`"$LdFlags`" -o $O $Src"

#   Start-Process -Filepath $GoCommandArray[0] -ArgumentList ($GoCommandArray[1..($GoCommandArray.Length - 1)] + " -ldflags `"$LdFlags`" -o $O $Src") -NoNewWindow -PassThru -Wait
# }

# function GoConfigure() {
#   if (-not (Test-Path ".\.git\hooks\pre-commit" -PathType Leaf)) {
#     $CurentDirectory = (Get-Location).Path;
#     try {
#       Set-Location $CurentDirectory; New-Item -ItemType SymbolicLink -Path .\.git\hooks\pre-commit -Target .\.scripts\pre-commit.sh;
#     }
#     catch {
#       Write-Host -ForegroundColor Green "The following step requires elevated rights. Unfortunately Windows does not allow creating symlinks unless running the command with eleveated rights.";
#       Write-Host -ForegroundColor Green "We will open a PowerShell console running with Administrator rigths. Please run the following command in that console, then close it.";
#       Write-Host '';
#       Write-Host -ForegroundColor Yellow  "Set-Location $CurentDirectory; New-Item -ItemType SymbolicLink -Path .\.git\hooks\pre-commit -Target .\.scripts\pre-commit.sh;";
#       Write-Host '';
#       read-host 'Press ENTER to continue...';
#       Start-Process -FilePath "powershell" -Verb RunAs;
#     }
#   }

# }

function PyInit() {
  Rename-Item -Path .\python_template -NewName $Project
  # TODO:
  # sed -e 's/python_template/$(PROJECT)/g' -i Makefile.mod.include
	# sed -e 's/python_template/$(PROJECT)/g' -i setup.py
}

# function GoMkDir() {
#   param(
#     [Parameter(Mandatory = $True)][System.String]$Path
#   )
#   New-Item -Type Directory -Path $Path -Force;
# }

# function GoRmDir() {
#   param(
#     [Parameter(Mandatory = $True)][System.String]$Path
#   )
#   if (Test-Path $Path -PathType Container) {
#     Remove-Item -Path $Path -Recurse -Force;
#   }
# }

# function GoTest() {
#   param(
#     [Parameter(Mandatory = $True)][System.String]$Command
#   )
#   $Tests = Get-Childitem -Path . -Include *_test.go -File -Recurse -ErrorAction SilentlyContinue | ForEach-Object {
#     "." + (Split-Path -Path $$_).Replace((Get-Location).Path, "") + "\..."
#   } | Sort-Object -Unique;
#   $GoCommand = "$Command $Tests"
#   $GoCommandArray = $GoCommand.Split(' ')
#   Write-Host -ForegroundColor Green $GoCommand
#   Start-Process -Filepath $GoCommandArray[0] -ArgumentList $GoCommandArray[1..($GoCommandArray.Length - 1)] -NoNewWindow -PassThru -Wait
# }

switch ($Action.ToLower()) {
  # 'build' {
  #   GoBuild -Command $Command -GoOs $GoOs -GoArch $GoArch -LdFlags $LdFlags -O $O -Src $Src;
  #   break;
  # }
  # 'configure' { GoConfigure; break; }
  'init' { PyInit; break; }
  # 'mkdir' { GoMkDir -Path $Path; break; }
  # 'rmdir' { GoRmDir -Path $Path; break; }
  # 'test' { GoTest -Command "$Command"; break; }
  default { Write-Host -ForegroundColor Red "No good action chosen"; exit 1; }
}
