# -*- coding: utf-8 -*-
import argparse
import datetime
import json
import logging
from typing import Iterator, List, Tuple

from requests_html import HTMLSession

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger(__name__)


def helper_title(title: str) -> Tuple[Tuple[int, int, int], str]:
    _, location = title.split('地区', 1)[0].split('日', 1)
    year, _ = _.split('年')
    month, day = _.split('月')
    return ((day, month, year), location)


class Crawler:
    def __init__(self):
        self.base_url = 'http://www.62422.cn'
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

        (day, month, year), location = helper_title(resp.html.find('title', first=True).text)
        LOG.info(f'[+] {day}/{month}/{year}: {location}')

        data = resp.html.text.split('点此查看会员收费标准与办理方式\n', 1)[1].split('\n')
        lst = (it
               for it in data
               if it.startswith(location))
        return lst


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('uri', help="uri")
    args = parser.parse_args()
    return args


def main(url: str = ''):
    crawler = Crawler()
    lst = crawler.parse()
    seen = {}
    date, _ = helper_title(lst[0].text)
    for it in lst:
        _, loc = helper_title(it.text)
        seen[loc] = list(crawler.parse_details(it.attrs['href']))
    result_filename = '_data/result_{}.json'.format(datetime.datetime.today().date())
    with open(result_filename, 'w') as fd:
        json.dump(seen, fd, ensure_ascii=False)
    LOG.info(f'[+] write to {result_filename}')


if __name__ == '__main__':
    # args = parse_args()
    # main(args.uri)
    main()
