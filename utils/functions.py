# Module that contains several useful functions


def sha_encode(hash_string):
    """
    This function encodes a string with SHA encryption
    More info: https://pt.wikipedia.org/wiki/SHA-2

    :param hash_string: String to encrypt
    :type hash_string: str
    :return: String encrypted with encryption SHA-256
    :rtype: str
    """

    from hashlib import sha256

    # Encodes a string with SHA256 encoding
    sha = sha256(hash_string.encode()).hexdigest()

    return sha


def get_credentials(target, reset=False):
    """
    This functions fetches or resets credentials from the Windows Credential Manager
    Module win32cred info: http://timgolden.me.uk/pywin32-docs/win32cred.html
    Microsoft info: https://docs.microsoft.com/en-us/windows/win32/api/wincred/nf-wincred-creduipromptforcredentialsa

    :param target: Internet or network address
    :type target: str
    :param reset: boolean
    :type reset: bool
    :return: username and password
    :rtype: dict
    """

    import win32cred

    if not reset:
        # Fetches the existent credentials
        credentials = win32cred.CredRead(TargetName=target, Type=win32cred.CRED_TYPE_GENERIC)
        return {'username': credentials['UserName'], 'password': credentials['CredentialBlob'].decode('utf-16')}

    else:
        # Triggers a Windows pop-up & sets new credentials
        credentials = win32cred.CredUIPromptForCredentials(TargetName=target,
                                                           Flags=win32cred.CREDUI_FLAGS_GENERIC_CREDENTIALS |
                                                                 win32cred.CREDUI_FLAGS_ALWAYS_SHOW_UI |
                                                                 win32cred.CREDUI_FLAGS_PERSIST)
        return {'username': credentials[0], 'password': credentials[1]}


if __name__ == '__main__':
    print('sha', )
    print('user', get_credentials('git:https://github.com')['username'])
