param(
  [Parameter(Mandatory = $True)][System.String]$Action = '',

  [System.String]$Py = 'pip',
  [System.String]$Pip = 'python',

  [System.String]$Project = 'hello',

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

$DefaultProject = 'py_greet'

function PyInit() {
  if ($Project -ne $DefaultProject) {
    Rename-Item -Path .\py_greet -NewName $Project
    Get-ChildItem -Path . -Recurse -File |
      Select-String -Pattern "py_greet" |
      Select-Object -Unique Path | ForEach-Object {
        (Get-Content $_.Path) |
          Foreach-Object {$_ -replace $DefaultProject, $Project}  |
          Out-File $_.Path
      }
  }
}

function PyRmDir() {
  param(
    [Parameter(Mandatory = $True)][System.String]$Path
  )
  if (Test-Path $Path -PathType Container) {
    Remove-Item -Path $Path -Recurse -Force;
  }
}

switch ($Action.ToLower()) {
  'init' { PyInit; break; }
  'rmdir' { PyRmDir -Path $Path; break; }
  default { Write-Host -ForegroundColor Red "No good action chosen"; exit 1; }
}
