#!/bin/bash

# Replace these variables as needed
numberOfDays=365
privateKeyPass="your_private_key_password"
fileName="your_filename.p12"

# Generate a New Private Key
openssl genpkey -algorithm RSA -out private_key.pem

# Generate a CSR (Certificate Signing Request)
# Note: You will be prompted to enter the distinguished name fields
openssl req -new -key private_key.pem -out csr.pem

# Self-sign the CSR
openssl x509 -req -days $numberOfDays -in csr.pem -signkey private_key.pem -out certificate.pem

# Export the Private Key with a passphrase
openssl rsa -in private_key.pem -out encrypted_private_key.pem -passout pass:$privateKeyPass

# Export to PKCS#12 Format
openssl pkcs12 -export -out $fileName -inkey encrypted_private_key.pem -in certificate.pem -passin pass:$privateKeyPass -passout pass:$privateKeyPass

# Cleanup
rm private_key.pem csr.pem encrypted_private_key.pem certificate.pem

echo "PKCS#12 file generated: $fileName"