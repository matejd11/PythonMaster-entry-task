#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import argparse
import sys

def main(amount, input_currency, output_currency):
    data = {}
    outputData = {}
    if not output_currency is False:
        outputData = {output_currency: 1}
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
