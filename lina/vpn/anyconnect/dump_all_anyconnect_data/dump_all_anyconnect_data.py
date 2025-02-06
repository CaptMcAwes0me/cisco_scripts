import os
from datetime import datetime
from lina.vpn.anyconnect.anyconnect_config.anyconnect_config import anyconnect_config
from lina.vpn.anyconnect.vpn_sessiondb_anyconnect_dump.vpn_sessiondb_anyconnect_dump \
    import vpn_sessiondb_anyconnect_dump
from lina.vpn.anyconnect.crypto_ca_certificates.crypto_ca_certificates import crypto_ca_certificates
from lina.vpn.anyconnect.crypto_ca_trustpoint.crypto_ca_trustpoint import crypto_ca_trustpoint
from lina.vpn.anyconnect.crypto_ca_trustpool.crypto_ca_trustpool import crypto_ca_trustpool
from lina.vpn.anyconnect.crypto_ca_crls.crypto_ca_crls import crypto_ca_crls
from lina.vpn.anyconnect.ssl_cipher.ssl_cipher import ssl_cipher
from lina.vpn.anyconnect.ssl_information.ssl_information import ssl_information
from lina.vpn.anyconnect.ssl_errors.ssl_errors import ssl_errors


def dump_all_anyconnect_data():
    """Gathers output from all AnyConnect-related commands and writes them to a log file under
    /var/log/fp_troubleshooting_data."""

    # Define the directory path
    troubleshooting_dir = "/var/log/fp_troubleshooting_data"

    # Check if the directory exists, if not, create it
    if not os.path.exists(troubleshooting_dir):
        try:
            os.makedirs(troubleshooting_dir)
            print(f"[+] Created directory: {troubleshooting_dir}")
        except Exception as e:
            print(f"[!] Error creating directory: {e}")
            return

    # Generate timestamp for the log file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(troubleshooting_dir, f"{timestamp}_anyconnect_dump.log")

    try:
        # Gather outputs
        data_to_dump = [
            ("AnyConnect Configuration", anyconnect_config(suppress_output=True)),
            ("VPN Session Database", vpn_sessiondb_anyconnect_dump(suppress_output=True)),
            ("Crypto CA Certificates", crypto_ca_certificates(suppress_output=True)),
            ("Crypto CA Trustpoints", crypto_ca_trustpoint(suppress_output=True)),
            ("Crypto CA Trustpool", crypto_ca_trustpool(suppress_output=True)),
            ("Crypto CA CRLs", crypto_ca_crls(suppress_output=True)),
            ("SSL Cipher", ssl_cipher(suppress_output=True)),
            ("SSL Information", ssl_information(suppress_output=True)),
            ("SSL Errors", ssl_errors(suppress_output=True))
        ]

        # Write all outputs to the log file
        with open(log_file, "w") as f:
            for title, output in data_to_dump:
                f.write(f"{'=' * 80}\n")
                f.write(f"{title}\n")
                f.write(f"{'-' * 80}\n")
                f.write(f"{output}\n")
                f.write(f"{'=' * 80}\n\n")

        print(f"\n[+] All AnyConnect data written to: {log_file}")

    except Exception as e:
        print(f"[!] Error writing AnyConnect data to file: {e}")
