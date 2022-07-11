import vk_api
import random
import time
import logging

session = vk_api.VkApi(token='vk1.a.UrMyw5v8ST--lhpnGwdWjo-Zzqxff6u5xNtnokHx3dOX8GoTBYYk80R6kJ9Ctj69OsaIkueLROxZ_NUD26mUBU9_9301WOTc8Isyu3B51YGPW9JG95ZI3T2s8UJCURxp1aJbNwni2GPz5-Db_kDf9EJ-xyLxb5d0YFc9L0nIYk_BLBhanGdJ6IoxaMcW9Y02')
listmsg = ['Спасибо, хороший пост👍🏻', 'Спасибо за информацию😊', '👍🏻', 'Люблю вас читать', '😊 Согласна с автором', '❤', 'Ждем следующий пост)', 'Интересно', 'У вас в паблике посты интересные, можно поучиться новому', '💚', '👍🏻👍🏻', '☺']

# recieve name of vk groups from txt file
with open('group.txt', 'r') as g_file:
    owner_id = g_file.read().splitlines()
y = 210997141 #идентификатор группы ШС

def spam(owner_id):
        for id in owner_id: #перебор владельцев пабликов
            time.sleep(20)
            print(id, '- взяли номер паблика из списка')
            g = session.method('wall.get', {'owner_id': id, 'count': 2})  # заменил на id s owner_id
            for id_post in g['items']:
                x = id_post.get('id')  # вывод номера поста последнего
                print(x, '- номер последнего поста')
                comments = session.method('wall.getComments', {'owner_id': id, 'post_id': x})  # заменил на id s owner_id
                print('взяли коментарии к посту', comments)
                block = 0
                if comments['count'] < 5:
                    for comment in comments['items']:
                        com_int = comment['from_id']
                        if com_int == -210997141:
                            print('-> уже есть наш комментарий')
                            block = 1
                    if block == 0:
                        print('-> оставим комментарий на пост -', x, ' от паблика', y )
                        try:
                            session.method('wall.createComment',
                                        {'owner_id': id, 'post_id': x, 'from_group': y, 'message': random.choice(listmsg)})
                        except Exception as err:
                            print('%%% Произошла ошибка:', err)
                            pass
                else:
                    print('комментариев у поста >  5')
            print('------------------')


if __name__ == '__main__':
    spam(owner_id)