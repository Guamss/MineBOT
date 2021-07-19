import requests
from bs4 import BeautifulSoup

class Opggtrack:
    def __init__(self, username, region):
        url = f"https://{region}.op.gg/summoner/userName={username}"
        response = requests.get(url)
        if response.ok:
            soup = BeautifulSoup(response.text, "lxml")
            self.unknownuser = soup.find("h2", {"class" : "Title"})
            if self.unknownuser != None:
                print("Cet utilisateur n'existe pas")
            else:
                summonerid = int(soup.find("div", {"class" : "GameListContainer"})["data-summoner-id"])
                updatedata = {"summonerId": summonerid}
                with requests.Session() as s:
                    s.post(url, data=updatedata)
                
                soup = BeautifulSoup(response.text, "lxml")
                self.last_ten_W = soup.find("span", {"class" : "win"})
                self.last_ten_D = soup.find("span", {"class" : "lose"})
                self.kdaratio = soup.find("span", {"class" : "KDARatio"})
                self.ranksolo = soup.find("div", {"class" : "TierRank"})
                if self.ranksolo == None:
                    self.ranksolo ="Unranked"
                else:
                    self.ranksolo = self.ranksolo.text.replace("\n", "").replace("\t", "").replace("  ", "")
                self.rankflex = soup.find("div", {"class" : "sub-tier__rank-tier "})
                if self.rankflex == None:
                    self.rankflex = "Unranked"
                else:
                    self.rankflex = self.rankflex.text.replace("\n", "").replace("\t", "").replace("  ", "")

    def get_kdaratio(self):
        return self.kdaratio.text
    
    def get_unknownuser(self):
        return self.unknownuser

    def get_ranksolo(self):
        return self.ranksolo

    def get_rankflex(self):
        return self.rankflex
    
    def get_last_ten_W(self):
        return self.last_ten_W.text
                    
    def get_last_ten_D(self):
        return self.last_ten_D.text
                