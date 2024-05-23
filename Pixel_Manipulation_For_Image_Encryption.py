from PIL import Image
import numpy as np

def load_image(image_path):
    """Load an image and convert it to a NumPy array."""
    img = Image.open(image_path)
    return np.array(img)

def save_image(np_array, output_path):
    """Save a NumPy array as an image."""
    img = Image.fromarray(np_array)
    img.save(output_path)

def encrypt_image(image_array, key):
    """Encrypt an image using XOR and pixel swapping."""
    # XOR operation with key
    encrypted_array = np.bitwise_xor(image_array, key)
    
    # Swap pixels
    encrypted_array = encrypted_array[::-1]
    
    return encrypted_array

def decrypt_image(encrypted_array, key):
    """Decrypt an image by reversing the encryption steps."""
    # Reverse pixel swapping
    decrypted_array = encrypted_array[::-1]
    
    # XOR operation with key
    decrypted_array = np.bitwise_xor(decrypted_array, key)
    
    return decrypted_array

def main():
    # Paths to the input and output images
    input_image_path = 'input_image.png'
    encrypted_image_path = 'encrypted_image.png'
    decrypted_image_path = 'decrypted_image.png'

    # Encryption key (must be the same for encryption and decryption)
    key = 123  # Example key

    # Load the image
    image_array = load_image(input_image_path)

    # Encrypt the image
    encrypted_array = encrypt_image(image_array, key)
    save_image(encrypted_array, encrypted_image_path)
    print(f"Image encrypted and saved to {encrypted_image_path}")

    # Decrypt the image
    decrypted_array = decrypt_image(encrypted_array, key)
    save_image(decrypted_array, decrypted_image_path)
    print(f"Image decrypted and saved to {decrypted_image_path}")

if __name__ == "__main__":
    main()
