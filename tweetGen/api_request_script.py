import requests, parser, sys, json, time

def get_article(article_url):
    url = "https://api.diffbot.com/v3/article"
    querystring = {"token":"5b799344a22b17f9a9be09ad531e3b0b","url":"{}".format(article_url)}
    headers = {
        'cache-control': "no-cache",
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    res_obj = response.json()
    return res_obj['objects'][0]['text']

def start_process():
    urls_file = open("pages.txt").readlines()
    output_file = open('original_text.txt', 'w')

    corpus = ''

    for line in urls_file:
        article = get_article(line)
        corpus += article
        output_file.write(corpus)
    print('Corpus saved to {}'.format(output_file.name))
if __name__ == "__main__":
    start_process()