#!/usr/bin/env python
# -*-coding: utf-8-*-


import logging
from simple_json_log_formatter import SimpleJsonFormatter
import json
import os


def get_logger():

    root_logger = logging.getLogger()
    if root_logger.handlers:
        return logging.getLogger()
    else:
        target_dir = os.path.join(os.path.dirname(__file__), 'log')
        log_file = os.path.join(target_dir, 'threat_feeds.log')
        root_logger.setLevel(logging.INFO)
        # format_str = '%(asctime)s - %(module_logger_name)s - %(levelname)s -
        # %(message)s'
        formatter = SimpleJsonFormatter(json.dumps)
        # formatter = logging.Formatter(format_str)
        handler = logging.FileHandler(log_file)
        handler.setLevel(logging.INFO)
        handler.setFormatter(formatter)
        root_logger.addHandler(handler)
        return logging.getLogger()
