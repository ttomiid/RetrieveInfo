# **RetrieveInfo**

RetrieveInfo is an automated tool designed to extract and collect key information from Windows systems using native Command Prompt (CMD) commands. This utility is tailored for diagnostics, audits, and system analysis, generating `.LOG` files organized with the results of the executed commands, allowing for quick and efficient data review.

## **Key Features**
- **Automated Command Execution:** RetrieveInfo runs a wide range of Windows commands to collect detailed information about the system, network, hardware, users, and more.
- **Flexible Execution Modes:**
  - **Background Mode:** Performs analysis without user interaction.
  - **CMD Interface:** Prompts the user to specify the folder where results will be saved.
- **Structured Output:** Results are automatically saved in `.LOG` files organized in a user-specified or default folder.
- **Easily Extendable:** Can be adapted to include additional commands as needed.

## **Executed Commands**
RetrieveInfo uses the following commands to gather information:
- **Network:**
  - `ipconfig /allcompartments /all`
  - `netstat -q`
  - `netstat -e`
  - `netstat -r`
  - `ipconfig /displaydns`
  - `arp -a`
  - `nbtstat -c`
- **Hardware and System:**
  - `wmic cpu list full`
  - `wmic bios list full`
  - `wmic memorychip list full`
  - `systeminfo`
  - `driverquery`
  - `ver`
- **Users and Policies:**
  - `net user`
  - `gpresult /r`
- **Processes and Services:**
  - `tasklist`
  - `sc query`
- **Utilities and Diagnostics:**
  - `curl -s ifconfig.me/all`
  - `getmac /v`
  - `tzutil /g`
  - `winget list`
  - `netsh wlan show all`

## **Use Cases**
- Auditing systems in corporate environments.
- Diagnosing hardware and software configurations.
- Analyzing network and user settings.
- Monitoring group policies and installed drivers.

## **System Requirements**
- Operating System: Windows 10 or newer.
- Python 3.x installed.
- Administrator privileges (required for certain commands).

## **Installation and Usage**
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/RetrieveInfo.git
   ```
2. Navigate to the project directory:
   ```bash
   cd RetrieveInfo
   ```
3. Run the program:
   - **Background mode:**
     ```bash
     python retrieveinfo.py
     ```
   - **CMD mode (specifying the output folder):**
     ```bash
     python retrieveinfo.py <folder_name>
     ```

## **Output Structure**
The generated `.LOG` files are stored in a folder organized by date and time (in default mode) or in the folder specified by the user.

## **Important Notes**
- This tool is intended for **legitimate and ethical use only**. Ensure you have the necessary permissions before using it on any system.
- It is not designed for hacking or malicious purposes.

## **Contributions**
Contributions are welcome! If you want to improve RetrieveInfo or add new features, feel free to submit a pull request or open an issue.

## **License**
RetrieveInfo is licensed under the **GNU General Public License v3.0**. See the [LICENSE](LICENSE) file for more details.



🇪🇦# **RetrieveInfo**🇪🇦

RetrieveInfo es una herramienta automatizada para extraer y recopilar información clave de sistemas Windows utilizando comandos nativos del símbolo del sistema (CMD). Diseñada para diagnósticos, auditorías y análisis de sistemas, esta utilidad genera archivos `.LOG` organizados con los resultados de los comandos ejecutados, permitiendo una visualización rápida y eficiente de los datos.

## **Características principales**
- **Ejecución automatizada de comandos:** RetrieveInfo ejecuta una amplia lista de comandos de Windows para obtener información detallada del sistema, red, hardware, usuarios, y más.
- **Modo de ejecución flexible:**
  - **Segundo plano:** Realiza el análisis sin interacción del usuario.
  - **Interfaz CMD:** Solicita al usuario el nombre de la carpeta donde se almacenarán los resultados.
- **Salida estructurada:** Los resultados se almacenan en archivos `.LOG` organizados en una carpeta especificada por el usuario o predeterminada.
- **Ampliación sencilla:** Puede adaptarse fácilmente para incluir comandos adicionales según las necesidades.

## **Comandos ejecutados**
RetrieveInfo utiliza los siguientes comandos para recopilar información:
- **Red:**
  - `ipconfig /allcompartments /all`
  - `netstat -q`
  - `netstat -e`
  - `netstat -r`
  - `ipconfig /displaydns`
  - `arp -a`
  - `nbtstat -c`
- **Hardware y sistema:**
  - `wmic cpu list full`
  - `wmic bios list full`
  - `wmic memorychip list full`
  - `systeminfo`
  - `driverquery`
  - `ver`
- **Usuarios y políticas:**
  - `net user`
  - `gpresult /r`
- **Procesos y servicios:**
  - `tasklist`
  - `sc query`
- **Utilidades y diagnóstico:**
  - `curl -s ifconfig.me/all`
  - `getmac /v`
  - `tzutil /g`
  - `winget list`
  - `netsh wlan show all`

## **Casos de uso**
- Auditorías de sistemas en entornos corporativos.
- Diagnóstico de hardware y software.
- Análisis de configuraciones de red y usuarios.
- Monitoreo de políticas de grupo y controladores instalados.

## **Requisitos del sistema**
- Sistema operativo: Windows 10 o superior.
- Python 3.x instalado.
- Privilegios de administrador (requeridos para ciertos comandos).

## **Instalación y uso**
1. Clona este repositorio:
   ```bash
   git clone https://github.com/tuusuario/RetrieveInfo.git
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd RetrieveInfo
   ```
3. Ejecuta el programa:
   - **Modo segundo plano:**
     ```bash
     python retrieveinfo.py
     ```
   - **Modo CMD (especificando carpeta de salida):**
     ```bash
     python retrieveinfo.py <nombre_carpeta>
     ```

## **Estructura de salida**
Los archivos `.LOG` generados se almacenan en una carpeta organizada por fecha y hora (en modo predeterminado) o en la carpeta especificada por el usuario.

## **Notas importantes**
- Esta herramienta está diseñada exclusivamente para **uso legítimo y ético**. Asegúrate de contar con los permisos necesarios antes de utilizarla en cualquier sistema.
- No está diseñada para usarse como herramienta de hacking o con fines maliciosos.

## **Contribuciones**
¡Las contribuciones son bienvenidas! Si deseas mejorar RetrieveInfo o agregar nuevas funcionalidades, no dudes en enviar un pull request o abrir un issue.

## **Licencia**
RetrieveInfo se distribuye bajo la licencia **GNU General Public License v3.0**. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---
