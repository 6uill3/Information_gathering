#!/usr/bin/env python
# *-* coding: utf-8 *-*


import pythonwhois  # https://pypi.python.org/pypi/pythonwhois


def whois(src):
    """

    :param src:
    :return:
    """
    try:
        short_resp = pythonwhois.get_whois(src)
        if 'whois_server' in short_resp.keys():
            server = ''.join(map(str, short_resp['whois_server']))
            large_raw_resp = pythonwhois.net.get_whois_raw(src, server=server)
            if len(large_raw_resp) != 0 and large_raw_resp is not None:
                large_raw_resp = ''.join(map(str, large_raw_resp)).split('\n')
                return parse_large_raw_response(large_raw_resp)
        else:
            whois_data = list()
            whois_data.append(short_resp)
            if len(whois_data) != 0 and whois_data is not None:
                return whois_data
    except pythonwhois.shared.WhoisException as e:
        return None


def parse_large_raw_response(whois_resp):
    """
    Parse a large raw answer of a whois query to a dictionary
    :param whois_resp: A list with the large raw whois answer to parse
    :return: A dictionary with the whois info
    """
    if whois_resp is not None and len(whois_resp) > 0:
        dict_response = dict()
        for record in whois_resp:
            if ':' in record:
                tmp = record.split(':')
                dict_response.update({tmp[0]: tmp[1]})
        return dict_response
    else:
        return None


