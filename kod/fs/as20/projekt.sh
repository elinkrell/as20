#
# Kan användas för följande:
# Kolla systemmiljö, testande
#
# Author: Frans Schartau/Elin Krell
# Last Update: 2026-01-08

echo "Välkommen till mitt RECON script för att kontrollera en Linux-miljö"

echo
echo "=== SYSTEMINFO ==="
uname -a

echo
echo "=== AKTUELL ANVÄNDARE ==="
echo $USER

echo
echo "=== ANVÄNDARE MED SHELL ==="
grep "sh$" /etc/passwd

echo
echo "=== NÄTVERK ==="
ip a | grep inet

echo
echo "=== LÄGG TILL FLERA TESTER  ==="

#
# skriv in dina kommandon för tester
#

lscpu
free -h

echo "What is your name?"
read name
echo "Nice to meet you, $name!"

echo "Choose an option:"
echo "1) Show current directory"
echo "2) Show files"
read choice

if [ "$choice" = "1" ]; then
	pwd
else
	ls
fi

