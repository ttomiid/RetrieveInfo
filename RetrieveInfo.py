from os import system
from os import popen
from os import execv
from sys import executable
from sys import argv
from datetime import datetime

def restart_script():
    print("Restarting script...")
    python = executable
    execv(python, [python] + argv)


try:
    system("MODE 71,20")
    date_time = datetime.now()
    folder_name = input("Folder name: ")
    system(f"mkdir results_{folder_name}")

    # IPCONFIG
    ipconfig_file = open(f"results_{folder_name}/IPCONFIG.log", "w", encoding="utf-8")
    ipconfig = "ipconfig /allcompartments /all"
    output_ipconfig = popen(ipconfig).read()
    ipconfig_file.write(f"""
    {date_time}\n
    {output_ipconfig}
    """)
    ipconfig_file.close()

    # WHOAMI
    whoami_file = open(f"results_{folder_name}/WHOAMI.log", "w", encoding="utf-8")
    whoami = "whoami"
    output_whoami = popen(whoami).read()
    whoami_file.write(f"""
    {date_time}\n
    {output_whoami}
    """)
    whoami_file.close()

    # TASKLIST
    tasklist_file = open(f"results_{folder_name}/TASKLIST.log", "w", encoding="utf8")
    tasklist = "tasklist"
    output_tasklist = popen(tasklist).read()
    tasklist_file.write(f"""
    {date_time}\n
    {output_tasklist}
    """)
    tasklist_file.close()

    # SYSTEMINFO
    systeminfo_file = open(f"results_{folder_name}/SYSTEMINFO.log", "w", encoding="utf8")
    systeminfo = "systeminfo"
    output_systeminfo = popen(systeminfo).read()
    systeminfo_file.write(f"""
    {date_time}\n
    {output_systeminfo}
    """)
    systeminfo_file.close()

    # WINDOWS VERSION
    verWin_file = open(f"results_{folder_name}/WINDOWS_VERSION.log", "w", encoding="utf8")
    verWin = "ver"
    output_verWin = popen(verWin).read()
    verWin_file.write(f"""
    {date_time}\n
    {output_verWin}
    """)
    verWin_file.close()

    # PUBLIC IP
    public_ip_file = open(f"results_{folder_name}/PUBLIC_IP.log", "w", encoding="utf8")
    public_ip = "curl -s ifconfig.me/all"
    output_publicIP = popen(public_ip).read()
    public_ip_file.write(f"""
    \n{date_time}\n
    {output_publicIP}
    """)
    public_ip_file.close()

    # ALL CONNECTIONS
    allConnections_file = open(f"results_{folder_name}/ALL_CONNECTIONS.log", "w", encoding="utf8")
    allConnections = "netstat -q"
    output_allConnections = popen(allConnections).read()
    allConnections_file.write(f"""
    {date_time}\n
    {output_allConnections}
    """)
    allConnections_file.close()

    # GET MAC
    getMac_file = open(f"results_{folder_name}/MAC.log", "w", encoding="utf8")
    getMac = "getmac /v"
    output_getMac = popen(getMac).read()
    getMac_file.write(f"""
    {date_time}\n
    {output_getMac}
    """)
    getMac_file.close()

    # NETWORK INTERFACE STATISTICS
    ifaceStatistics_file = open(f"results_{folder_name}/IFACE_STATISTICS.log", "w", encoding="utf8")
    ifaceStatistics = "netstat -e"
    output_ifaceStatistics = popen(ifaceStatistics).read()
    ifaceStatistics_file.write(f"""
    {date_time}\n
    {output_ifaceStatistics}
    """)
    ifaceStatistics_file.close()

    # ROUTE TABLES
    routeTables_file = open(f"results_{folder_name}/ROUTE_TABLES.log", "w", encoding="utf8")
    routeTables = "netstat -r"
    output_routeTables = popen(routeTables).read()
    routeTables_file.write(f"""
    {date_time}\n
    {output_routeTables}
    """)
    routeTables_file.close()

    # DRIVERS
    drivers_file = open(f"results_{folder_name}/DRIVERS.log", "w", encoding="utf8")
    drivers = "driverquery"
    output_drivers = popen(drivers).read()
    drivers_file.write(f"""
    {date_time}\n
    {output_drivers}
    """)
    drivers_file.close()

    # CPU
    cpu_file = open(f"results_{folder_name}/CPU.log", "w", encoding="utf8")
    cpu = "wmic cpu list full"
    output_cpu = popen(cpu).read()
    cpu_file.write(f"""
    {date_time}\n
    {output_cpu}
    """)
    cpu_file.close()

    # BIOS
    bios_file = open(f"results_{folder_name}/BIOS.log", "w", encoding="utf8")
    bios = "wmic bios list full"
    output_bios = popen(bios).read()
    bios_file.write(f"""
    {date_time}\n
    {output_bios}
    """)
    bios_file.close()

    # RAM (MEMORYCHIP)
    memorychip_file = open(f"results_{folder_name}/MEMORYCHIP_RAM.log", "w", encoding="utf8")
    memorychip = "wmic memorychip list full"
    output_memorychip = popen(memorychip).read()
    memorychip_file.write(f"""
    {date_time}\n
    {output_memorychip}
    """)
    memorychip_file.close()

    # WINDOWS SERVICES
    servicesWin_file = open(f"results_{folder_name}/WINDOWS_SERVICES.log", "w", encoding="utf8")
    servicesWin = "sc query"
    output_servicesWin = popen(servicesWin).read()
    servicesWin_file.write(f"""
    {date_time}\n
    {output_servicesWin}
    """)
    servicesWin_file.close()

    # GROUP POLICY (GPRESULT)
    gpresult_file = open(f"results_{folder_name}/GROUP_POLICY.log", "w", encoding="utf8")
    gpresult = "gpresult /r"
    output_gpresult = popen(gpresult).read()
    gpresult_file.write(f"""
    {date_time}\n
    {output_gpresult}
    """)
    gpresult_file.close()

    # CACHE DNS
    cacheDNS_file = open(f"results_{folder_name}/CACHE_DNS.log", "w", encoding="utf8")
    cacheDNS = "ipconfig /displaydns"
    output_cacheDNS = popen(cacheDNS).read()
    cacheDNS_file.write(f"""
    {date_time}\n
    {output_cacheDNS}
    """)
    cacheDNS_file.close()

    # ARP TABLE
    arpTable_file = open(f"results_{folder_name}/ARP_TABLE.log", "w", encoding="utf8")
    arpTable = "arp -a"
    output_arpTable = popen(arpTable).read()
    arpTable_file.write(f"""
    {date_time}\n
    {output_arpTable}
    """)
    arpTable_file.close()

    # NBT CACHE
    nbtCache_file = open(f"results_{folder_name}/NBT_CACHE.log", "w", encoding="utf8")
    nbtCache = "nbtstat -c"
    output_nbtCache = popen(nbtCache).read()
    nbtCache_file.write(f"""
    {date_time}
    {output_nbtCache}
    """)
    nbtCache_file.close()

    # WINDOWS USERS
    usersWin_file = open(f"results_{folder_name}/WINDOWS_USERS.log", "w", encoding="utf8")
    usersWin = "net user"
    output_userWin = popen(usersWin).read()
    usersWin_file.write(f"""
    {date_time}\n
    {output_userWin}
    """)
    usersWin_file.close()

    # TIME ZONE
    timeZone_file = open(f"results_{folder_name}/TIME_ZONE.log", "w", encoding="utf8")
    timeZone = "tzutil /g"
    output_timeZone = popen(timeZone).read()
    timeZone_file.write(f"""
    {date_time}\n
    {output_timeZone}
    """)
    timeZone_file.close()

    # PROGRAMS
    programs_file = open(f"results_{folder_name}/PROGRAMS_WINDOWS.log", "w")
    programs = "winget list"
    output_programs = popen(programs).read()
    programs_file.write(f"""
    {date_time}\n
    {output_programs}
    """)
    programs_file.close()

    # WLAN INFORMATION
    wlan_all_file = open(f"results_{folder_name}/WLAN_INFORMATION.log", "w", encoding="utf8")
    wlan_all = "netsh wlan show all"
    output_wlan_all = popen(wlan_all).read()

    # SHOW NETWORKS WITH WLAN
    wlan_networks = "netsh wlan show networks"
    output_wlan_networks = popen(wlan_networks).read()

    # SHOW DRIVERS
    wlan_drivers = "netsh wlan show drivers"
    output_wlan_drivers = popen(wlan_drivers).read()

    # SHOW INTERFACES
    wlan_ifaces = "netsh wlan show interfaces"
    output_wlan_ifaces = popen(wlan_ifaces).read()

    # SHOW PROFILES
    wlan_profiles = "netsh wlan show profiles"
    output_wlan_profiles = popen(wlan_profiles).read()

    wlan_all_file.write(f"""
    {date_time}\n
    {output_wlan_all}\n

    ________________________________________

    {output_wlan_networks}\n

    ________________________________________

    {output_wlan_drivers}\n

    ________________________________________

    {output_wlan_ifaces}\n

    ________________________________________

    {output_wlan_profiles}

    """)
    wlan_all_file.close()


except FileNotFoundError as fnfe:
    print("Creating the “results” folder...\n")
    #system(f"mkdir results_{folder_name}")
    #restart_script()
except Exception as e:
    print(f"Ocurrio un error {e}", type(e))
except KeyboardInterrupt as ki:
    system("cls")
    print("Exiting...")
    input("\nPress enter to continue...")
else:
    print(f"""
    \nThe execution was successful, the results are in the “results_{folder_name}” folder.
    \nPress enter to continue...
    """)
    input()



# pyinstaller --onefile --icon="icon.ico" RetrieveInfo.py
# pyinstaller --onefile --noconsole --icon="icon.ico" RetrieveInfo.py