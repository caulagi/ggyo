# ggyo

A small python script to encrypt and decrypt ansible-vault files

## Usage

```shell
$ python3 -m venv venv
$ . ./venv/bin/activate
$ pip install ansible

$ ./ggyo.py -h
usage: ggyo.py [-h] [--extension EXTENSION] [--input_dir INPUT_DIR]
               {encrypt,decrypt}

Work with ansible-vault files

positional arguments:
  {encrypt,decrypt}

optional arguments:
  -h, --help            show this help message and exit
  --extension EXTENSION
                        extension type for vault files (default: vault)
  --input_dir INPUT_DIR
                        input directory for vault files (default: .)

# decrypt files ending with vault
$ ./ggyo.py decrypt --input_dir ~/jipu/src/anthos/workstations/std-gke-admin-wks-01
Vault password:
Decrypting /Users/pradip.caulagi/jipu/src/anthos/workstations/std-gke-admin-wks-01/admin-ws-config.yaml.vault
Decrypting /Users/pradip.caulagi/jipu/src/anthos/workstations/std-gke-admin-wks-01/ssh/std-gke-admin-wks-01.vault
Decrypting /Users/pradip.caulagi/jipu/src/anthos/workstations/std-gke-admin-wks-01/scripts/import_ova_to_vsphere.sh.vault
Decrypting /Users/pradip.caulagi/jipu/src/anthos/workstations/std-gke-admin-wks-01/scripts/gcov_env_std.sh.vault

# encrypt previously decrypted files
$ ./ggyo.py encrypt
Vault password:
Encrypting /Users/pradip.caulagi/jipu/src/anthos/workstations/std-gke-admin-wks-01/admin-ws-config.yaml
Encrypting /Users/pradip.caulagi/jipu/src/anthos/workstations/std-gke-admin-wks-01/ssh/std-gke-admin-wks-01
Encrypting /Users/pradip.caulagi/jipu/src/anthos/workstations/std-gke-admin-wks-01/scripts/import_ova_to_vsphere.sh
Encrypting /Users/pradip.caulagi/jipu/src/anthos/workstations/std-gke-admin-wks-01/scripts/gcov_env_std.sh
```
