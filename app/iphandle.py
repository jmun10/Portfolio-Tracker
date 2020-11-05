from flask import request
import socket
import tldextract

# takes in request object and returns domain as a string
def getDomain(request):
    try:
        ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
        domain = socket.gethostbyaddr(ip)[0]
    except Exception as e:
        print(e)
        domain = None

    return domain


def filterDomains(domain):
    """ checks if any lines in ignore_list.txt are present in domain string input.
        if so, function returns None. otherwise function returns unmodified domain.

        function assumes 'ignore_list.txt' is located in same directory
    """

    if not domain:
        return None

    # may need to change path
    with open('./resources/ignore_list.txt') as r:
        for line in r:
            # do not character match newline
            if line.rstrip() in domain:
                return None

    return domain


def parseDomains(domain):
    """ Needs tldextract installed
        Add to requirements.txt?

        Returns simplified domain as string. 
        If domain is none, returns none
    """
    if domain is not None:
        extract = tldextract.extract(domain).registered_domain
        if not extract:
            return None

        return extract

    return None
    