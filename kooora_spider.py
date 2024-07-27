import scrapy

class KoooraSpider(scrapy.Spider):
    name = 'kooora'
    
    # Set the initial URL
    def start_requests(self):
        base_url = "https://footballdatabase.com/league-scores/saudi-arabia-pro-league-2023-2024/"
        for i in range(1, 6):  # Adjust the range if more pages are needed
            url = f"{base_url}{i}"
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        date = response.xpath('//h4/text()').get()
        if date:
            date = date.strip()  # Strip any leading/trailing whitespace

        matches = response.xpath('//div[@class="club-gamelist-match"]')
        
        for match in matches:
            team1 = match.xpath('.//div[@class="club-gamelist-match-clubs"][1]/a/text()').get()
            score = match.xpath('.//div[@class="club-gamelist-match-score text-center"]/text()').get()
            print (score)
            team2 = match.xpath('.//div[@class="club-gamelist-match-clubs"][2]/a/text()').get()
            
            # Handle possible None values
            team1 = team1.strip() if team1 else 'Unknown'
            score = score.strip() if score else 'Unknown'
            team2 = team2.strip() if team2 else 'Unknown'
            
            yield {
                'Date': date if date else 'Unknown',
                'Team 1': team1,
                'Score': score,
                'Team 2': team2
            }

