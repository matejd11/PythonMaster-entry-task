#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import argparse
import sys

def main(amount, input_currency, output_currency):
    data = {'CZK': [27.0226, u'', 1],
            'EUR': [1, u'€', 1],
            'USD': [1.0885, u'$', 1],
            'CNY': [7.1809, u'¥', 1],
            'GBP': [0.75703, u'£', 1],
            'ILS': [4.2986, u'₪', 1],
            'KRW': [1320.77, u'₩', 1],
            'PHP': [52.076, u'₱', 1],
            'THB': [39.552, u'฿', 1],
            'ZAR': [18.0475, u'R', 1]}

    if len(input_currency) == 1:
        for cur in data:
            if data[cur][1] == output_currency:
                amount_in_EUR = float(amount) / data[cur][0] * data[cur][2]
    else:
        amount_in_EUR = float(amount) / data[input_currency][0] * data[input_currency][2]
    outputData = {}
    if not output_currency is False:
        if len(output_currency) == 1:
            for cur in data:
                if data[cur][1] == output_currency:
                    outputData[cur] = float(amount_in_EUR) / data[cur][2] * data[cur][0]
        else:
            outputData = {output_currency: float(amount_in_EUR) / data[output_currency][2] * data[output_currency][0]
}
    else:
        for cur in data:
            outputData[cur] = float(amount_in_EUR) / data[cur][2] * data[cur][0]

    for key in outputData:
        outputData[key] = round(outputData[key], 2)

    inputData = {'amount': amount, 'currency': input_currency}
    res = {'input': inputData, 'output': outputData}
    print(json.dumps(res, sort_keys=True, indent=4))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Currency converter - PythonMaster entry test - Matej Dujava')
    parser.add_argument('--amount', action='store', help='amount which we want to convert - float')
    parser.add_argument('--input_currency', action='store', help='input currency - 3 letters name or currency symbol')
    parser.add_argument('--output_currency', action='store', help='requested/output currency - 3 letters name or currency symbol')

    result = parser.parse_args()

    if result.amount is None:
        sys.exit("amount is required, try -h")
    if result.input_currency is None:
        sys.exit("input_currency is required, try -h")
    if result.output_currency is None:
        result.output_currency = False

    main(result.amount, result.input_currency, result.output_currency)
