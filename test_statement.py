from statement import statement


class TestStatement():
    def test_statement(self):
        invoice = """
        [
          {
            "customer": "BigCo",
            "performances": [
              {
                "playID": "hamlet",
                "audience": 55
              },
              {
                "playID": "as-like",
                "audience": 35
              },
              {
                "playID": "othello",
                "audience": 40
              }
            ]
          }
        ]
        """

        # plays is a dict, like this:
        plays = """{
            "hamlet": {"name": "Hamlet", "type": "tragedy"},
            "as-like": {"name": "As You Like It", "type": "comedy"},
            "othello": {"name": "Othello", "type": "tragedy"}
        } """

        result = statement(invoice, plays)

        assert result == ("Statement for BigCo\n"
                          "Hamlet: 650.0 55 (seats)\n"
                          "As You Like It: 580.0 35 (seats)\n"
                          "Othello: 500.0 40 (seats)\n"
                          "  Amount owed is 1730.0\n"
                          "  You earned 47 credits\n")
