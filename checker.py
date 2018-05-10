#!/usr/bin/env python
# -*-coding: utf-8-*-


import re


DOMAIN_REGEX = re.compile("(?:https:\/\/|http:\/\/){0,1}(?:www\.)\
{0,1}(.+\..+)")
IP_REGEX = re.compile("^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}\
(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")


def check_domain(domains):
    """
    Check if the format of the domains are valid
    :param domains:
    :return:
    """
    domain_list = list()
    if domains is not None:
        for domain in domains:
            match = DOMAIN_REGEX.match(domain)
            if match is not None:
                domain_list.append(match.group(1))
            else:
                print('Domain: {} is not well specified'.format(domain))
                # logger.warning('Domain: {} is not well \
# specified'.format(domain))
    return domain_list


def check_ip(ips):
    """
    Check if the format of the IPs are valid
    :param ips:
    :return:
    """
    ip_list = list()
    if ips is not None:
        for ip in ips:
            match = IP_REGEX.match(ip)
            if match is not None:
                ip_list.append(ip)
            else:
                print('IP: {} is not well specified'.format(ip))
                # logger.warning('Domain: {} is not well \
                # specified'.format(domain))
    return ip_list
