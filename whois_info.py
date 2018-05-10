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
        answer = pythonwhois.get_whois(source)
        whois_data.append(answer)
        if len(whois_data) != 0 and whois_data is not None:
            return whois_data
    except Exception as e:
        return None
