# Description: This script contains the registration troubleshooting menu.

from core.utils import flush_stdin
from firepower.registration.verify_connectivity.verify_connectivity import verify_connectivity
from firepower.registration.bandwidth_test.bandwidth_test import run_bandwidth_test
from firepower.registration.sftunnel_conf.sftunnel_conf import sftunnel_conf
from firepower.registration.sftunnel_json.sftunnel_json import sftunnel_json
from firepower.registration.sftunnel_certificate.sftunnel_certificate import sftunnel_certificate
from firepower.registration.registration_log_filter.registration_log_filter import grep_logs
from firepower.database.em_peers.em_peers import em_peers


def registration_troubleshooting():
    while True:  # Replace recursion with a loop for better performance
        flush_stdin()  # Ensure the input buffer is clean
        print("\n" + "=" * 80)
        print(" Registration Menu ".center(80, "="))
        print("=" * 80)
        print("1) Verify Connectivity")
        print("2) Run Bandwidth Test")
        print("3) Check sftunnel.conf")
        print("4) Check sftunnel.json")
        print("5) Check EM Peers Table")
        print("6) Check sftunnel Certificate")
        print("7) Gather Logs")
        print("0) Return to Main Menu")
        print("\n" + "*" * 80)
        print("Note: Options 1 and 2 are meant to be ran on both the FMC and FTD simultaneously.")
        print("*" * 80)

        # Prompt for the user's choice
        choice = input("Enter your choice (0-7): ").strip()

        # Process the user's choice
        if choice == '1':
            print("\n" + "-" * 80)
            print("Verifying Connectivity...".center(80))
            print("-" * 80)
            verify_connectivity()
        elif choice == '2':
            print("\n" + "-" * 80)
            print("Running Bandwidth Test...".center(80))
            print("-" * 80)
            run_bandwidth_test()
        elif choice == '3':
            print("\n" + "-" * 80)
            print("Checking sftunnel.conf...".center(80))
            print("-" * 80)
            sftunnel_conf()
        elif choice == '4':
            print("\n" + "-" * 80)
            print("Checking sftunnel.json...".center(80))
            print("-" * 80)
            sftunnel_json()
        elif choice == '5':
            print("\n" + "-" * 80)
            print("Checking EM Peers Table...".center(80))
            print("-" * 80)
            em_peers()
        elif choice == '6':
            print("\n" + "-" * 80)
            print("Checking sftunnel Certificate...".center(80))
            print("-" * 80)
            sftunnel_certificate()
        elif choice == '7':
            print("\n" + "-" * 80)
            print("Gathering Logs...".center(80))
            print("-" * 80)
            grep_logs()
        elif choice == '0':
            print("\nReturning to main menu...")
            break
        else:
            print("\n[!] Invalid choice. Please enter a number between 0 and 7.")
