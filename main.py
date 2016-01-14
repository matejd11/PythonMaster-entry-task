#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import argparse
import sys

def main(amount, input_currency, output_currency):
    data = {'CZK': [27.0226, u'', 1],
            'EUR': [1, u'€', 1],
            'USD': [1.0885, u'$', 1],
            'AUD': [1.5695, u'', 1],
            'BGN': [1.9558, u'', 1],
            'BRL': [4.373, u'', 1],
            'CAD': [1.5647, u'', 1],
            'CHF': [1.095, u'', 1],
            'CNY': [7.1809, u'¥', 1],
            'CZK': [27.021, u'', 1],
            'DKK': [7.4624, u'', 1],
            'GBP': [0.75703, u'£', 1],
            'HKD': [8.4775, u'', 1],
            'HRK': [7.666, u'', 1],
            'HUF': [315.97, u'', 1],
            'IDR': [15155.06, u'', 1],
            'ILS': [4.2986, u'₪', 1],
            'INR': [73.4516, u'', 1],
            'JPY': [128.26, u'', 1],
            'KRW': [1320.77, u'₩', 1],
            'MXN': [19.5529, u'', 1],
            'MYR': [4.7855, u'', 1],
            'NOK': [9.6071, u'', 1],
            'NZD': [1.6903, u'', 1],
            'PHP': [52.076, u'₱', 1],
            'PLN': [4.373, u'', 1],
            'RON': [4.5348, u'', 1],
            'RUB': [83.2007, u'', 1],
            'SEK': [9.285, u'', 1],
            'SGD': [1.567, u'', 1],
            'THB': [39.552, u'฿', 1],
            'TRY': [3.3025, u'', 1],
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
