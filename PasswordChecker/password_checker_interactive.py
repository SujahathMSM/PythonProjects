import requests
import hashlib
import getpass


def request_api_data(query_char):
    """Request data from HIBP API with the first 5 characters of the password hash."""
    url = f'https://api.pwnedpasswords.com/range/{query_char}'
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f'Error fetching: {response.status_code}, check the API and try again')
    return response


def get_password_leaks_count(hashes, hash_to_check):
    """Check if the password hash exists in the API response and return the count of leaks."""
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return int(count)
    return 0


def pwned_api_check(password):
    """Check if password exists in API response."""
    # Convert password to SHA1 hash
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


def main():
    """Interactive password checker."""
    print('===== Password Breach Checker =====')
    print('This tool checks if your password has been exposed in data breaches.')
    print('Your password is never sent over the network - only a partial hash is used.')
    print('Press Ctrl+C to exit at any time.\n')
    
    try:
        while True:
            password = getpass.getpass('Enter password to check (or press Enter to exit): ')
            if not password:
                break
                
            count = pwned_api_check(password)
            if count:
                print(f'⚠️ WARNING: This password was found in {count} data breaches!')
                print('You should change this password immediately!')
            else:
                print('✅ Good news! This password was not found in any known data breaches.')
            
            print('-' * 50)
    except KeyboardInterrupt:
        print('\nExiting password checker...')
    
    print('Thank you for using the Password Breach Checker!')


if __name__ == "__main__":
    main()