from modules import *
import time

"""
First of all set your urls, header, mail settings in modules.
Trendyol(urltrendyol, headers, sendermail, password, gettermail, sendermail)
Hepsiburada(urlhepsiburada, headers, sendermail, password, gettermail, sendermail)
in modules set your price exp line : 37 and 79
"""

if __name__ == '__main__':
    while(True):
        q = TrendYol(urltrendyol, headers, sendermail, password, gettermail)
        q.kontrol()
        time.sleep(60*60)
