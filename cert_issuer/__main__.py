#!/usr/bin/env python3

import os.path
import sys

PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if __package__ is None and not hasattr(sys, 'frozen'):
    path = os.path.realpath(os.path.abspath(__file__))
    sys.path.insert(0, os.path.dirname(os.path.dirname(path)))


def cert_issuer_main(args=None):
    from cert_issuer import config
    /* conf.ini에서 설정 읽어 들이는 듯 함 */
    parsed_config = config.get_config()
    from cert_issuer import issue_certificates
    /* issue_certificates.py의 main을 실행 */
    issue_certificates.main(parsed_config)


if __name__ == '__main__':
    cert_issuer_main()
