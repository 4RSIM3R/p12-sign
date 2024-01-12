# PowerShell script to generate a self-signed certificate

# Replace these variables as needed
$numberOfDays = "365"
$privateKeyPass = "12345678"
$fileName = "certificate.p12"

# Create cert directory if it doesn't exist
$certDir = "cert"
if (-not (Test-Path -Path $certDir)) {
    New-Item -ItemType Directory -Path $certDir
}

# Generate a New Private Key with 2048-bit
openssl genpkey -algorithm RSA -out $certDir\private_key.pem -pkeyopt rsa_keygen_bits:2048

# Generate a CSR (Certificate Signing Request)
openssl req -new -key $certDir\private_key.pem -out $certDir\csr.pem

# Self-sign the CSR
openssl x509 -req -days $numberOfDays -in $certDir\csr.pem -signkey $certDir\private_key.pem -out $certDir\certificate.pem

# Export the Private Key with a passphrase
openssl rsa -in $certDir\private_key.pem -out $certDir\encrypted_private_key.pem -passout pass:$privateKeyPass

# Export to PKCS#12 Format
openssl pkcs12 -export -out $certDir\$fileName -inkey $certDir\encrypted_private_key.pem -in $certDir\certificate.pem -passin pass:$privateKeyPass -passout pass:$privateKeyPass

Write-Host "PKCS#12 file generated in cert directory: $fileName"
