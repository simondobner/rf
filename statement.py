import json
from math import floor


def statement(invoice, plays):
    totalAmount = 0
    volumeCredits = 0
    invoice = json.loads(invoice)
    result = f"Statement for {invoice[0]['customer']}"

    format = {'lang': "en-US",
              'style': "currency",
              'currency': "USD",
              'minimumFractionDigits': 2}

    for perf in invoice[0]['performances']:
        print(f"--->{perf}")
        play = plays[perf.playID]
        thisAmount = 0

        if play['type'] == 'tragedy':
            if play['type'] == "tragedy":
                thisAmount = 40000
            if perf['audience'] > 30:
                thisAmount += 1000 * (perf.audience - 30)

        elif play['type'] == 'comedy':
            thisAmount = 30000
            if perf['audience'] > 20:
                thisAmount += 10000 + 500 * (perf.audience - 20)
            thisAmount += 300 * perf.audience
        else:
            raise Exception(f'unknown type: {play["type"]}')

        # add volume credits
        volumeCredits += max(perf.audience - 30, 0)
        # add extra credit for every ten comedy attendees
        if "comedy" == play['type']:
            volumeCredits += floor(perf['audience'] / 5)

        # print line for this order
        result += f'{play.name}: {thisAmount/100} {perf.audience} seats)\n'
        totalAmount += thisAmount

    result += f'Amount owed is {totalAmount/100}\n'
    result += f'You earned {volumeCredits} credits\n'

    return result
