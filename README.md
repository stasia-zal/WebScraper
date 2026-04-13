# WebScraper
## Project implementasion steps
### Stages 1-3
1. provide URL address of product's opinions webpage
2. Send the request to provided URL address
3. If status code is ok, fetch all opinions from requested webpage
4. For all fetched opinions, parse them to extract relevant data
5. Check if there is next page with opinions
6. For all remaining pages repeat steps 2-5
7. Save obtained opinions

## Project inputs
### Product codes
- 225645   *18+
- 8679864   *18+
- 189795038
### Opinion 
|component|name|selector|
|----|-|-|
|opinions Id opinios author |opinion_id|[data-entry-id]|
|authors name|author|.user-post__author-name|
|authors recommendation|recommendation|.user-postscore > .user-postauthor-recomendation > em|
|score expressed in number of stars|score|.user-postscore-count|
|opinions content|content|.user-post__text|
|list of product advantages|pros|.review-feature__item--positive|
| list of product disadvantages|cons|.review-feature__item--negative|
| how many users think that opinion was helpful|like|button.vote-yes > span|
| how many users think that opinion was unhelpful|dislike|utton.vote-no > span|
| publishing date|publish_date|.user-post__published > time:nth-child(1)[datetime]|
| purchase date|purchase_date|.user-post__published > time:nth-child(2)[datetime]|