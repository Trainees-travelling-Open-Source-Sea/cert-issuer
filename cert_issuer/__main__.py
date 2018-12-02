#!/usr/bin/env python3

import os.path # 파일 경로를 생성 및 수정하고, 파일 정보를 쉽게 다룰 수 있게 해주는 모듈.
import sys # 파이썬 인터프리터가 제공하는 변수들과 함수들을 직접 제어할 수 있게 해주는 모듈

PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # 입력받은 파일/디렉터리의 경로를 반환

if __package__ is None and not hasattr(sys, 'frozen'): #sys에 'frozen' 이라는 변수가 있는지 확인.
    path = os.path.realpath(os.path.abspath(__file__)) #파일의 절대경로가 symbolic link인 경우 원본 위치를 찾아줌.
    sys.path.insert(0, os.path.dirname(os.path.dirname(path)))  # 파이썬 검색 경로에 새 디렉토리가 들어간다.


def cert_issuer_main(args=None):
    from cert_issuer import config
    /* conf.ini에서 설정 읽어 들이는 듯 함 */
    parsed_config = config.get_config()  #config 파일의 get_config 함수 호출
    from cert_issuer import issue_certificates
    /* issue_certificates.py의 main을 실행 */
    issue_certificates.main(parsed_config)  # issue_certificates 파일의 main 함수 호출


if __name__ == '__main__':
    cert_issuer_main()
