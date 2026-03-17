def nmap(ip):
    var = f"nmap -A -p- {ip} -v"
    print("running nmap scan against{var}")
nmap(input("what ip would you like to scan? "))