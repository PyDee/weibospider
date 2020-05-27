import time
import scrapy
import json
from ..items import UserInfo


class WeiboPhoneUserSpider(scrapy.Spider):
    name = 'phone_user'
    allowed_domains = ['m.weibo.cn']

    def start_requests(self):
        weibo_ids = [
            '3112824195',
            '1254320317',
            '6036529063',
            '3317061287',
            '2791246031',
            '3931589228',
            '5799410070',
            '6012033367',
            '3698434955',
            '5555858373',
            '5649090962',
            '5616417326',
            '6197250416',
            '7117289923',
            '3172594702',
            '5253397178',
            '6680210709',
            '3760131390',
            '2422998604',
            '3154731520',
            '1751721415',
            '3219744011',
            '6584944130',
            '6872067913',
            '2392083991',
            '7244976042',
            '5371073828',
            '2844310155',
            '6006349936',
            '2643306411',
            '5610345194',
            '6194928395',
            '2552808525',
            '1593923561',
            '1650772641',
            '1934731210',
            '5584388711',
            '2932564282',
            '5480245584',
            '2460484093',
            '5749045011',
            '3202581372',
            '6367594917',
            '7052908872',
            '1729297174',
            '1663662553',
            '5723675714',
            '2734152245',
            '6025820133',
            '7230746593',
            '1794192860',
            '6728015940',
            '5637860786',
            '6981521563',
            '1291418670',
            '6055901978',
            '2617908727',
            '5755294565',
            '2938201161',
            '1790403934',
            '7402748782',
            '7185943670',
            '2176075730',
            '6601889351',
            '3295704955',
            '6038303811',
            '6751363642',
            '5972979923',
            '2677961660',
            '6323549215',
            '3723286584',
            '2798586115',
            '7227199102',
            '1747988880',
            '5360628215',
            '3672684255',
            '6524276242',
            '5942223919',
            '2074380701',
            '5705849432',
            '2644134254',
            '2343130541',
            '3722171330',
            '5838338592',
            '5984303819',
            '6085862883',
            '3903477560',
            '5336806540',
            '2002259593',
            '2471590870',
            '5949884166',
            '2704501292',
            '6499871269',
            '5810429145',
            '5688834097',
            '1842003605',
            '6525919637',
            '5506465328',
            '3249067622',
            '5446893743',
            '6186374667',
            '3858746846',
            '6388051909',
            '3063124763',
            '5585120158',
            '7303546111',
            '6333979989',
            '2957800964',
            '5839995172',
            '1400805870',
            '1835124833',
            '5308187768',
            '1140112500',
            '6499382232',
            '6441549314',
            '5210301729',
            '6315551382',
            '2916424241',
            '3167662730',
            '5727404623',
            '6871655666',
            '5204448814',
            '6580387141',
            '5340156726',
            '3869711522',
            '7332613968',
            '5352801310',
            '5872333730',
            '2456118657',
            '5621309795',
            '3669900967',
            '7131946958',
            '5181170641',
            '3893648515',
            '5019369070',
            '5251824222',
            '2012860721',
            '3279342163',
            '2612675530',
            '3958383036',
            '5118257124',
            '7029880376',
            '2113486355',
            '2174184155',
            '5599802934',
            '1949264307',
            '7288430221',
            '5982915623',
            '2011074590',
            '5451758137',
            '2393554207',
            '5550696152',
            '3525106922',
            '2561975495',
            '5995111833',
            '6021925017',
            '5241231142',
            '6847586347',
            '5597517594',
            '7065307446',
            '2070449227',
            '6879169689',
            '1905669433',
            '3211832965',
            '1963459227',
            '3177348601',
            '1791135587',
            '3721643220',
            '5302127192',
            '6630999654',
            '2295359145',
            '2143920754',
            '6305598904',
            '2936914861',
            '6123978511',
            '5837414531',
            '6336678888',
            '3726173453',
            '5139870225',
            '3843137117',
            '6416980382',
            '6067911238',
            '3969344454',
            '5652427020',
            '3309735305',
            '7313124202',
            '6562073296',
            '6989587017',
            '5585427648',
            '5913871527',
            '1562921815',
            '1811624523',
            '5688133042',
            '6095748618',
            '5384533130',
            '3762053124',
            '5857371747',
            '6870373690',
            '5647296933',
            '7247100920',
            '2687930482',
            '3445573424',
            '6321309846',
            '6037598601',
            '2849281540',
            '6151747751',
            '7236151768',
            '6108128097',
            '2924534777',
            '3842947071',
            '3722010292',
            '5684514610',
            '6697210939',
            '2876557420',
            '2269789433',
            '2550560170',
            '2766829227',
            '5671913518',
            '6326022034',
            '5512631388',
            '5301899302',
            '2610036771',
            '5049741427',
            '5400658787',
            '6071661218',
            '7113043922',
            '5310902638',
            '3134254933',
            '7146863148',
            '5915040873',
            '2176869600',
            '5967713279',
            '2814394392',
            '5692764474',
            '5334360721',
            '6972114590',
            '5656904668',
            '6359529926',
            '5879398889',
            '7279515389',
            '2948003513',
            '3835544688',
            '2308491302',
            '2874210601',
            '6311473717',
            '5671546871',
            '1820479453',
            '3672449355',
            '5252852777',
            '1924399761',
            '7373144880',
            '6298453103',
            '5947101038',
            '5642224132',
            '5484769838',
            '6157303767',
            '3868994581',
            '2289735183',
            '5831380014',
            '6520174405',
            '7192259399',
            '1793068981',
            '5896051895',
            '3194743434',
            '6024121911',
            '3121258754',
            '6542505869',
            '3308788117',
            '5652153059',
            '1856822764',
            '6073693929',
            '5997742831',
            '2294734770',
            '6018725789',
            '3594031981',
            '5760765429',
            '6516538155',
            '1850586643',
            '5172160374',
            '5222997298',
            '3292495451',
            '2077432477',
            '6243562052',
            '5198304630',
            '3749603505',
            '2101100293',
            '5972785184',
            '6514748287',
            '7033101186',
            '3961249149',
            '2510266197',
            '5509277893',
            '5985082507',
            '5470432526',
            '5063941911',
            '5545908552',
            '6106071431',
            '7405669250',
            '5409737454',
            '1996620371',
            '1816737174',
            '3858329887',
            '6079876092',
            '3089730470',
            '2996327463',
            '2849207075',
            '2246618440',
            '5482534021',
            '5670725531',
            '5346636720',
            '5637650234',
            '6205965381',
            '5314453462',
            '2747031851',
            '5675249241',
            '5730054068',
            '5539504995',
            '5714867986',
            '6938307478',
            '1739855684',
            '1134500742',
            '6660821239',
            '1756725841',
            '1799625592',
            '2839821453',
            '7099942129',
            '5485577560',
            '3319473711',
            '6073614214',
            '1769236325',
            '1773041932',
            '5414408330',
            '7385009185',
            '2119379967',
            '5375391660',
            '1783516792',
            '2843944262',
            '7322450229',
            '6619871397',
            '1769786714',
            '3699036903',
            '3218439540',
            '2395580327',
            '7261218073',
            '5974720246',
            '2674365421',
            '5245753287',
            '6227463890',
            '2260880461',
            '6374881278',
            '5191178299',
            '3627368467',
            '1778628997',
            '1902624531',
            '6618404794',
            '5232037036',
            '5773642644',
            '5018069513',
            '6267678909',
            '1774740335',
            '2152024320',
            '3750833507',
            '1826026454',
            '2274500785',
            '6290817386',
            '5802499071',
            '3103047992',
            '6673425476',
            '1779636641',
            '6400846619',
            '5107717651',
            '5381569682',
            '6065389201',
            '5701531611',
            '6064345446',
            '6660101149',
            '2124841737',
            '3181447661',
            '5645036115',
            '6112935226',
            '1828448655',
            '5692192693',
            '7346234797',
            '1882584947',
            '5707933427',
            '2105542644',
            '2858399044',
            '3917647256',
            '2902068177',
            '5239029216',
            '2140925475',
            '1402213897',
            '5526365172',
            '2122842671',
            '2563692834',
            '5187480751',
            '6898065994',
            '1886802607',
            '1738882383',
            '1825950955',
            '5574738184',
            '2752973541',
            '2282816911',
            '6576322560',
            '3869584225',
            '5800215694',
            '5375816384',
            '3018812717',
            '3477432340',
            '2339077967',
            '5979133811',
            '5969943858',
            '1846856303',
            '3191504923',
            '5260610610',
            '5315284860',
            '5842526399',
            '5100839368',
            '1974676765',
            '7275154514',
            '6333528864',
            '1741787305',
            '2612345347',
            '1726101152',
            '5651051305',
            '2880981582',
            '6366020957',
            '5631467694',
            '5472248977',
            '6047064901',
            '6520899958',
            '5983356535',
            '1496837023',
            '3960346968',
            '2122837255',
            '6360668907',
            '5665829978',
            '5690919898',
            '5772848818',
            '5669113001',
            '5385063962',
            '6011717214',
            '5513321404',
            '6486468263',
            '6331684508',
            '6452879043',
            '1772359972',
            '6275120341',
            '6024828928',
            '5302297563',
            '1710388602',
            '2120387487',
            '5631307035',
            '5464976924',
            '7114504127',
            '5631765971',
            '5669845970',
            '1960815865',
            '6303147867',
            '2742929007',
            '1781268537',
            '5848537299',
            '2395691051',
            '2353186852',
            '5648919209',
            '1984516987',
            '6876898261',
            '5532141248',
            '5997969990',
            '5704039339',
            '2704159493',
            '2649681417',
            '2305785521',
            '6553430024',
            '5659965729',
            '5869642482',
            '6086486586',
            '1993632475',
            '7031134000',
            '2737168483',
            '5996081926',
            '5039882138',
            '2258923895',
            '3275662975',
            '1941206087',
            '5550001160',
            '2530658062',
            '6738398963',
            '6343932759',
            '5089084852',
            '2609260845',
            '1628320800',
            '6526853596',
            '1890042547',
            '6190771392',
            '5458646757',
            '5845610264',
            '6572986599',
            '6642064977',
            '3310429821',
            '6302126802',
            '5365858081',
            '6144602393',
            '3091141085',
            '1700100811',
            '6324271923',
            '5488216206',
            '6969859599',
            '2178787943',
            '6284582957',
            '6085780599',
            '2934827335',
            '5829980726',
            '5680500907',
            '6479071422',
            '6580092106',
            '6384872550',
            '5762483483',
            '5635798877',
            '2101560362',
            '6590937306',
            '5656744065',
            '7159455099',
            '5847598938',
            '5683704840',
            '1866161071',
            '6904814458',
            '3073535337',
            '7350880531',
            '1764416257',
            '2269661503',
            '7157698418',
            '3742673495',
            '1108189895',
            '5977512285',
            '5110749419',
            '6407947977',
            '6210434066',
            '6121144393',
            '3018609787',
            '3983752712',
            '5086148935',
            '7397652186',
            '6249652571',
            '2702512441',
            '1980658311',
            '5418800970',
            '5362593213',
            '5459284070',
            '5308936898',
            '3270740281',
            '3819034027',
            '2187480734',
            '1807129444',
            '2832261757',
            '5913616661',
            '6355118292',
            '1499055057',
            '6016012242',
            '6078360434',
            '2116036181',
            '3611343121',
            '2281771550',
            '2238260963',
            '5538914562',
            '5020771112',
            '1795609473',
            '6394238057',
            '6135658521',
            '2545712083',
            '3808037622',
            '6399544038',
            '2133927663',
            '5664496652',
            '1927829745',
            '7266097324',
            '6182956174',
            '5462827935',
            '7107980481',
        ]
        for weibo_id in weibo_ids:
            # if weibo_ids.index(weibo_id) == 167:
            #     break
            url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value={}'.format(weibo_id)
            '''
            profile，，2302833112824195
            weibo，，1076033112824195
            ablum，，1078033112824195
            https://m.weibo.cn/api/container/getIndex?type=uid&value=3112824195&containerid=1005053112824195
            '''
            # 交给调度器
            yield scrapy.Request(
                url=url,
                callback=self.parse
            )

    def parse(self, response):
        userItem = UserInfo()
        result = json.loads(response.text)
        a = {
            "province": "广东",
            "birthday": "巨蟹座",
            "labels": "旅游",
            # 'containerid' # todo 获取以上信息
        }

        gender = '男'
        result_data = result.get('data')
        user_info = result_data.get('userInfo')
        userItem['_id'] = user_info.get('id')
        userItem['nick_name'] = user_info.get('screen_name')
        userItem['crawl_time'] = int(time.time())
        userItem['gender'] = gender if user_info.get('gender') == 'm' else '女'
        userItem['brief_introduction'] = user_info.get('description')
        userItem['vip_level'] = user_info.get('mbrank')
        userItem['follows_num'] = user_info.get('follow_count')
        userItem['fans_num'] = user_info.get('followers_count')
        userItem['tweets_num'] = user_info.get('statuses_count')

        yield userItem
