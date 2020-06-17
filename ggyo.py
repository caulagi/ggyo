#!/usr/bin/env python3
"""
Work with ansible-vault files
"""
import argparse
import os
import sys
from pathlib import Path

from ansible.constants import DEFAULT_VAULT_ID_MATCH
from ansible.parsing.vault import PromptVaultSecret, VaultEditor, VaultLib

# path where a list of decrypted files is maintained, so we can encrypt them again
CACHE_DIR = os.path.join(os.path.expanduser("~"), ".config", "ggyo")
CACHE_FILENAME = "run"


def _get_password():
    secret = PromptVaultSecret(prompt_formats=["Vault password: "])
    secret.load()
    return secret


def encrypt_files(input_dir, extension):
    secret = _get_password()
    with open(os.path.join(CACHE_DIR, CACHE_FILENAME)) as cache_file:
        for fi in cache_file:
            fi = fi.strip()
            print(f"Encrypting {fi}")
            v = VaultEditor(VaultLib([(DEFAULT_VAULT_ID_MATCH, secret)])).encrypt_file(
                fi, secret, output_file=f"{fi}.{extension}"
            )


def decrypt_files(input_dir, extension):
    secret = _get_password()
    Path(CACHE_DIR).mkdir(parents=True, exist_ok=True)
    with open(os.path.join(CACHE_DIR, CACHE_FILENAME), "w") as cache_file:
        for fi in Path(input_dir).glob(f"**/*.{extension}"):
            print(f"Decrypting {fi}")
            v = VaultEditor(VaultLib([(DEFAULT_VAULT_ID_MATCH, secret)])).decrypt_file(
                fi, output_file=os.path.splitext(fi)[0]
            )
            cache_file.write(f"{os.path.splitext(fi)[0]}\n")


def handle_arguments():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--extension",
        default="vault",
        help="extension type for vault files (default: %(default)s)",
    )
    parser.add_argument(
        "--input_dir",
        default=os.getcwd(),
        help="input directory for vault files (default: %(default)s)",
    )
    parser.add_argument("action", choices=["encrypt", "decrypt"])
    args = parser.parse_args()
    return (args.action, args.input_dir, args.extension)


if __name__ == "__main__":
    action, input_dir, extension = handle_arguments()
    if not os.path.isdir(input_dir):
        print(f"No such directory: {input_dir}")
        sys.exit(1)
    func = encrypt_files if action == "encrypt" else decrypt_files
    func(input_dir, extension)
