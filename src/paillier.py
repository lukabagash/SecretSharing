from phe import paillier


def compute_average_with_paillier(data):
    """
    Compute the average of data using Paillier encryption.
    """

    public_key, private_key = paillier.generate_paillier_keypair()

    # Encrypt the data
    encrypted_data = [public_key.encrypt(x) for x in data]

    # Compute the sum of encrypted data
    encrypted_sum = sum(encrypted_data)

    # Compute the average in encrypted form
    encrypted_avg = encrypted_sum / len(data)

    # Decrypt the average
    average = private_key.decrypt(encrypted_avg)

    return average