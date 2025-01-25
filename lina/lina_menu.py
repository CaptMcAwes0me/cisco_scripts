# Description: This script contains the Lina menu and its options.



def lina_menu():
    while True:
        print("\n" + "=" * 80)
        print(" Lina Menu ".center(80, "="))
        print("=" * 80)
        print("1) Device Information")
        print("2) NAT (Network Address Translation)")
        print("3) Access Control (ACLs)")
        print("4) Inspection Features")
        print("5) VPN")
        print("6) High Availability (HA) / Failover")
        print("7) Traffic Analysis and Logging")
        print("8) Clustering")
        print("9) User Authentication and AAA")
        print("0) Exit")
        print("=" * 80)

        # Prompt the user for their choice
        choice = input("Select an option (0-9): ").strip()

        # Process the user's choice
        if choice == "1":
            print("\n" + "-" * 80)
            print("Accessing Device Information...".center(80))
            print("-" * 80)
            device_information()
        elif choice == "2":
            print("\n" + "-" * 80)
            print("Accessing NAT (Network Address Translation)...".center(80))
            print("-" * 80)
            registration_troubleshooting()
        elif choice == "3":
            print("\n" + "-" * 80)
            print("Accessing Access Control (ACLs)...".center(80))
            print("-" * 80)
            database_troubleshooting()
        elif choice == "4":
            print("\n" + "-" * 80)
            print("Accessing Inspection Features...".center(80))
            print("-" * 80)
            disk_usage_troubleshooting()
        elif choice == "5":
            print("\n" + "-" * 80)
            print("Accessing VPN...".center(80))
            print("-" * 80)
            cpu_usage_troubleshooting()
        elif choice == "6":
            print("\n" + "-" * 80)
            print("Accessing High Availability (HA) / Failover...".center(80))
            print("-" * 80)
            database_troubleshooting()
        elif choice == "7":
            print("\n" + "-" * 80)
            print("Accessing Traffic Analysis and Logging...".center(80))
            print("-" * 80)
            disk_usage_troubleshooting()
        elif choice == "8":
            print("\n" + "-" * 80)
            print("Accessing Clustering...".center(80))
            print("-" * 80)
            cpu_usage_troubleshooting()
        elif choice == "9":
            print("\n" + "-" * 80)
            print("Accessing User Authentication and AAA...".center(80))
            print("-" * 80)
            cpu_usage_troubleshooting()
        elif choice == "0":
            print("\nExiting the script. Goodbye!")
            break
        else:
            print("\n[!] Invalid choice. Please enter a number between 0 and 9.")
