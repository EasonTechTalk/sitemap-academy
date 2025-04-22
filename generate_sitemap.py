import os
import sys
from sitemap_generator import SitemapGenerator

# Get website URL from GitHub repository variable
website_url = os.environ.get('WEBSITE_URL')
if not website_url:
    print("Error: WEBSITE_URL environment variable not set")
    sys.exit(1)

try:
    print(f"Generating sitemap for {website_url}")
    generator = SitemapGenerator(website_url)
    generator.crawl()
    generator.write('sitemap.xml')
    print("Sitemap generated successfully")
except Exception as e:
    print(f"Error generating sitemap: {e}")
    sys.exit(1)
