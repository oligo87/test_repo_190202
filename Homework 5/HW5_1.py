import requests
base_url = 'http://pulse-rest-testing.herokuapp.com'

r_post_item = requests.post(base_url+'/roles', data={'name': 'Hero 1', 'type': 'Supernatural', 'level': 5, 'book': 104})
role = r_post_item.json()
print(role)
role_id = str(role['id'])

r_get_item = requests.get(base_url+'/roles/'+role_id)
print(r_get_item.json())

r_get_list = requests.get(base_url+'/roles')
print(r_get_list.json())

r_put = requests.put(base_url+'/roles/'+role_id, data={'name': 'Hero Changed', 'level': 6})
r_get_item = requests.get(base_url+'/roles/'+role_id)
print(r_get_item.json())

r_get_list = requests.get(base_url+'/roles')
print(r_get_list.json())

r_del_item = requests.delete(base_url+'/roles/'+role_id)
