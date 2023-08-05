class CDSL:
    def __init__(self):
        self.security_ch = 50
        print("CDSL con Called")

    def charges(self):
        print("This is CDSL charges Method",self.security_ch)


class NSDL:
    def __init__(self):
        self.security_ch11 = 100
        print("NSDL con Called")

    def charges11(self):
        print("This is NSDL charges11 Method",self.security_ch11)


class ZERODHA(NSDL, CDSL):
    def __init__(self):
        CDSL.__init__(self)
        NSDL.__init__(self)
        NSDL.charges11(self)
        print("ZERODHA Constructor Called")

    def user_charges(self):
        print("User Charges")


uday = ZERODHA()

uday.user_charges()
uday.charges11()
uday.charges()