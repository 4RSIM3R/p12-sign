from pyhanko.pdf_utils.incremental_writer import IncrementalPdfFileWriter
from pyhanko.sign import signers, fields
from pyhanko import stamp
import fitz  # For metadata modification
from pyhanko.pdf_utils import text, images
from pyhanko.sign.validation import validate_pdf_signature, ValidationContext, KeyUsageConstraints

doc = fitz.open("example.pdf")

page_width = doc[0].mediabox.width  # Assuming you're adding the field to the first page
page_height = doc[0].mediabox.height


page_width = int(page_width)
page_height = int(page_height)
sign_x = int(100)
sign_y = int(100)
ppi = 72
x1 = int(sign_x * (ppi / 25.4))
y1 = int((page_height * (ppi / 25.4)) - (sign_y * (ppi / 25.4)))
x2 = int(x1 + 200)
y2 = int((page_height * (ppi / 25.4)) - (sign_y * (ppi / 25.4) + 80))

# Load the PKCS#12 file and signer
signer = signers.SimpleSigner.load_pkcs12(
    pfx_file="cert/certificate.p12",
    passphrase=b"12345678"  # Replace with your actual passphrase
)

# Open the PDF file to be signed
with open("example.pdf", "rb") as pdf_file:
    w = IncrementalPdfFileWriter(pdf_file, strict=False)

    fields.append_signature_field(
            w, sig_field_spec=fields.SigFieldSpec(
                'Signature', box=(x1, y1, x2, y2)
            )
        )

    meta = signers.PdfSignatureMetadata(field_name="Signature")
    

    pdf_signer = signers.PdfSigner(
        meta, 
        signer=signer, 
        stamp_style=stamp.StaticStampStyle(
            background=images.PdfImage('assets/digital_stamp.png'),
            border_width=0,
        ),
        timestamper=None
    )

    with open("signed.pdf", "wb") as output_file:
        pdf_signer.sign_pdf(
            w, 
            output=output_file,
        )
