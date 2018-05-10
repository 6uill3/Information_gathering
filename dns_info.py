#!/usr/bin/env python
# -*-coding: utf-8-*-


import dns.resolver
import dns.reversename
import dns.query
import dns.zone
import gui


def domain_info(domain):
    """
    Harvest and print the different DNS records of a domain
    :param domain:
    :return:
    """
    gui.a_command_line(a_record(domain))
    gui.ns_command_line(ns_record(domain))
    gui.mx_command_line(mx_record(domain))
    gui.soa_command_line(soa_record(domain))
    gui.txt_command_line(txt_record(domain))
    # zone_transfer(domain)


def ip_info(ip):
    """

    :param ip:
    :return:
    """
    ptr_record(ip)


def a_record(domain):
    """

    :param domain:
    :return:
    """
    a_record_list = list()
    try:
        a_rec = dns.resolver.query(domain, 'A')
        for data in a_rec:
            a_record_list.append(data.to_text())
    except Exception:
        return None
    return a_record_list


def ns_record(domain):
    """

    :param domain:
    :return:
    """
    ns_record_dict = dict()
    try:
        ns_rec = dns.resolver.query(domain, 'NS')
        for data in ns_rec:
            data = str(data).rstrip('.')
            ns_record_dict.update({data: a_record(data)})
    except Exception as e:
        return None
    return ns_record_dict


def mx_record(domain):
    """

    :param domain:
    :return:
    """
    mx_record_dict = dict()
    try:
        mx_rec = dns.resolver.query(domain, 'MX')
        for data in mx_rec:
            dns_name = data.exchange.to_text().rstrip('.')
            preference = data.preference
            values = a_record(dns_name)
            values.append(str(preference))
            mx_record_dict.update({dns_name: values})
    except Exception as e:
        return None
    return mx_record_dict


def soa_record(domain):
    """

    :param domain:
    :return:
    """
    try:
        soa_rec = dns.resolver.query(domain, 'SOA')
        return soa_rec.rrset.items
    except Exception:
        return None


def txt_record(domain):
    """

    :param domain:
    :return:
    """
    txt_record_list = list()
    try:
        txt_rec = dns.resolver.query(domain, 'TXT')
        for data in txt_rec:
            txt_record_list.append(data)
    except Exception:
        return None
    return txt_record_list


def ptr_record(ip):
    """

    :param ip:
    :return:
    """
    try:
        address = dns.reversename.from_address(ip)
        return address
    except Exception as e:
        return None


def zone_transfer(domain):
    """

    :param domain:
    :return:
    """
    try:
        ns_record_dict = ns_record(domain)
        for key, values in ns_record_dict.items():
            if len(values) > 0:
                for value in values:
                    server = values
                z = dns.zone.from_xfr(dns.query.xfr(server, domain))
                names = z.nodes.keys()
                for n in names:
                    print(z[n].to_text(n))
    except Exception as e:
        print(e)
        return None