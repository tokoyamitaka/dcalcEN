from tokenize import Number


data = {
  "0":{
    "id": 0,
    "name": "120沙袋(绿)",
    "防御": 443243,
    "火抗": 0,
    "冰抗": 0,
    "光抗": 0,
    "暗抗": 0
  },
  "1":{
    "id": 1,
    "name": "130沙袋",
    "防御": 506109,
    "火抗": 0,
    "冰抗": 0,
    "光抗": 0,
    "暗抗": 0
  },

}


def get_monster_data(id):
    return data.get(id,{
    "id": 0,
    "name": "120沙袋(绿)",
    "防御": 443243,
    "火抗": 0,
    "冰抗": 0,
    "光抗": 0,
    "暗抗": 0
  })