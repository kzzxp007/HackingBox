# versao 2 do codigo, adaptado pra termux e com senha e usuario
import time
import os
import hashlib
from colorama import Fore, Style, init
init(autoreset=True)
user = input("Qual e seu nome?  ")
print(Fore.RED + f"Welcome to HackingBox, {user}.")
time.sleep(2)
os.system("clear")
print(Fore.BLUE + "\n=====Oque vc deseja hoje?=====")
print("0. Atualizar termux")
print("1. DDoS")
print("2. ZPhisher")
print("3. NMAP")
print("4. SQLMap")
print("5. Metasploit")
print("6. GhostTrack")
print("7. Infect (Virus)")
print("8. Kali Linux")
print("9. TBomb")
print("10. CamPhish")
print("00. Sair")
try:
  rep = int(input("Insira sua opcão:  "))
except ValueError:
  print(Fore.RED + "Apenas números! (Ex: 1, 2, 3)")
  exit()

# atualizando
if rep == 0:
  os.system("pkg update && pkg upgrade -y")

# DDoS (DDoS-Ripper)
elif rep == 1:
  print(Fore.GREEN + "Instalando DDoS-Ripper")
  print("Clonar repositorio:")
  print("git clone https://github.com/palahsu/DDoS-Ripper.git")
  print("cd DDoS-Ripper")
  print("Permissão:")
  print("chmod +x DDoS-Ripper")
  print("Entrando:")
  print("python3 DRipper.py")

# ZPhisher
elif rep == 2:
  print(Fore.GREEN + "Clonar repositorio:")
  print("git clone https://github.com/htr-tech/zphisher")
  print("cd zphisher")
  print("Permissão:")
  print("chmod +x zphisher")
  print("Entrando:")
  print("bash zphisher.sh")

# NMAP
elif rep == 3:
  print("pkg install nmap")
  print("NMAP Instalado!")

# SQLMap
elif rep == 4:
  print(Fore.GREEN + "Clonar repositorio:")
  print("git clone https://github.com/sqlmapproject/sqlmap")
  print("cd sqlmap")
  print("python sqlmap.py -h")

# Metasploit
elif rep == 5:
  print(Fore.GREEN + "Atualizando termux")
  print("pkg update && pkg upgrade -y")
  print(Fore.GREEN + "Instalando git, curl e wget...")
  print("pkg install git curl wget -y")
  print(Fore.GREEN + "Clonando repositorio...")
  print("git clone https://github.com/rapid7/metasploit-framework.git")
  print(Fore.GREEN + "Entrando e instalando dependencias...")
  print("cd metasploit-framework")
  print("gem install bundler")
  print("bundle install --jobs=4")
  print("./msfconsole")
# GhostTrack
elif rep == 6:
  print("git clone https://github.com/HunxByts/GhostTrack.git")
  print("cd GhostTrack")
  print("pip3 install -r requirements.txt")
  print("python3 GhostTR.py")
elif rep == 7:
  print("CUIDADO!!")
  print("pkg install git -y")
  print("pip install lolcat")
  print("git clone https://github.com/noob-hackers/infect")
  print("cd $HOME")
  print("cd infect")
  print("bash infect.sh")
elif rep == 8:
  print("apt update")
  print("termux-setup-storage")
  print("pkg install wget")
  print("wget -O install-nethunter-termux https://offs.ec/2MceZWr")
  print("chmod +x install-nethunter-termux")
  print("./install-nethunter-termux")
  print("Apos a instalação:")
  print("nh")
elif rep == 9:
  print("git clone https://github.com/TheSpeedX/TBomb.git")
  print("cd TBomb")
  print("pip install -r requirements.txt")
  print("bash TBomb.sh")

elif rep == 10:
  print("git clone https://github.com/baradatipu/CamPhish")
  print("cd CamPhish")
  print("bash camphish.sh")
# Saindo / Else
elif rep == 00:
  print("Saindo...")
  exit()
else:
  print("Opção invalida!")
