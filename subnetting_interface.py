import subprocess

def main():
    while True:
        print("Welcome to the Subnetting Script Interface!")
        print("1. Subnet Calculation Script")
        print("2. IP Allocation Script")
        print("3. Exit")
        
        choice = input("Enter the number of the script you want to run (1/2) or enter 3 to exit: ")
        
        if choice == '1':
            print("\nSubnet Calculation Script:")
            print("This script calculates subnet details such as total IPs, usable IPs, subnet mask, and IP range.")
            ip_cidr = input("Enter IP address with CIDR notation (e.g. 192.168.100.1/24): ")
            
            subprocess.run(["python", "subnet_calculation.py", ip_cidr])
            
        elif choice == '2':
            print("\nIP Allocation Script:")
            print("This script calculates and displays network details for multiple departments.")
            
            subprocess.run(["python", "departments_ip_allocation.py"])
            
        elif choice == '3':
            print("Exiting the Subnetting Script Interface. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please select a valid option (1, 2, or 3).")

if __name__ == "__main__":
    main()
