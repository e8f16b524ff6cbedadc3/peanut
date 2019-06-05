# -*- coding: utf-8 -*-
import argparse
import logging
from typing import List, Iterator

from requests_html import HTMLSession

logging.basicConfig(level=logging.INFO)


class Crawler:
    def __init__(self):
        self.base_url = 'http://www.62422.cn'
        self.logger = logging.getLogger(__name__)
        self.session = HTMLSession()

    def parse(self) -> List[str]:
        url = f'{self.base_url}/search.asp?cataid=77'
        resp = self.session.get(url)
        lst = resp.html.find('a[href^=look]')
        return lst

    def parse_details(self, url: str) -> Iterator[str]:
        url = f'{self.base_url}/{url}'
        resp = self.session.get(url)
        resp.html.encoding = 'gbk'

        _, location = resp.html.find('title', first=True).text.split('地区', 1)[0].split('日', 1)
        year, _ = _.split('年')
        month, day = _.split('月')
        self.logger.info(f'[+] {day}/{month}/{year}: {location}')

        data = resp.html.text.split('点此查看会员收费标准与办理方式\n', 1)[1].split('\n')
        lst = (it
               for it in data
               if it.startswith(location))
        for it in lst:
            self.logger.info(f'[+] entry: {it}')
        return lst


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('uri', help="uri")
    args = parser.parse_args()
    return args


def main(url: str = ''):
    crawler = Crawler()
    lst = crawler.parse()
    crawler.parse_details(lst[0].attrs['href'])


if __name__ == '__main__':
    # args = parse_args()
    # main(args.uri)
    main()
