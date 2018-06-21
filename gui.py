#!/usr/bin/env python
# -*-coding: utf-8-*-


def a_command_line(record):
    """

    :param record:
    :return:
    """
    record_type = 'A RECORD'
    print('-' * (len(record_type) + 1))
    print(record_type)
    print('-' * (len(record_type) + 1))
    if record is not None:
        for value in record:
            print(value)
    else:
        print('No {} record'.format(record_type.upper()))
    print('')


def mx_command_line(record):
    """
    Format the MX record info in command line
    :param record:
    :return:
    """
    record_type = 'MX RECORD'
    print('-' * (len(record_type) + 1))
    print(record_type.upper())
    print('-' * (len(record_type) + 1))
    try:
        if record is not None:
            for key, values in record.items():
                if len(values) == 2:
                    print(key.ljust(35, ' ') + values[0].ljust(20, ' ') +
                          'Preference: ' + values[1])
                elif len(values) == 1:
                    print(key.ljust(35, ' ') + values[0].ljust(20, ' '))
                elif len(values) == 0:
                    print(key)
        else:
            print('No {} record'.format(record_type))
            print('')
    except Exception as e:
        print('No {} record'.format(record_type))
    print('')


def ns_command_line(record):
    """
    Format the NS record info in command line
    :param record:
    :return:
    """
    record_type = 'NS RECORD'
    print('-' * (len(record_type) + 1))
    print(record_type.upper())
    print('-' * (len(record_type) + 1))
    try:
        if record is not None:
            for key, values in record.items():
                if len(values) == 2:
                    print(key.ljust(35, ' ') + values[0].ljust(20, ' ') +
                          'Preference: ' + values[1])
                elif len(values) == 1:
                    print(key.ljust(35, ' ') + values[0].ljust(20, ' '))
                elif len(values) == 0:
                    print(key)
        else:
            print('No {} record'.format(record_type))
            print('')
    except Exception as e:
        print('No {} record'.format(record_type))
    print('')


def soa_command_line(record):
    """

    :param record:
    :return:
    """
    record_type = 'SOA RECORD'
    print('-' * (len(record_type) + 1))
    print(record_type)
    print('-' * (len(record_type) + 1))
    if record is not None:
        for value in record:
            print(value)
    else:
        print('No {} record'.format(record_type.upper()))
    print('')


def txt_command_line(record):
    """

    :param record:
    :return:
    """
    record_type = 'TXT RECORD'
    print('-' * (len(record_type) + 1))
    print(record_type)
    print('-' * (len(record_type) + 1))
    if record is not None:
        for value in record:
            values = value.to_text().split()
            for v in values:
                print(v)
    else:
        print('No {} record'.format(record_type.upper()))
    print('')


def ptr_command_line(record):
    """

    :param record:
    :return:
    """
    record_type = 'PTR RECORD'
    print('-' * (len(record_type) + 1))
    print(record_type)
    print('-' * (len(record_type) + 1))
    if record is not None:
        print(record)
    else:
        print('No {} record'.format(record_type.upper()))
    print('')


def zt_command_line(record):
    """

    :param record:
    :return:
    """
    record_type = 'PTR RECORD'
    print('-' * (len(record_type) + 1))
    print(record_type)
    print('-' * (len(record_type) + 1))
    if record is not None:
        print(record)
    else:
        print('No {} record'.format(record_type.upper()))
    print('')


# def whois_command_line(data):
#     """
#     Prints the whois info in command line
#     :param data: A list of dicts. Each dict contain a key and a list of values
#     :return:
#     """
#     try:
#         query = 'WHOIS INFO'
#         print('-' * (len(query) + 1))
#         print(query)
#         print('-' * (len(query) + 1))
#         if data is not None:
#             for dictionary in data:
#                 try:
#                     del dictionary['raw']
#                 except Exception as e:
#                     pass
#                 for key, values in dictionary.items():
#                     for value in values:
#                         print('{} {}'.format(key.ljust(20, ' '), value))
#             print('')
#         else:
#             print('No Whois info')
#             print('')
#     except Exception as e:
#         print('No Whois info')
#         print('')


def whois_command_line(data):
    """
    Prints the whois info in command line
    :param data: A list of dicts. Each dict contain a key and a list of values
    :return:
    """
    try:
        query = 'WHOIS INFO'
        print('-' * (len(query) + 1))
        print(query)
        print('-' * (len(query) + 1))
        for key, value in data.items():
            print('{}: {}'.format(key, value))
        print('')
    except Exception as e:
        print('No Whois info')
        print('')