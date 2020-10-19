# Shell script to generate private/public keypair for ssh-authentication for password-less connecting to a remote server.

## Script taken from here: https://github.com/centic9/generate-and-send-ssh-key

## Usage:

The script expects some commandline arguments which specify which key should be transferred/created and 
where it should be sent to:

    -u (--user) <username>, default: $USER
    -f (--file) <file>,     default: ~/.ssh/id_test
    -h (--host) <hostname>, default: host
     
    -p (--port)    <port>, default: <default ssh port>
    -k (--keysize) <size>, default: 2048
    -t (--keytype) <type>, default: rsa
    
    -P(--passphrase) <key-passphrase>, default: <empty>

You should at least set `--user`, `--file`, and `--host`.  
If the key-file does not exist yet, a new key will be generated.

Example(from the folder where the script is):
Set permissions: sudo chmod +x generateSSH.sh
Create key-pair(please refer to the list above for all the possible options): ./generateSSH.sh --user bob --host myhost