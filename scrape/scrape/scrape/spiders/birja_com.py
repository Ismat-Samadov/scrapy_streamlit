import scrapy

class CombinedSpider(scrapy.Spider):
    name = "birja_com"
    allowed_domains = ["birja.com"]
    start_urls = ["https://birja.com/category/az/1/2/0/satilir/1",
                  'birja.com/content/az/3',
                  'birja.com/content/az/2',
                  'birja.com/login',
                  'birja.com/lang/ru',
                  'birja.com/category/az/1/2/0/satilir',
                  'birja.com/category/az/1/14/0/icare',
                  'birja.com/category/az/1/26/0/mubadile',
                  'birja.com/category/az/1/29/0/aliram',
                  'birja.com/category/az/1/30/0/xarici-dashinmaz-emlak',
                  'birja.com/category/az/1/31/0/kiraye-gotururem',
                  'birja.com/category/az/32/33/0/avtomobil',
                  'birja.com/category/az/32/36/0/qoshqular',
                  'birja.com/category/az/32/37/0/avtomobil-hisseleri-aksessuarlar',
                  'birja.com/category/az/32/38/0/avtoservis-avadanliqlari',
                  'birja.com/category/az/32/39/0/mototexnika',
                  'birja.com/category/az/32/40/0/kend-teserrufati-texnikasi',
                  'birja.com/category/az/32/41/0/diger',
                  'birja.com/category/az/32/42/0/yuk-mashinlari',
                  'birja.com/category/az/43/44/0/musiqi-aletleri',
                  'birja.com/category/az/43/45/0/idman-turizm',
                  'birja.com/category/az/43/46/0/mashinlari-avadanliqlari',
                  'birja.com/category/az/43/47/0/tikinti-materiallari',
                  'birja.com/category/az/43/48/0/agac-ve-bitkiler',
                  'birja.com/category/az/43/49/0/cevahirat',
                  'birja.com/category/az/43/50/0/telefon-nomreleri',
                  'birja.com/category/az/43/51/0/oyun-konsollari',
                  'birja.com/category/az/43/52/0/ushaqlar-uchun',
                  'birja.com/category/az/43/53/0/biletler',
                  'birja.com/category/az/43/54/0/diger',
                  'birja.com/category/az/43/55/0/erzaq',
                  'birja.com/category/az/43/56/0/meishet-avadanliqlari',
                  'birja.com/category/az/43/57/0/derman',
                  'birja.com/category/az/43/58/0/mobil-telefonlar',
                  'birja.com/category/az/43/59/0/avadanliq-ve-meishet-cihazlari',
                  'birja.com/category/az/43/60/0/heyvanlar',
                  'birja.com/category/az/43/61/0/kitablar-ve-jurnallar',
                  'birja.com/category/az/43/62/0/kosmetika',
                  'birja.com/category/az/43/63/0/mebel',
                  'birja.com/category/az/43/64/0/tibbi-avadanliqlar',
                  'birja.com/category/az/43/65/0/geyim-ayaqqabi-ve-tekstil',
                  'birja.com/category/az/43/66/0/saatlar-ve-zergerlik',
                  'birja.com/category/az/43/67/0/entiq-eshyalari',
                  'birja.com/category/az/43/68/0/ofis-avadanligi',
                  'birja.com/category/az/43/70/0/1001-xirdavat',
                  'birja.com/category/az/71/72/0/ish-axtariram',
                  'birja.com/category/az/71/97/0/ish-teklif-edirem',
                  'birja.com/category/az/121/122/0/immiqrasiya',
                  'birja.com/category/az/121/123/0/emiqrasiya',
                  'birja.com/category/az/121/124/0/tikish',
                  'birja.com/category/az/121/125/0/repetitor',
                  'birja.com/category/az/121/126/0/tikinti-ve-temir',
                  'birja.com/category/az/121/127/0/diger',
                  'birja.com/category/az/121/128/0/berberlik',
                  'birja.com/category/az/121/129/0/dayelik',
                  'birja.com/category/az/121/130/0/mebel-yigilmasi-ve-temiri',
                  'birja.com/category/az/121/131/0/idman',
                  'birja.com/category/az/121/132/0/foto-ve-video',
                  'birja.com/category/az/121/133/0/huquqi',
                  'birja.com/category/az/121/134/0/it',
                  'birja.com/category/az/121/135/0/heyvanlar-uchun',
                  'birja.com/category/az/121/136/0/bag',
                  'birja.com/category/az/121/137/0/chatdirilma',
                  'birja.com/category/az/121/138/0/eylence',
                  'birja.com/category/az/121/139/0/meishet-texnikasinin-temiri',
                  'birja.com/category/az/121/140/0/komputerde-metnlerin-yigilmasi-ve-chapi',
                  'birja.com/category/az/121/141/0/reqs',
                  'birja.com/category/az/121/142/0/avto-ve-neqliyyat',
                  'birja.com/category/az/121/143/0/tehlukesizlik',
                  'birja.com/category/az/121/144/0/meishet',
                  'birja.com/category/az/121/145/0/xarici-diller-ve-tercume',
                  'birja.com/category/az/121/146/0/kurslar',
                  'birja.com/category/az/121/147/0/kosmetika',
                  'birja.com/category/az/121/148/0/ashpazliq',
                  'birja.com/category/az/121/149/0/masaj',
                  'birja.com/category/az/121/150/0/tibbi',
                  'birja.com/category/az/121/196/0/hamam-sauna',
                  'birja.com/category/az/151/152/0/biletler',
                  'birja.com/category/az/151/153/0/meishet-avadanliqlari',
                  'birja.com/category/az/151/154/0/erzaq',
                  'birja.com/category/az/151/155/0/ushaqlar-uchun',
                  'birja.com/category/az/151/156/0/oyun-konsollari',
                  'birja.com/category/az/151/157/0/telefon-nomreleri',
                  'birja.com/category/az/151/158/0/cevahirat',
                  'birja.com/category/az/151/159/0/bitkiler-ve-bag',
                  'birja.com/category/az/151/160/0/tikinti-materiallari',
                  'birja.com/category/az/151/161/0/mashinlari-avadanliqlari',
                  'birja.com/category/az/151/162/0/idman-turizm',
                  'birja.com/category/az/151/163/0/musiqi-aletleri',
                  'birja.com/category/az/151/164/0/ferqli',
                  'birja.com/category/az/151/165/0/derman',
                  'birja.com/category/az/151/166/0/mobil-telefonlar',
                  'birja.com/category/az/151/167/0/entiq-eshyalari',
                  'birja.com/category/az/151/168/0/saatlar-ve-zergerlik',
                  'birja.com/category/az/151/169/0/avadanliq-ve-meishet-cihazlari',
                  'birja.com/category/az/151/170/0/geyim-ayaqqabi-ve-tekstil',
                  'birja.com/category/az/151/171/0/tibbi-avadanliqlar',
                  'birja.com/category/az/151/172/0/mebel',
                  'birja.com/category/az/151/173/0/kosmetika',
                  'birja.com/category/az/151/174/0/kitablar-ve-jurnallar',
                  'birja.com/category/az/151/175/0/heyvanlar',
                  'birja.com/category/az/151/176/0/ofis-avadanligi',
                  'birja.com/category/az/151/177/0/pulsuz-qebul-edirem',
                  'birja.com/category/az/178/185/0/kredit',
                  'birja.com/category/az/178/188/0/kiraye-icare',
                  'birja.com/category/az/178/189/0/tanishliq',
                  'birja.com/category/az/178/197/0/biznes',
                  ]

    def parse(self, response):
        # Extract the href attributes from anchor elements on the current page
        links = response.css('div.cs_card_title a::attr(href)').getall()

        for link in links:
            # Follow the links to individual product pages and scrape data
            yield response.follow(link, self.parse_product, meta={'link': link})

        # Extract the next page link
        next_page = response.css('ul.pagination li.cs_active_pagination + li a::attr(href)').get()

        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_product(self, response):
        # Extract data from individual product pages
        link = response.request.meta['link']
        yield {
            'Link': link,
            'Phone': response.xpath('//td[a[contains(@href, "tel:")]]/a/@href').get(),
        }
