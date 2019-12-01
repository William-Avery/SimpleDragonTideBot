import requests, sys, time, bs4, re

class Session:
    def __init__(self, _user, _pass, _charid):
        self.s = requests.Session()
        self.username = _user
        self.password = _pass
        self.charID = _charid
        self.response = ""
        self.A_HP = 0
        self.M_HP = 0
        self.combat_turn = 4
        self.combat = False
        self.HealthPercent = 0

    def Login(self):
        # Login to Account
        print("-- Starting Session --")

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
        }

        logindata = {
            "dt_username": self.username,
            "password": self.password,
            "Login": "Login"
        }
        r = self.s.post(url='https://www.dragontide.com/logincheck2.aspx', data=logindata, headers=headers)
        self.s.get(url='https://www.dragontide.com/cookiecheck2.aspx')
        self.s.get(url='https://www.dragontide.com/myportal.aspx')
        if(r.status_code != 200):
            sys.exit('Server Error - No response back on Account Login')
        else:
            print("[Success] Account Login")

        # Login to Character
        chardata = {
            "char": self.charID
        }

        r = self.s.get(url='https://www.dragontide.com/logincheck3.aspx', params=chardata)
        if(r.status_code != 200):
            sys.exit('Server Error - No response back on Character Login')
        else:
            print("[Success] Character Login\n")
            r = self.s.get(url='https://www.dragontide.com/wild.aspx')
            self.response = r

    def Start(self):
        print("-- Starting Bot --")
        print("Checking Combat State...")

        # Pre-check for sessions already in combat
        self.Login_CombatCheck()

        # Start Process
        while True:

            # Determine State
            if self.combat:
                print("[State] In Combat")
                self.HealthCheck_IC()
                if(self.HealthPercent != 100):
                    self.RunAway()
                else:
                    while self.combat:
                        self.Attack()
            else:
                print("[State] Out Of Combat")
                # Check Health
                self.HealthCheck_OOC()
                    # If health is 100% Hunt, Else Rest
                if(self.HealthPercent == 100):
                    self.Hunt()
                else:
                    self.Rest()
        time.sleep(25)
    
    def Login_CombatCheck(self): 
        text = b'Enemy'
        if text in self.response.content:
            self.combat = True
        else:   
            self.combat = False

    def Combat_CombatCheck(self):
        print("[Combat] Combat Check")

    def Attack(self):
        print("[Combat] Attacking Monster")

    def Hunt(self):
        print("[Hunting] Start Hunting")
        params = {
            "dir": "H"
        }
        r = self.s.get(url='https://www.dragontide.com/wild.aspx', params=params)
        self.response = r
        print(r.content)
        
        while self.combat == True:
            self.Attack()
        time.sleep(10)

    def Rest(self):
        print("[Rest] Start Resting")
        params = {
            "dir": "R"
        }

        r = self.s.get(url='https://www.dragontide.com/wild.aspx', params=params)

    def HealthCheck_OOC(self): # Out Of Combat
        print("[Health] Performing Health Check")
        soup = bs4.BeautifulSoup(self.response.content, 'html.parser')
        htmlresult = soup.find('b').getText()
        values = re.findall(r'\d+', htmlresult)
        self.A_HP = values[0]
        self.M_HP = values[1]
        self.prcnt(values[0],values[1])
        print(f"{self.A_HP}/{self.M_HP} {self.HealthPercent}%")

    def prcnt(self, x, y):
        x = int(x)
        y = int(y)
        if not x and not y:
            print('x = 0%\ny = 0%')
        elif x < 0 or y < 0:
            print("can't be negative!")
        else:
            total = int(((x/y) * 100))
            self.HealthPercent = total

    def HealthCheck_IC(self): # In Combat
        print("[Health] Performing Health Check")

    def RunAway(self):
        params = {
            "type": f"run-{self.combat_turn}"
        }
        print(params["type"])

        r = self.s.get(url="https://www.dragontide.com/combat.aspx")