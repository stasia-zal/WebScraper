import requests
from bs4 import BeautifulSoup
import json
import os 
product_id = 124893467
next = True
headers = {
    "Cookie":'''sv3=1.0_33a489ce-3743-11f1-a9d6-327762139762; userCeneo=ID=c3c63f94-0c7b-4d73-a17e-8a5006a4a3d0; ai_user=MOmYH|2026-04-13T14:15:23.082Z; appType=%7B%22Value%22%3A1%7D; ga4_ga=GA1.2.33a489ce-3743-11f1-a9d6-327762139762; _gcl_au=1.1.1190663634.1776089745; FPID=FPID2.2.bnV3AeA%2FBZEQSxD2gUN3YSzk8bPJIr7Y1H1tiZAizCE%3D; consentcookie=eyJBZ3JlZUFsbCI6dHJ1ZSwiQ29uc2VudHMiOlsxLDMsNCwyXSwiVENTdHJpbmciOiJDUWltZlFBUWltZlFBR3lBQkJQTENhRXNBUF9nQUFBQUFCNVlJekpEN0JiRkxVRkF3RmhqWUtzUU1JRVRVTUNBQW9RQUFBYUJBQ0FCUUFLUUlBUUNra0FRQkFTZ0JBQUNBQUFBSUNSQklRQU1BQUFBQ0VBQVFBQUFJQUFFQUFDUUFRQUlBQUFBZ0FBUUFBQVlBQUFpQUlBQUFBQUlnQUlBQUFBQW1RaEFBQUlBRUVBQWhBQUVJQUFBQUFBQUFBQUFBZ0FBQUFBQ0FBSUFBQUFBQUNBQUFJQUFBQUFBQUFBQUFCQkdZQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFCWUtBREFBRUVaZ2tBR0FBSUl6Qm9BTUFBUVJtRVFBWUFBZ2pNS2dBd0FCQkdZWkFCZ0FDQ013NkFEQUFFRVppRUFHQUFJSXpFb0FNQUFRUm1LUUFZQUFnak1XZ0F3QUJCR1kuSUl6SkQ3QmJGTFVGQXdGaGpZS3NRTUlFVFVNQ0FBb1FBQUFhQkFDQUJRQUtRSUFRQ2trQVFCQVNnQkFBQ0FBQUFJQ1JCSVFBTUFBQUFDRUFBUUFBQUlBQUVBQUNRQVFBSUFBQUFnQUFRQUFBWUFBQWlBSUFBQUFBSWdBSUFBQUFBbVFoQUFBSUFFRUFBaEFBRUlBQUFBQUFBQUFBQUFnQUFBQUFDQUFJQUFBQUFBQ0FBQUlBQUFBQUFBQUFBQUJBIiwiVmVyc2lvbiI6InYzIn0=; _tt_enable_cookie=1; _ttp=01KP3NYW9TDM5A48X57ZATNTKQ_.tt.1; fs=et%3d639123040798021218%26sg%3d4d30e12a-4dc8-40ad-85f6-302c5cb97365%26st%3dipad+air%26encode%3dtrue; mbc=; urdsc=2; __RequestVerificationToken=bi9QExSsg9t29N4LjR2HrnopH9RV7VH-oaaWYmnNBs-Sn-FpzlYvE7rh__YiuQSY023M99bgqmMeyjPYwpsF7iAntI94trfjHaPV9z4kDcY1; st2=se%3dMKg-baSiu4YZ1bbrEUH6EK8MyUcF_Qmx%2cestid%3dgclidCj0KCQiA49XMBhDRARIsAOOKJHasKHYMCSIZngBA3HBAqgKteO9Y--xglYK6dFv3StHiMME52MfbWjUaAv6NEALw_wcB%2c_t%3d63912303480%2cencode%3dtrue; __utmf=17c17b2ad92f734b88848a1cfa1b7516_k2wCRI6tAVSgxOOwMsWh%2Bvo35Yf981ST; ga4_aw=GCL.1776699484.Cj0KCQiA49XMBhDRARIsAOOKJHasKHYMCSIZngBA3HBAqgKteO9Y--xglYK6dFv3StHiMME52MfbWjUaAv6NEALw_wcB; ga4_gs=2.2.k1$i1776699481$u53760314; FPLC=iQvygbBUerzyno9AnIvNsBS7D6OOP90Ip0SrA6nYBQ9lustzUiR8cJpq1Yzw9hz5vhv%2FjIfgc9l0mjt3OR84vUjbZnyIy2Jztm3P%2BEun1uqTesY%3D; cProdCompare_v2=; _gcl_aw=GCL.1776699485.Cj0KCQiA49XMBhDRARIsAOOKJHasKHYMCSIZngBA3HBAqgKteO9Y--xglYK6dFv3StHiMME52MfbWjUaAv6NEALw_wcB; _gcl_gs=2.1.k1$i1776699481$u53760314; browserBlStatus=1; rc=igdamb4ThOT/AObseYIgrEpeFsMflKvyuxDK5KCbsUg30Ssz4H6KZktEfTsEk8fkMj18bAYwPfqFLO7lx+XpGY+7ViIx1Ru6GR0zPcrS0VV02Lp/N9ZNcjI9fGwGMD36CGiym+7mCDf3VxXh2pW6+q+7tXCaIff6pOqzvg6LbK/O7vAe+gXwSNzjJ0WZwPioxeYCSPiF3RUVdUcrID+4DUpeFsMflKvyuxDK5KCbsUg30Ssz4H6KZjUBejSlRBNd+DiU/RkF4tBfQ/e1EyB6PQfBL5fT0zb6plzDlXSHtqcPAqQyTRSnkGrB+q4JLSHFFBd9MXb/4d+QD8Vuw6xzVkpeFsMflKvy0b8BhTe6kMdxLc+bAVp+E3CKlbKzeUNk; ttcsid_CNK74OBC77U1PP7E4UR0=1776699485704::xf9diMhBgrGXhnYkI3dr.2.1776699512329.1; ttcsid=1776699485705::fvrTZx3z4jRxrjvqtFqY.2.1776699512329.0::1.23700.26621::0.0.0.0::0.0.0; ga4_ga_K2N2M0CBQ6=GS2.2.s1776699484$o4$g1$t1776699512$j60$l0$h638139925; ai_session=cDTVQ|1776699484355|1776699793033'''
}
page= 1
all_opinions_list = []

while next:
    # page = 1
    url = f"https://www.ceneo.pl/{product_id}/opinie-{page}"
    print(url)
    response = requests.get(url=url,headers=headers)
    if response.status_code == 200:
        page_dom = BeautifulSoup(response.text,'html.parser')
        soup = page_dom.find('h1').get_text()
        all_opinions = page_dom.find_all('div',{'class':'js_product-review'})
        opinions = page_dom.select("div.js_product-review:not(.user-post--highlight)")
        for opinion in opinions:
            single_opinion = {
                "opinion_id":opinion["data-entry-id"],
                "author":opinion.select_one("span.user-post__author-name").get_text().strip(),
                'reccomendation':opinion.select_one('span.user-post__author-recommendation>em').get_text().strip() if opinion.
                    select_one('span.user-post__author-recommendation>em') else None,
                "score":opinion.select_one('.user-post__score-count').get_text().strip(),
                "content":opinion.select_one('div.user-post__text').get_text().strip(),
                "pros":[p.get_text().strip() for p in opinion.select('div.review-feature__item--positive')],
                "cons":[c.get_text().strip() for c in opinion.select('div.review-feature__item--negative')],
                "like":opinion.select_one('button.vote-yes > span').get_text().strip(),
                "dislike":opinion.select_one('button.vote-no > span').get_text().strip(),
                "publishing_date":opinion.select_one('span.user-post__published > time:nth-child(1)')["datetime"].strip() if opinion.select_one('span.user-post__published > time:nth-child(1)') else None,
                "purchase_date":opinion.select_one('span.user-post__published > time:nth-child(2)')['datetime'].strip() if opinion.select_one('span.user-post__published > time:nth-child(2)') else None,
            }
            all_opinions_list.append(single_opinion)            
        next = True if page_dom.select_one("button.pagination__next") else False
        print(f' next = {next}')
        if next: page+=1
if not os.path.exists("./opinions"):
    os.mkdir("./opinions")
with open(f"./opinions/{product_id}.json",'w',encoding="UTF-8") as file:
    json.dump(all_opinions_list,file,indent=4)