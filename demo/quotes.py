"""

"""

from sukhoi import Miner, core, Pool

class AuthorMiner(Miner):
    def run(self, dom):
        elem = dom.fst('div', ('class', 'author-description'))
        self.pool.append(elem.text().strip().rstrip())

class QuoteMiner(Miner):
    def run(self, dom):
        elems = dom.find('div', ('class', 'quote'))
        self.pool.extend(map(self.extract_quote, elems))

        elem = dom.fst('li', ('class', 'next'))
        if elem: self.next(elem.fst('a').attr['href'])

    def extract_quote(self, elem):
        quote = elem.fst('span', ('class', 'text'))
        author_url = elem.fst('a').attr['href']

        return {'quote': quote.text().strip().rstrip(), 
        'author':AuthorMiner(self.geturl(author_url))}

if __name__ == '__main__':
    URL = 'http://quotes.toscrape.com/tag/humor/'
    pool = []
    QuoteMiner(URL, pool)
    core.gear.mainloop()

    print repr(pool)

