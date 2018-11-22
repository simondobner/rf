import json
from math import floor


def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
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
        this_amount = 0

        if play['type'] == 'tragedy':
            if play['type'] == "tragedy":
                this_amount = 40000

            if perf['audience'] > 30:
                this_amount += 1000 * (perf['audience'] - 30)

        elif play['type'] == 'comedy':
            this_amount = 30000
            if perf['audience'] > 20:
                this_amount += 10000 + 500 * (perf['audience'] - 20)
            this_amount += 300 * perf['audience']
        else:
            raise Exception(f'unknown type: {play["type"]}')

        # add volume credits
        volume_credits += max(perf['audience'] - 30, 0)
        # add extra credit for every ten comedy attendees

        if "comedy" == play['type']:
            volume_credits += floor(perf['audience'] / 5)

        # print line for this order
        result += f"{play['name']}: {this_amount/100} {perf['audience']} (seats)\n"
        total_amount += this_amount

    result += f'Amount owed is {total_amount/100}\n'
    result += f'You earned {volume_credits} credits\n'

    return result

    # Statement for BigCo
    #   Hamlet: $650.00 (55 seats)
    #   As You Like It: $580.00 (35 seats)
    #   Othello: $500.00 (40 seats)
    # Amount owed is $1,730.00
    # You earned 47 credits
