#!/usr/bin/env python
# *-* coding: utf-8 *-*


import pythonwhois  # https://pypi.python.org/pypi/pythonwhois


def whois(source):
    """

    :param source:
    :return:
    """
    try:
        whois_data = list()
        short_answer = pythonwhois.get_whois(source)
        if short_answer.keys()
        server = ''.join(map(str, short_answer['whois_server']))
        large_raw_answer = pythonwhois.net.get_whois_raw(source, server=server)
        parsed_large_raw_answer = pythonwhois.parse.parse_raw_whois(large_raw_answer)
        whois_data.append(parsed_large_raw_answer)
        if len(whois_data) != 0 and whois_data is not None:
            return whois_data
    except pythonwhois.shared.WhoisException as e:
        return None


def whois_old(source):
    """

    :param source:
    :return:
    """
    try:
        whois_data = list()
        short_answer = pythonwhois.get_whois(source)
        whois_data.append(short_answer)
        if len(whois_data) != 0 and whois_data is not None:
            return whois_data
    except pythonwhois.shared.WhoisException as e:
        return None


def get_whois_sever(source):
    """

    :param source:
    :return:
    """
    try:
        server = pythonwhois.net.get_root_server(source)
        print(server)
    except Exception as e:
        print('No server')
