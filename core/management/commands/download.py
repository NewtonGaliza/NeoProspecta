from django.core.management.base import BaseCommand

import gzip
import requests

class Command(BaseCommand):
    help = 'Download file'

    def handle(self, *args, **kwargs):
        url = 'https://www.arb-silva.de/fileadmin/silva_databases/release_128/Exports/SILVA_128_LSURef_tax_silva.fasta.gz'

        r = requests.get(url)

   
        with open('arquivo.gz', 'wb') as f:
            f.write(r.content)

        with gzip.open('arquivo.gz', 'rb') as f:
            for line in f:
                linha  = line.decode('UTF-8') #cast bytes to string
        
