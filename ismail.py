"""
    File name:
    Author: Aleksander Boldyrev
    Python Version: 3.3
"""

import re


def ismail(email):
    name = (email.split('@')[0])
    domain = email.split('@')[-1]


    # cond_a - '@' should be present in the mail only once
    if not len(email.split('@')) == 2:
        return False
    # cond_b - Name not longer than 128
    if not (0 < len(name) <= 128):
        return False

    # cond_c - Minimum domain length 3 symbols. Max domain length 256 symbols
    if not (3 <= len(domain) <= 256):
        return False

    # cond_d - There are no space in the domain
    if (' ' in domain):
        return False

    # cond_e - Dot should split domain on two or more none empty parts
    if '.' in domain and 0 in [len(prt) for prt in domain.split(".")]:
        return False

    # cond_f - Domain parts cannot have "-" at the beginning or at the end of the domain part
    for prt in domain.split("."):
        if re.search(r'^[-]|[-]$', prt):
            return False

    # cond_g - Possible symbols for domain a-z 0-9._- only
    for ch in domain:
        if not re.search(r'^[a-z0-9._-]$', ch):
            return False

    # cond_h - Possible symbols for username a-z0-9"._-!,: only
    for ch in name:
        if not re.search(r'^[A-Za-z0-9"._!,:-]$', ch):
            return False

    # cond_k - Pair of quotes is possible only
    if not len(name.split('"')) % 2 != 0:
        return False

    # cond_l - Symbols !,: should go inside the quotes "!,:"
    sub_name = (''.join(name.split("\"")[::2]))
    if not (not bool(re.search(r'[!,:]',  sub_name))):
        return False

    # cond_m - Two dot in the row unacceptable for the username ".."
    return '..' not in name

if __name__ == '__main__':
    if ismail(input('set Email : ')):
        print('valid Email')
    else:
        print('input ERROR')
