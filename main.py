import rsa

if __name__ == '__main__':
    message = 29

    public_key, private_key = rsa.calculate_keys()

    encrypted_message = rsa.encrypt(message, public_key)
    decrypted_message = rsa.decrypt(encrypted_message, private_key)

    assert message == decrypted_message
    print('Success')
