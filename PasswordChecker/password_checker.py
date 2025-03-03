import requests
import hashlib
import sys


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


def main(args):
    """Main function to check passwords."""
    print('Checking if your passwords have been pwned...')
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'Password "{password}" was found {count} times... You should change your password!')
        else:
            print(f'Password "{password}" was NOT found. Carry on!')
    return 'Done!'


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Remove the script name from arguments
        sys.argv.pop(0)
        main(sys.argv)
    else:
        print('Please provide passwords to check as command line arguments')
        print('Example: python password_checker.py password1 password2 password3')