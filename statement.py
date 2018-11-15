import json


def statement(invoice, plays):
    totalAmount = 0
    volumeCredits = 0
    invoice = json.loads(invoice)
    result = "Statement for ".format(invoice['customer'])

    format = {'lang': "en-US",
              'style': "currency",
              'currency': "USD",
              'minimumFractionDigits': 2};

    for perf in invoice.performances:
        None
        play = plays[perf.playID]
        thisAmount = 0;

        if play['type'] == 'tragedy':
            None
        # switch (play.type) {
        # case "tragedy":
        # thisAmount = 40000;
        # if (perf.audience > 30) {
        #   thisAmount += 1000 * (perf.audience - 30);
        # }
        # break;
        elif play['type'] == 'comedy':
            None
        # thisAmount = 30000;
        # if (perf.audience > 20) {
        #   thisAmount += 10000 + 500 * (perf.audience - 20);
        # }
        # thisAmount += 300 * perf.audience;
        # break;
        else:
            raise Exception(f'unknown type: {play["type"]}')

    #
    #   // add volume credits
    #   volumeCredits += Math.max(perf.audience - 30, 0);
    #   // add extra credit for every ten comedy attendees
    #   if ("comedy" === play.type) volumeCredits += Math.floor(perf.audience / 5);
    #
    #   //print line for this order
    #   result += `  ${play.name}: ${format(thisAmount/100)} (${perf.audience} seats)\n`;
    #   totalAmount += thisAmount;
    # }
    # result += `Amount owed is ${format(totalAmount/100)}\n`;
    # result += `You earned ${volumeCredits} credits\n`;

    return result
