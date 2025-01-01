import time
import random

def mix_codes(codes):
    # Mix codes
    mixed = ''.join(random.sample(codes, len(codes)))
    return mixed

def main():
    # Asking the user to enter codes
    print("""
    my Channel Telegram = @Black_Edalat
    
    my ID Telegram = @taklorix
    """)
    user_input = input("Please enter your codes (comma separated): ")
    codes = user_input.split(',')

    print("Mixing codes...")
    time.sleep(3)  # Wait for 3 seconds

    mixed_code = mix_codes(codes)
    print(f"Your mixed code: {mixed_code}")

    # Generate link (here is only a hypothetical link)
    link = f"http://example.com/mixed_code/{mixed_code}"
    print(f"Mixed code link: {link}")

if __name__ == "__main__":
    main()
