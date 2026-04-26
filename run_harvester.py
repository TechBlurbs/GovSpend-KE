import logging
import os
from dotenv import load_dotenv

# Initialize logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("Harvester")

def main():
    """
    Main entry point for the GovSpend-KE data harvester.
    This script coordinates the ingestion of data from various sources.
    """
    load_dotenv()
    
    logger.info("Starting GovSpend-KE Harvester...")
    
    # Placeholder for ingestion logic
    # from src.ingestion.treasury_scraper import TreasuryScraper
    # from src.ingestion.ocob_scraper import OCOBScraper
    
    logger.info("Harvester execution completed.")

if __name__ == "__main__":
    main()
