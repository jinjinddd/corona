import requests
import xmltodict
import json
from pprint import pprint


def get_corona_data(startCreateDt,endCreateDt):
    url="http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson"

    params={
        'serviceKey':'LRIesazP58TeZ6uApgF/9Dn+MXtxaSgclvTw/oExEG2oFvueI0g1xq2ulxlEZQhH7NRKwraZT++Dh11Hn+lpYA==',
        'pageNo':'1',
        'numOfRows':30,
        'startCreateDt':startCreateDt,#'20220118',
        'endCreateDt':endCreateDt,#'20220118',
    }

    res=requests.get(url, params=params)
    #print(res.url)
    dict_data=xmltodict.parse(res.text)
    print(dict_data)
    json_data=json.dumps(dict_data)
    #print(json_data, type(json_data))

    dict_data=json.loads(json_data)
    #print(dict_data,type(dict_data))
    #pprint(dict_data['response']['body']['items']['item'])

    #totalCount로 제대로 데이터가 가져와졌는지 확인하기
    totalCount= dict_data['response']['body']['totalCount']
    if totalCount=="0":
        return False

    area_data=dict_data['response']['body']['items']['item']
    area_data.reverse()
    #print(area_data)

    return area_data


