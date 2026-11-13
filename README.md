# NT Schools Directory Scraper — Scrapy

Scrapy spider that collects contact details for every school in the [Northern Territory (Australia) schools directory](https://directory.ntschools.net/#/schools) and exports them to CSV.

## The challenge

The directory is a JavaScript application: the school list is loaded in the browser, so the HTML that a normal scraper downloads has no school data in it.

Instead of rendering the page with a headless browser, the spider calls the same JSON API the website uses:

1. `GET /api/System/GetAllSchools` returns the list of all schools and their codes
2. For each school, `GET /api/System/GetSchool?itSchoolCode=<code>` returns its details
3. The spider extracts the fields below and writes one row per school

This is faster and lighter than browser automation, and the data comes back already structured.

## Output

[`ntschools/NetSchool.csv`](ntschools/NetSchool.csv): 208 schools.

| Field | Description |
|:--|:--|
| Name | School name |
| PhysicalAddress | Street address |
| PostalAddress | Postal address |
| Phone | Telephone number |
| Email | Contact email |

## Usage

```bash
pip install scrapy
cd ntschools
scrapy crawl SchoolsCrawl -O schools.csv
```

## Tech stack

Python · Scrapy · JSON API requests · CSV export

## Responsible use

`ROBOTSTXT_OBEY` is enabled. The data comes from a public directory; respect the site's terms of use and do not overload it.

## License

Apache 2.0
