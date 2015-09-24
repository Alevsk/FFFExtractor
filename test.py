#!/usr/bin/env python

import httplib
import zlib

conn = httplib.HTTPSConnection("www.facebook.com")

headers = {
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36",
    'accept': "*/*",
    'referer': "https//www.facebook.com/search/189386589649/likers",
    'accept-encoding': "gzip, deflate, sdch",
    'accept-language': "es-ES,es;q=0.8",
    'cookie': "datr=d8GZVehvehoQQUwJYHtAYTHw; js_ver=2089; a11y=%7B%22sr%22%3A0%2C%22sr-ts%22%3A1442943982937%2C%22jk%22%3A0%2C%22jk-ts%22%3A1442943982937%2C%22kb%22%3A1%2C%22kb-ts%22%3A1442977936362%2C%22hcm%22%3A0%2C%22hcm-ts%22%3A1442943982937%7D; c_user=1078496755; fr=045EqER6breGo38NM.AWW776aghpJ-5NvzcwBh5LzQ-HY.BTcmu4.q6.FXy.0.AWUQpKID; xs=228%3AF9oQ60QpZG1_yQ%3A2%3A1420843044%3A2849; csm=2; s=Aa6cYt9nuc5iF4Nw.BVxUkP; lu=gheYJIujtZqjPojhw1oIa6hw; act=1442985916159%2F6; p=-2; presence=EDvF3EtimeF1442986031EuserFA21078496755A2EstateFDsb2F1442983040781Et2F_5bDiFA2thread_3a638416782911399A2EsiFA2638416782911399A2C_5dElm2FnullEuct2F1442982476538EtrFA2loadA2EtwF1104251781EatF1442986031123G442986031286CEchFDp_5f1078496755F18CC; datr=d8GZVehvehoQQUwJYHtAYTHw; js_ver=2089; a11y=%7B%22sr%22%3A0%2C%22sr-ts%22%3A1442943982937%2C%22jk%22%3A0%2C%22jk-ts%22%3A1442943982937%2C%22kb%22%3A1%2C%22kb-ts%22%3A1442977936362%2C%22hcm%22%3A0%2C%22hcm-ts%22%3A1442943982937%7D; c_user=1078496755; fr=045EqER6breGo38NM.AWUTRCzbOYX3jQyAoSobIPXMB_Y.BTcmu4.q6.FXy.0.AWXAQZMO; xs=228%3AF9oQ60QpZG1_yQ%3A2%3A1420843044%3A2849; csm=2; s=Aa6cYt9nuc5iF4Nw.BVxUkP; lu=gh213iihjslaMahUZQ7pmkIw; act=1443045740357%2F4; p=-2; presence=EDvF3EtimeF1443046161EuserFA21078496755A2EstateFDsb2F1443043376847Et2F_5bDiFA2thread_3a638416782911399A2EsiFA2638416782911399A2C_5dElm2FnullEuct2F1442982476538EtrFA2loadA2EtwF1885337184EatF1443046134608G443046161175CEchFDp_5f1078496755F12CC; wd=1280x702"
    }

conn.request("GET", "/ajax/pagelet/generic.php/BrowseScrollingSetPagelet?data=%7B%22typeahead_sid%22%3A%22%22%2C%22tr%22%3Anull%2C%22topic_id%22%3Anull%2C%22em%22%3Afalse%2C%22mr%22%3Afalse%2C%22view%22%3A%22list%22%2C%22display_params%22%3A%5B%5D%2C%22logger_source%22%3A%22www_main%22%2C%22encoded_query%22%3A%22%7B%5C%22bqf%5C%22%3A%5C%22likers(189386589649)%5C%22%2C%5C%22vertical%5C%22%3A%5C%22none%5C%22%2C%5C%22post_search_vertical%5C%22%3Anull%2C%5C%22intent_data%5C%22%3Anull%2C%5C%22query_analysis%5C%22%3Anull%7D%22%2C%22trending_source%22%3Anull%2C%22has_top_pagelet%22%3Anull%2C%22ref_path%22%3A%22%2Fsearch%2F189386589649%2Flikers%22%2C%22tl_log%22%3Afalse%2C%22encoded_title%22%3A%22WyJQZW9wbGUrd2hvK2xpa2UrIix7InRleHQiOiJVbml2ZXJzaWRhZCtQYW5hbWVyaWNhbmEiLCJ1aWQiOjE4OTM4NjU4OTY0OSwidHlwZSI6InBhZ2UifV0%22%2C%22is_trending%22%3Afalse%2C%22page_number%22%3A2%2C%22browse_location%22%3A%22%22%2C%22filter_ids%22%3A%7B%22520053742%22%3A520053742%2C%221066595962%22%3A1066595962%2C%221406468036%22%3A1406468036%2C%22100000891774285%22%3A100000891774285%7D%2C%22callsite%22%3A%22browse_ui%3Ainit_result_set%22%2C%22cursor%22%3A%22AbqJ-EyP7OY0pDVuWBDLB_0_h9ZhUWZxBXx_JKvTbdC1JnHcaunquJHcKDLSVPIUZa7sBeKhWsTHg-7yEpc_iXlxVTMiKJ82UsEAIx7nq68S3id49XceO4RwiYmgmJFyUV6auKW0deRHjHoVeRecMc-EY7Ps44FNylnBcc8RCGOIGA%22%2C%22exclude_ids%22%3Anull%2C%22impression_id%22%3A%229d6ea2b2%22%2C%22ref%22%3A%22unknown%22%2C%22experience_type%22%3A%22grammar%22%2C%22story_id%22%3Anull%7D&__user=1078496755&__a=1&__dyn=7AmajEyl2qm9ongDxiWOGeFDzECiq2WiqAdy9VCC-K26m5-bzES2N6y8-bxu3fzoat1bxjx27W88xi5VJ1efKiVWz9EpwzxO2OE&__req=k&__rev=1951399", headers=headers)

res = conn.getresponse()

print res.status, res.reason
#print res.getheaders()

data = res.read()
decompress = zlib.decompress(data, 16+zlib.MAX_WBITS)

print decompress.decode('utf-8')

