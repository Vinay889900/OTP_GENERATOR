import random
import string

def generate_otp(length=6, otp_type='numeric'):
    if otp_type == 'numeric':
        characters = string.digits
    elif otp_type == 'alphanumeric':
        characters = string.ascii_letters + string.digits
    else:
        raise ValueError("Invalid otp_type. Choose 'numeric' or 'alphanumeric'.")
    
    otp = ''.join(random.choice(characters) for _ in range(length))
    return otp

def main():
    # Input OTP type from user
    otp_type = input("Enter OTP type ('numeric' or 'alphanumeric'): ").strip().lower()
    
    # Validate OTP type
    if otp_type not in ['numeric', 'alphanumeric']:
        print("Invalid OTP type. Please choose 'numeric' or 'alphanumeric'.")
        return
    
    # Input OTP length from user
    otp_length = input("Enter OTP length: ").strip()
    
    # Validate OTP length
    if not otp_length.isdigit():
        print("Invalid OTP length. Please enter a valid integer.")
        return
    
    otp_length = int(otp_length)  # Convert to integer
    
    # Generate the OTP
    otp = generate_otp(length=otp_length, otp_type=otp_type)
    print("Your OTP is:", otp)

if __name__ == "__main__":
    main()
