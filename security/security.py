import boto3
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import traceback


def encrypting_password(parameter, public_key):
    try:
        if not parameter:
            return parameter
        encode_paramater = parameter.encode('utf-8')
        cipher_paramater = PKCS1_OAEP.new(key=public_key)
        encrypt_cipher = cipher_paramater.encrypt(encode_paramater)
        return encrypt_cipher
    except Exception as e:
        print(f"Error in Encrypting Password:- {traceback.format_exc()}")
        return None

def decrypting_paramter(paramater, private_key):
    try:
        if not paramater:
            return paramater
        cipher_parameter =  PKCS1_OAEP.new(key=private_key)
        decrypt_cipher = cipher_parameter.decrypt(paramater)
        decode_parameter = decrypt_cipher.decode('utf-8')
        return decode_parameter
    except Exception as e:
        print(f"Error in Decrypting Password:- {traceback.format_exc()}")
        return None

def read_keys():
    with open(r"public_pem.pem") as pu_file:
        read_pu = pu_file.read()
        if not read_pu:
            raise ValueError("Public key file is empty")
    pu_key = RSA.import_key(read_pu)

    with open(r"private_pem.pem") as pr_file:
        read_pr = pr_file.read()
        if not read_pr:
            raise ValueError("Private key file is empty")
    pr_key = RSA.import_key(read_pr)

    return pu_key, pr_key


pu, pr = read_keys()
enc = encrypting_password("jayname.   isds   ##2 dmine", pu)
print(f"----------------{enc}")
dec = decrypting_paramter(enc, pr)
print(f"----------------{dec}")
