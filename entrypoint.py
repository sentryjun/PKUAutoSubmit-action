#!/usr/bin/env python

import os
import sys
import argparse
import warnings
from selenium import webdriver

from func import run

warnings.filterwarnings('ignore')


def sys_path():
    path = os.path.join(os.getcwd(), 'phantomjs', 'bin')
    if sys.platform.startswith('win'):
        return os.path.join(path, 'phantomjs.exe')
    elif sys.platform.startswith('linux'):
        return os.path.join(path, 'phantomjs-linux')
    elif sys.platform.startswith('darwin'):
        return os.path.join(path, 'phantomjs')
    else:
        raise Exception('暂不支持该系统')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('username', type=str)
    parser.add_argument('password', type=str)
    parser.add_argument('campus', type=str)
    parser.add_argument('reason', type=str)
    parser.add_argument('in_habitation', type=str)
    parser.add_argument('in_district', type=str)
    parser.add_argument('in_street', type=str)
    parser.add_argument('out_destination', type=str)
    parser.add_argument('out_track', type=str)
    parser.add_argument('wechat', type=str)
    parser.add_argument('sckey', type=str)
    args = parser.parse_args()

    print('Driver Launching...')
    assert os.path.isfile(sys_path())
    driver_pjs = webdriver.PhantomJS(
        executable_path=sys_path(),
        service_args=['--ignore-ssl-errors=true'],
    )
    print('Driver Launched\n')

    run(driver_pjs, args.username, args.password, args.campus, args.reason,
        args.out_destination, args.out_track,
        args.in_habitation, args.in_district, args.in_street, False, '',
        eval(args.wechat), args.sckey)

    driver_pjs.quit()
