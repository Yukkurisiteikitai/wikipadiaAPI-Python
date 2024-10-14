import requests
import random


#wikipediaの記事のタイトルから検索をかけて存在したら説明を表示するAPI
def get_wikipedia_summary(title):
    # Wikipedia APIのURL
    url = "https://en.wikipedia.org/w/api.php"
    
    # APIパラメータ
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "exintro": True,
        "explaintext": True,
        "titles": title
    }
    
    # リクエストを送信
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
        # ページIDを取得
        pages = data.get("query", {}).get("pages", {})
        
        # ページの説明文を表示
        for page_id, page_data in pages.items():
            if "extract" in page_data:
                print(f"説明文: {page_data['extract']}\n\n")
            else:
                print("説明文が見つかりませんでした。")
    else:
        print("エラーが発生しました。")


def cheackWikiFound(title):
    url = "https://en.wikipedia.org/w/api.php"
    params = {"action": "query","format": "json","prop": "extracts","exintro": True,"explaintext": True,"titles": title}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()    
        pages = data.get("query", {}).get("pages", {})
        for page_id, page_data in pages.items():
            if "extract" in page_data:
                return True
            else:
                return False
    else:
        print("エラーが発生しました。")
        return False

words = ["a","q","z","w","s","x","e","d","c","r","f","v","t","g","b","y","h","n","u","j","m","i","k",",","o","l","p","Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]

def j(n,l):
    t = ""
    for i in range(n):
        t += l[random.randint(0,len(l)-1)]
    return t

def words_settings(n):
    t = ""
    for i in range(n):
        t += words[random.randint(0,len(words)-1)]
    return t


def RandomWordsSerch(count :int):
    global words
    serchCount = 0
    while True:
        a = words_settings(3)
        if(cheackWikiFound(a) == True):
            print(a)
            get_wikipedia_summary(a)
            print("success")
            serchCount+=1
            if serchCount >= count:
                print("SerchEnd")
                break

#ランダムに単語を取得してその説明文を表示する関数.
RandomWordsSerch(100)

# タイトルを指定してWikipediaから説明文を取得して表示する.
title = "discord"  # 検索するタイトル.
get_wikipedia_summary(title)
