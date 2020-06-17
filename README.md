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
  {encrypt,decrypt}     Encrypt previously unvaulted files

optional arguments:
  -h, --help            show this help message and exit
  --extension EXTENSION
                        extension type for vault files (default: vault)
  --input_dir INPUT_DIR
                        input directory for vault files (default: .)
  
# decrypt files ending with vault
$  ./ggyo.py decrypt --input_dir ~/jipu/src/anthos

# encrypt previously decrypted files
$ ./ggyo.py encrypt --input_dir ~/jipu/src/anthos
```
