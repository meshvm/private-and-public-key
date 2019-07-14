import base64
import logging

from cryptography.exceptions import UnsupportedAlgorithm
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def demonstrate_asymmetric_string_encryption(plain_text):

    try:
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=4096,
            backend=default_backend()
        )
        public_key = private_key.public_key()

        # ENCRYPTION
        cipher_text_bytes = public_key.encrypt(
            plaintext=plain_text.encode('utf-8'),
            padding=padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA512(),
                label=None
            )
        )
        cipher_text = base64.urlsafe_b64encode(cipher_text_bytes)
        print("Encrypted Cipher Text = ", cipher_text, "\n")

        decrypted_cipher_text_bytes = private_key.decrypt(
            ciphertext=base64.urlsafe_b64decode(cipher_text),
            padding=padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA512(),
                label=None
            )
        )
        decrypted_cipher_text = decrypted_cipher_text_bytes.decode('utf-8')
        print("Decrypted Cipher text = ", decrypted_cipher_text, "\n")

    except UnsupportedAlgorithm:
        logger.exception("Asymmetric encryption failed")


if __name__ == '__main__':

    In = input("Enter a Message To Encrypt = ")
    print("Input Text = ", In, "\n")
    demonstrate_asymmetric_string_encryption(In)
