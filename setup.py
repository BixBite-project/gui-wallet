from cx_Freeze import setup, Executable

setup(
    name = "wallet",
    version = "0.0.0.1",
    description = "BixbiteGUIWallet",
    executables = [Executable("wallet.py")]
)
