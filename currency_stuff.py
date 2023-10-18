import urllib.request
import xml.dom.minidom
from date_stuff import get_date


# TDD
def request(days_delta=0):
    response = urllib.request.urlopen(f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={get_date(days_delta)}")
    if response.code == 200:
        return response
    raise Exception("Bad Response")
    


# BDD
def get_valutes(days_delta=0, with_rub=False):
    exit_dict = dict()
    response = request(days_delta)
    dom = xml.dom.minidom.parse(response)
    dom.normalize()
    nodeArray = dom.getElementsByTagName("Valute")
    for node in nodeArray:
        childList = node.childNodes
        for child in childList:
            if child.nodeName not in exit_dict:
                exit_dict[child.nodeName] = []
            exit_dict[child.nodeName].append(child.childNodes[0].nodeValue)
    if with_rub:
        exit_dict["NumCode"].insert(0, "001")
        exit_dict["CharCode"].insert(0, "RUB")
        exit_dict["Nominal"].insert(0, "1")
        exit_dict["Name"].insert(0, "Российский рубль")
        exit_dict["Value"].insert(0, "1")
    return exit_dict
