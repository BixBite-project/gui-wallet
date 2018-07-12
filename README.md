# Bixbite GUI Wallet

Copyright (c) 2017, Sumokoin.org
Copyright (c) 2018, Bixbite.pro

**One of the most easy-to-use, intuitive GUI (full) wallets in crypto.**

![](https://www.sumokoin.org/images/sumokoin-gui-wallet-v0.0.1-b2.png)


# Installation & running from source codes

1. Clone the repo:
		
		git clone https://github.com/BixBite-project/gui-wallet gui-wallet

2. Install dependencies (with Python 2.7):

	* Generally, you can use Python `pip` to install required components:
		
			pip install PySide, requests, psutil
	
	* or
			
			pip install -r requirements.txt 
	
	* On some OSes, PySide may be required to install from pre-built packages. For example, on Ubuntu 16.04, install PySide with the following command:
			
			sudo apt install python-pyside


3. Download Bixbite binaries from [Bixbite repo](https://github.com/BixBite-project/bixbite) and put it to `Resources/bin` sub-directory.

4. Run the wallet (Python 2.7):
		
		cd /path/to/gui-wallet
		python wallet.py
