from .models import Quote
import urllib.request,json


def get_quotes():
    #this functiongets json response from our url
    get_quotes_url='http://quotes.stormconsultancy.co.uk/random.json'
    with urllib.request.urlopen(get_quotes_url)as url:
        get_qoutes_data=url.read()
        get_qoutes_response = json.loads(get_qoutes_data)

        quotes_results=None

        if get_qoutes_response['quote']:
            quotes_results = process_results(get_qoutes_response)

        return quotes_results


def 