headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"
}

params = {
    "country_code": "FR",
    "country_codes[]": "pt",
    "currency_code": "EUR",
    "grape_filter": "varietal",
    "min_rating": "1",
    "order_by": "price",
    "order": "asc",
    "page": 1,
    "price_range_max": "50",
    "price_range_min": "0",
    "wine_type_ids[]": "1",
    "wine_style": "style"
}

api_url = "https://www.vivino.com/api/explore/explore"

r = requests.get(api_url, params=params, headers=headers)

results = []
for t in r.json()["explore_vintage"]["matches"]:
    winery = t["vintage"]["wine"]["winery"]["name"]
    year = t["vintage"]["year"]
    wine_id = t["vintage"]["wine"]["id"]
    wine = f'{t["vintage"]["wine"]["name"]} {t["vintage"]["year"]}'
    rating = t["vintage"]["statistics"]["ratings_average"]
    num_review = t["vintage"]["statistics"]["ratings_count"]
    price = t["prices"][0]["amount"] if "prices" in t else None
    wine_type = t["vintage"]["wine"]["type_id"]
    style = t["vintage"]["wine"]["style"]
    country = t["vintage"]["wine"]['region']["country"]["name"]
    results.append((winery, year, wine_id, wine, rating, num_review, price, wine_type, style, country))

for result in results:
    winery = result[0]
    year = result[1]
    wine_id = result[2]
    wine = result[3]
    rating_avg = result[4]
    num_reviews = result[5]
    price = result[6]
    wine_type = result[7]
    style = result[8]
    country = result[9]

    page = 1
    while True:
        results.append([wine_id, year, winery, wine, rating_avg, num_reviews, price, wine_type, style, country])
        page += 1

df_out = pd.DataFrame(
    results,
    columns=["Wine ID", "Year", "Winery", "Wine", "Rating_avg", "Num_reviews", "Price", "Type", "Style", "Country"]
)

df_out.to_csv("vivino.csv", index=False)