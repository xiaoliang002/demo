# -*- coding: utf-8 -*-
# @Time    : 2020/9/21 9:42 上午
# @Author  : Xiao Liang -cn
# @Software: PyCharm
#elk工具查询示例

import json
import fire
from elasticsearch import Elasticsearch

es = Elasticsearch(['xxx.xx.xx.xx'], http_auth=('xxx', 'xxx'), timeout=3600)

'''must = and，should = or，must_not = not '''

dsl = {
    "query": {
        "bool": {
            "must": [],
            "filter": [{"bool": {"filter": [
            ]
            }}, ],
            "should": [],
            "must_not": []
        }},
    "sort": [
        {"logTime": {"order": "desc", "unmapped_type": "boolean"}}
    ]
}

#下面是命令行参数的一个字段转义,使用的是and关系,同时三个字段条件满足即可显示数据
def SaasLogs(Code, Type, ID):
    Code = {"bool": {"should": [{"match_phrase": {"interfaceType": Code}}], "minimum_should_match": 1}},
    type = {
        "业务流水号": "orderNo",
        "订单编号": "orderSerialNo",
        "退保单号": "policyRefundSerialNo",
        "保单号": "policyNo"
    }

    conditions = {"bool": {"should": [{"match_phrase": {type.get(Type): ID}}], "minimum_should_match": 1}}
    dsl.get('query').get('bool').get('filter')[0].get('bool').get('filter').append(conditions)
    dsl.get('query').get('bool').get('filter').append(Code)

    data = es.search(index='rest-template-log', body=dsl, from_='0', size=1)
    print(json.dumps(data['hits']['hits'], indent=2, ensure_ascii=False))

    # print(dsl)


if __name__ == '__main__':
    try:
        fire.Fire(SaasLogs)
    except Exception as e:
        print("暂时无法查询到相关数据")
        
  
#python file xxxx 订单编号 xxxxx
