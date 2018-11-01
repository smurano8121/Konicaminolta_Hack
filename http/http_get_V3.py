import requests
import json

def Json_get():
    headers = {"content-type": "application/json"}
    json_str = requests.get('http://ec2-13-231-238-116.ap-northeast-1.compute.amazonaws.com:3000/users', headers=headers)
    print(json_str)
    json_dict = json_str.json()
    print(json_dict[0])
    print('json_dict:{}'.format(json_dict[0]["user_name"]))
    #
    json_str = '''
    {
         "user_id":"1",
         "start":"riku"
    }
    '''
    # json_dict = json.loads(str(json_str))
    # print(json_dict)
    # print(json_str.status_code)    # HTTPのステータスコード取得
    # print(json_str.text)    # レスポンスのHTMLを文字列で取得

Json_get()

# def Json_get():
#  response = requests.post('https://jsondata.okiba.me/v1/json/m1NvW180922122602', data={'user_id': 'bar'})
#     print(response.status_code)    # HTTPのステータスコード取得
#     print(response.text)    # レスポンスのHTMLを文字列で取得
