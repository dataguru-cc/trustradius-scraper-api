"""TrustRadius scraper API: DataGuru Python SDK example.

Runs DataGuru's TrustRadius APIs and prints the JSON they return:
  - TrustRadius Software Details: $0.0022 per successful request ($2.20 per 1,000)
  - TrustRadius Software Search: $0.0012 per successful request ($1.20 per 1,000)

Setup:
    pip install -r requirements.txt
    export DATAGURU_API_KEY="your key"   # free credit at https://dashboard.dataguru.cc

Run:
    python examples/sdk_example.py            # every API below
    python examples/sdk_example.py trustradius-software-details
"""
import json
import sys
from pathlib import Path

from dataguru import DataGuru, DataGuruError

def trustradius_software_details(dg):
    """TrustRadius Software Details: Get a software product's TrustRadius profile and reviews from its URL, including score, rating and review counts, star distribution, vendor, categories, review insights with pros and cons, reviewer breakdowns, installations by industry and a page of reviews with reviewer details."""
    return dg.call(
        "trustradius-software-details",
        product_url="https://www.trustradius.com/products/hubspot-crm/reviews",
    )


def trustradius_software_search(dg):
    """TrustRadius Software Search: Search TrustRadius by keyword and get matching business software with star scores, rating and review counts, Top Rated categories, primary category and a short description."""
    return dg.call(
        "trustradius-software-search",
        query="crm",
    )


EXAMPLES = {
    "trustradius-software-details": trustradius_software_details,
    "trustradius-software-search": trustradius_software_search,
}
DEFAULT = ['trustradius-software-details', 'trustradius-software-search']


def main(names):
    out = Path("output")
    out.mkdir(exist_ok=True)
    with DataGuru() as dg:  # reads DATAGURU_API_KEY
        for name in names:
            data = EXAMPLES[name](dg)
            (out / f"{name}.json").write_text(json.dumps(data, indent=2, ensure_ascii=False))
            print(f"{name}: saved output/{name}.json")
            print(json.dumps(data, indent=2, ensure_ascii=False)[:1500])


if __name__ == "__main__":
    names = sys.argv[1:] or DEFAULT
    unknown = [n for n in names if n not in EXAMPLES]
    if unknown:
        sys.exit(f"Unknown API {unknown}. Choose from: {', '.join(EXAMPLES)}")
    try:
        main(names)
    except DataGuruError as error:
        sys.exit(f"DataGuru error: {error}")
