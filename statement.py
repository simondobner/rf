import json
from math import floor


def statement(invoice, plays):
    totalAmount = 0
    volumeCredits = 0
    invoice = json.loads(invoice)
    plays = json.loads(plays)
    result = f"Statement for {invoice[0]['customer']}\n"

    format = {'lang': "en-US",
              'style': "currency",
              'currency': "USD",
              'minimumFractionDigits': 2}

    # for (let perf of invoice.performances) {
    #     const play = plays[perf.playID];
    # let thisAmount = 0;

    for perf in invoice[0]['performances']:
        play = plays[perf['playID']]
        thisAmount = 0

        if play['type'] == 'tragedy':
            if play['type'] == "tragedy":
                thisAmount = 40000

            if perf['audience'] > 30:
                thisAmount += 1000 * (perf['audience'] - 30)

        elif play['type'] == 'comedy':
            thisAmount = 30000
            if perf['audience'] > 20:
                thisAmount += 10000 + 500 * (perf['audience'] - 20)
            thisAmount += 300 * perf['audience']
        else:
            raise Exception(f'unknown type: {play["type"]}')

        # add volume credits
        volumeCredits += max(perf['audience'] - 30, 0)
        # add extra credit for every ten comedy attendees

        if "comedy" == play['type']:
            volumeCredits += floor(perf['audience'] / 5)

        # print line for this order
        result += f"{play['name']}: {thisAmount/100} {perf['audience']} (seats)\n"
        totalAmount += thisAmount

    result += f'Amount owed is {totalAmount/100}\n'
    result += f'You earned {volumeCredits} credits\n'

    return result

        # Statement for BigCo
        #   Hamlet: $650.00 (55 seats)
        #   As You Like It: $580.00 (35 seats)
        #   Othello: $500.00 (40 seats)
        # Amount owed is $1,730.00
        # You earned 47 credits