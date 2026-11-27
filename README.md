# TrustRadius Scraper API

Scrape TrustRadius with a JSON API. This repo has working Python examples for DataGuru's TrustRadius scraper APIs: TrustRadius Software Details and TrustRadius Software Search.

[DataGuru](https://dataguru.cc) runs the scraping, proxies, retries and parsing, and returns clean JSON. You pay only for successful requests, from $0.0012 per request, out of a prepaid balance: no subscription. New accounts get $1.00 of free credit.

## TrustRadius APIs

| API | What it returns | Price | Page |
| --- | --- | --- | --- |
| [TrustRadius Software Details](#trustradius-software-details) | Get a software product's TrustRadius profile and reviews from its URL, including score, rating and review counts, star distribution, vendor, categories, review insights with pros and cons, reviewer breakdowns, installations by industry and a page of reviews with reviewer details. | $0.0022 | [https://dataguru.cc/apis/trustradius-software-details/](https://dataguru.cc/apis/trustradius-software-details/) |
| [TrustRadius Software Search](#trustradius-software-search) | Search TrustRadius by keyword and get matching business software with star scores, rating and review counts, Top Rated categories, primary category and a short description. | $0.0012 | [https://dataguru.cc/apis/trustradius-software-search/](https://dataguru.cc/apis/trustradius-software-search/) |

## Quick start

1. Create a free account and an API key at [dashboard.dataguru.cc](https://dashboard.dataguru.cc).
2. Install and run:

```bash
git clone https://github.com/dataguru-cc/trustradius-scraper-api.git
cd trustradius-scraper-api
pip install -r requirements.txt
export DATAGURU_API_KEY="your key"
python examples/sdk_example.py trustradius-software-details
```

## Examples

Every example covers all 2 TrustRadius APIs. Pass an API name to run just one; with no name each script runs them all, and each call is billed at the price above.

| File | Style | Run |
| --- | --- | --- |
| [`examples/sdk_example.py`](examples/sdk_example.py) | [DataGuru Python SDK](https://github.com/dataguru-cc/dataguru-python) (`pip install dataguru-sdk`), one function per API, saves JSON to `output/` | `python examples/sdk_example.py` |
| [`examples/requests_example.py`](examples/requests_example.py) | Plain `requests`, synchronous | `python examples/requests_example.py` |
| [`examples/async_example.py`](examples/async_example.py) | `asyncio` + `httpx`, concurrent with a limit | `python examples/async_example.py` |
| [`examples/scrapy_spider.py`](examples/scrapy_spider.py) | Scrapy spider, items to JSON/CSV | `scrapy runspider examples/scrapy_spider.py -O trustradius.json` |

All requests use the header `Authorization: Api-Key YOUR_API_KEY`. Errors return `{"success": false, "error": {"code", "message", "request_id"}}`, with HTTP 402 when the balance runs out and 429 (with `Retry-After`) when rate limited. Failed requests are not charged.

## API reference

### TrustRadius Software Details

Get a software product's TrustRadius profile and reviews from its URL, including score, rating and review counts, star distribution, vendor, categories, review insights with pros and cons, reviewer breakdowns, installations by industry and a page of reviews with reviewer details.

- Endpoint: `POST https://api.dataguru.cc/api/v1/trustradius/software/details`
- Price: $0.0022 per successful request ($2.20 per 1,000)
- Rate limit: 60 requests/minute
- Page and live playground: https://dataguru.cc/apis/trustradius-software-details/
- Documentation: https://dataguru.cc/documentation/trustradius-software-details/

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `location` | string | no | Two-letter country code to fetch the page from (default US). |
| `page` | integer | no | Reviews page (10 reviews per page). Default: `1`. |
| `product_url` | string | yes | Full TrustRadius product URL (e.g. https://www.trustradius.com/products/hubspot-crm/reviews). |

**Response fields:** `product_id`, `name`, `slug`, `url`, `homepage`, `logo`, `vendor`, `categories`, `score`, `score_scale`, `ratings_count`, `review_count`, `star_distribution`, `review_insights`, `reviewer_company_sizes`, `reviewer_roles`, `reviewer_countries`, `installations`, `page`, `total_pages`, `reviews`, plus `_metadata`

```bash
curl -X POST "https://api.dataguru.cc/api/v1/trustradius/software/details" \
  -H "Authorization: Api-Key $DATAGURU_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"product_url": "https://www.trustradius.com/products/hubspot-crm/reviews"}'
```

<details><summary>Response schema</summary>

Values are type placeholders from the API's published schema, not real data.

```json
{
  "product_id": "1234567890",
  "name": "string",
  "slug": "string",
  "url": "https://example.com/...",
  "homepage": "string",
  "logo": "string",
  "vendor": {
    "id": "1234567890",
    "name": "string",
    "homepage": "string",
    "logo": "string"
  },
  "categories": [
    {
      "name": "string",
      "url": "https://example.com/..."
    }
  ],
  "score": 0.0,
  "score_scale": 0,
  "ratings_count": 0,
  "review_count": 0,
  "star_distribution": {},
  "review_insights": {
    "title": "string",
    "based_on": "string",
    "summary": "string",
    "pros": [
      "string"
    ],
    "cons": [
      "string"
    ]
  },
  "reviewer_company_sizes": [
    {
      "value": "string",
      "count": 0
    }
  ],
  "reviewer_roles": [
    {
      "value": "string",
      "count": 0
    }
  ],
  "reviewer_countries": [
    {
      "value": "string",
      "count": 0
    }
  ],
  "installations": {
    "total": 0,
    "updated": "string",
    "by_industry": [
      {
        "industry": "string",
        "naics_code": "string",
        "companies": 0,
        "share_percent": 0.0
      }
    ]
  },
  "page": 0,
  "total_pages": 0,
  "reviews": [
    {
      "id": "1234567890",
      "url": "https://example.com/...",
      "title": "string",
      "rating": 0.0,
      "date": "2026-01-01T12:00:00Z",
      "source": "string",
      "verification": "string",
      "use_cases": "string",
      "pros": [
        "string"
      ],
      "cons": [
        "string"
      ],
      "likelihood_to_recommend": "string",
      "other_answers": {},
      "reviewer": {
        "name": "string",
        "job_title": "string",
        "job_type": "string",
        "department": "string",
        "company": "string",
        "company_size": "string",
        "industry": "string",
        "headline": "string",
        "years_experience": 0,
        "profile_url": "https://example.com/..."
      }
    }
  ],
  "_metadata": {
    "request_id": "3f6c1a2e-8b4d-4c1e-9a7f-2d5e6b7c8d9e",
    "execution_time_ms": 842,
    "endpoint": "TrustRadius Software Details",
    "mode": "live",
    "format": "json",
    "timestamp": "2026-01-01T12:00:00+00:00"
  }
}
```

</details>

### TrustRadius Software Search

Search TrustRadius by keyword and get matching business software with star scores, rating and review counts, Top Rated categories, primary category and a short description.

- Endpoint: `POST https://api.dataguru.cc/api/v1/trustradius/software/search`
- Price: $0.0012 per successful request ($1.20 per 1,000)
- Rate limit: 60 requests/minute
- Page and live playground: https://dataguru.cc/apis/trustradius-software-search/
- Documentation: https://dataguru.cc/documentation/trustradius-software-search/

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `limit` | integer | no | Maximum number of products to return (1-25). Default: `25`. |
| `location` | string | no | Two-letter country code to search from (default US). |
| `page` | integer | no | Results page (25 products per page). Default: `1`. |
| `query` | string | yes | Software keywords or a product name, e.g. "crm" or "project management". |
| `sort` | string | no | Sort order - relevant, reviews (most reviewed), positive (highest rated), critical (lowest rated) or alpha (name). Default: `relevant`. Allowed: `relevant`, `reviews`, `positive`, `critical`, `alpha`. |

**Response fields:** `query`, `sort`, `page`, `search_url`, `total_results`, `result_count`, `results`, plus `_metadata`

```bash
curl -X POST "https://api.dataguru.cc/api/v1/trustradius/software/search" \
  -H "Authorization: Api-Key $DATAGURU_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "crm"}'
```

<details><summary>Response schema</summary>

Values are type placeholders from the API's published schema, not real data.

```json
{
  "query": "string",
  "sort": "relevant",
  "page": 0,
  "search_url": "https://example.com/...",
  "total_results": 0,
  "result_count": 0,
  "results": [
    {
      "position": 0,
      "name": "string",
      "slug": "string",
      "url": "https://example.com/...",
      "logo": "string",
      "star_rating": 0.0,
      "ratings_count": 0,
      "review_count": 0,
      "has_score": false,
      "customer_verified": false,
      "top_rated_in": [
        "string"
      ],
      "primary_category": {
        "name": "string",
        "url": "https://example.com/..."
      },
      "alternatives_url": "https://example.com/...",
      "description": "string"
    }
  ],
  "_metadata": {
    "request_id": "3f6c1a2e-8b4d-4c1e-9a7f-2d5e6b7c8d9e",
    "execution_time_ms": 842,
    "endpoint": "TrustRadius Software Search",
    "mode": "live",
    "format": "json",
    "timestamp": "2026-01-01T12:00:00+00:00"
  }
}
```

</details>

## More

- Python SDK and examples for all DataGuru APIs: [github.com/dataguru-cc/dataguru-python](https://github.com/dataguru-cc/dataguru-python) ([docs](https://dataguru-python.readthedocs.io/))
- Every API, with a live playground: [https://dataguru.cc/apis/](https://dataguru.cc/apis/)
- Use DataGuru from Claude, ChatGPT or Cursor through the MCP server: [https://dataguru.cc/mcp/](https://dataguru.cc/mcp/)
- Run thousands of inputs from a CSV at half price with batch jobs: [https://dataguru.cc/documentation/](https://dataguru.cc/documentation/)
- Other scraper APIs: [1688](https://github.com/dataguru-cc/1688-scraper-api), [Airbnb](https://github.com/dataguru-cc/airbnb-scraper-api), [Alibaba](https://github.com/dataguru-cc/alibaba-scraper-api), [AliExpress](https://github.com/dataguru-cc/aliexpress-scraper-api), [Amazon](https://github.com/dataguru-cc/amazon-scraper-api), [arXiv](https://github.com/dataguru-cc/arxiv-scraper-api), [ASOS](https://github.com/dataguru-cc/asos-scraper-api), [Best Buy](https://github.com/dataguru-cc/best-buy-scraper-api), [Booking.com](https://github.com/dataguru-cc/booking-scraper-api), [Brave Search](https://github.com/dataguru-cc/brave-search-scraper-api), [CA State Bar](https://github.com/dataguru-cc/california-state-bar-scraper-api), [Capterra](https://github.com/dataguru-cc/capterra-scraper-api), [CoinGecko](https://github.com/dataguru-cc/coingecko-scraper-api), [CoinMarketCap](https://github.com/dataguru-cc/coinmarketcap-scraper-api), [Companies House](https://github.com/dataguru-cc/companies-house-scraper-api), [Costco](https://github.com/dataguru-cc/costco-scraper-api), [CourtListener](https://github.com/dataguru-cc/courtlistener-scraper-api), [Crunchbase](https://github.com/dataguru-cc/crunchbase-scraper-api), [Discord](https://github.com/dataguru-cc/discord-scraper-api), [DoorDash](https://github.com/dataguru-cc/doordash-scraper-api), [eBay](https://github.com/dataguru-cc/ebay-scraper-api), [Etsy](https://github.com/dataguru-cc/etsy-scraper-api), [Expedia](https://github.com/dataguru-cc/expedia-scraper-api), [Fiverr](https://github.com/dataguru-cc/fiverr-scraper-api), [Flipkart](https://github.com/dataguru-cc/flipkart-scraper-api), [Glassdoor](https://github.com/dataguru-cc/glassdoor-scraper-api), [Google Flights](https://github.com/dataguru-cc/google-flights-scraper-api), [Google Patents](https://github.com/dataguru-cc/google-patents-scraper-api), [Google Scholar](https://github.com/dataguru-cc/google-scholar-scraper-api), [Google Search](https://github.com/dataguru-cc/google-search-scraper-api), [Grubhub](https://github.com/dataguru-cc/grubhub-scraper-api), [Home Depot](https://github.com/dataguru-cc/home-depot-scraper-api), [Instagram](https://github.com/dataguru-cc/instagram-scraper-api), [Investing.com](https://github.com/dataguru-cc/investing-com-scraper-api), [Justia](https://github.com/dataguru-cc/justia-scraper-api), [Kayak](https://github.com/dataguru-cc/kayak-scraper-api), [Kick](https://github.com/dataguru-cc/kick-scraper-api), [Lazada](https://github.com/dataguru-cc/lazada-scraper-api), [MarketWatch](https://github.com/dataguru-cc/marketwatch-scraper-api), [Mercado Libre](https://github.com/dataguru-cc/mercado-libre-scraper-api), [Monster](https://github.com/dataguru-cc/monster-scraper-api), [OpenCorporates](https://github.com/dataguru-cc/opencorporates-scraper-api), [OpenTable](https://github.com/dataguru-cc/opentable-scraper-api), [PACER](https://github.com/dataguru-cc/pacer-scraper-api), [PitchBook](https://github.com/dataguru-cc/pitchbook-scraper-api), [PubMed](https://github.com/dataguru-cc/pubmed-scraper-api), [Reddit](https://github.com/dataguru-cc/reddit-scraper-api), [Redfin](https://github.com/dataguru-cc/redfin-scraper-api), [Resy](https://github.com/dataguru-cc/resy-scraper-api), [Rightmove](https://github.com/dataguru-cc/rightmove-scraper-api), [SEC EDGAR](https://github.com/dataguru-cc/sec-edgar-scraper-api), [Seeking Alpha](https://github.com/dataguru-cc/seeking-alpha-scraper-api), [Shopee](https://github.com/dataguru-cc/shopee-scraper-api), [Skyscanner](https://github.com/dataguru-cc/skyscanner-scraper-api), [Target](https://github.com/dataguru-cc/target-scraper-api), [TikTok](https://github.com/dataguru-cc/tiktok-scraper-api), [TradingView](https://github.com/dataguru-cc/tradingview-scraper-api), [TripAdvisor](https://github.com/dataguru-cc/tripadvisor-scraper-api), [Trulia](https://github.com/dataguru-cc/trulia-scraper-api), [Twitch](https://github.com/dataguru-cc/twitch-scraper-api), [Uber Eats](https://github.com/dataguru-cc/uber-eats-scraper-api), [Upwork](https://github.com/dataguru-cc/upwork-scraper-api), [Vrbo](https://github.com/dataguru-cc/vrbo-scraper-api), [Walmart](https://github.com/dataguru-cc/walmart-scraper-api), [Wayfair](https://github.com/dataguru-cc/wayfair-scraper-api), [X (Twitter)](https://github.com/dataguru-cc/twitter-scraper-api), [Yahoo Finance](https://github.com/dataguru-cc/yahoo-finance-scraper-api), [YouTube](https://github.com/dataguru-cc/youtube-scraper-api), [Zillow](https://github.com/dataguru-cc/zillow-scraper-api), [ZoomInfo](https://github.com/dataguru-cc/zoominfo-scraper-api), [Zoopla](https://github.com/dataguru-cc/zoopla-scraper-api)

## License

The example code is MIT licensed. Use of the DataGuru API is subject to the [terms of service](https://dataguru.cc/terms/).
