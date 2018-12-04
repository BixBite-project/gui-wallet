from cx_Freeze import setup, Executable

setup(
    name = "wallet",
    version = "0.0.0.2",
    description = "BixbiteGUIWallet",
    executables = [Executable("wallet.py")]
)


pyinstaller wallet.py --icon=Resources\icons\bixbite.ico --windowed
pyinstaller --onefile --windowed --icon=bixbite.ico wallet.py

get-FileHash .\bootstrap.min.css | Format-List