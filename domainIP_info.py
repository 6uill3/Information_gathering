#!/usr/bin/env python
# -*-coding: utf-8-*-


import argparse
import checker
import dns_info
import whois_info
import gui
# import my_logger


def arguments():
    """
    Manage the arguments
    :return the arguments:
    """
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-d', '--domain', action='store', help='The domain \
that is going to be fingerprinted')
    parser.add_argument('-df', '--domain_file', action='store', help='The \
file in where the domains are to be fingerprinted are stored')
    parser.add_argument('-i', '--ip', action='store', help='The ip that is \
going to be fingerprinted')
    parser.add_argument('-if', '--ip_file', action='store', help='The file in \
where the IPs are to be fingerprinted are stored')
    args = parser.parse_args()

    return args


def main():
    # logger.info('STARTING SCRIPT')
    args = arguments()
    if args.ip is not None:
        ip_list = list()
        ip_list.append(args.ip)
        ip_list = checker.check_ip(ip_list)
        if ip_list is not None:
            for ip in ip_list:
                gui.whois_command_line(whois_info.whois(ip))
                dns_info.ip_info(ip)
    elif args.domain is not None:
        domain_list = list()
        domain_list.append(args.domain)
        domain_list = checker.check_domain(domain_list)
        if domain_list is not None:
            for domain in domain_list:
                # gui.whois_command_line(whois_info.whois_old(domain))
                gui.whois_command_line(whois_info.whois(domain))
                dns_info.domain_info(domain)


if __name__ == '__main__':
    # logger = my_logger.get_logger()
    main()
