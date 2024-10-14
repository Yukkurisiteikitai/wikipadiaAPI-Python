import requests
import random
import json



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

def getWikiSentence(title):
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
                return page_data['extract']
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
# タイトルを指定してWikipediaから説明文を取得
# title = "discord"  # 検索するタイトル
# get_wikipedia_summary(title)
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
    titles = []
    sentences =[]
    serchCount = 0
    while True:
        a = words_settings(3)
        if(cheackWikiFound(a) == True):
            print(a)
            # get_wikipedia_summary(a)
            titles.append(a)
            sentences.append(getWikiSentence(a))
            print("success")
            serchCount+=1
            if serchCount >= count:
                print("SerchEnd")
                break
t = []
s = []

def RandomWordsSerchReturnJson(count :int):
    global words
    
    titles = []
    sentences =[]
    serchCount = 0
    while True:
        a = words_settings(3)
        if(cheackWikiFound(a) == True):
            print(a)
            # get_wikipedia_summary(a)


            sentences_temp = getWikiSentence(a)
            if sentences_temp != "":
                titles.append(a)
                sentences.append(sentences_temp)
            else:
                continue

            # titles[len(titles)] = a
            # sentences[len(sentences)] = B

            print(sentences[len(sentences)-1])
            print()
            print("success")
            serchCount+=1
            if serchCount >= count:
                print("SerchEnd")
                print("sentences:")
                for i in range(len(titles)):
                    # print(titles[i])
                    print(sentences[i])
                # print(titles[i] for i in range(len(titles)))
                # print(sentences[i] for i in range(len(sentences)))
                return titles,sentences
                



# print(s)
t,s = RandomWordsSerchReturnJson(100)
# print(t)

print("\n\n[Load WikiAPI Scusess]\n\n")

import json
# JSONLファイルを作成
with open('output/outputv3.jsonl', 'w') as file:
    for t, k in zip(t, s):
        # 辞書として構造を定義
        data = {
            "title": t,
            "sencentes": k
        }
        # JSON形式でファイルに書き込み
        file.write(json.dumps(data) + '\n')

print("output.jsonlファイルが作成されました。")
# RandomWordsSerch(100)


# for i in range(len(words)):
#     get_wikipedia_summary(words[i])