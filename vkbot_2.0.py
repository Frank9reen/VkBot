# Задача сделать работу с КАПЧЕЙ
# issue запуск скрипта не в 10-00 по мск, т.к. в группах часто пост рекламы выходит в это время
# удаление номера паблика из списка где я в БЛ remove
# https://lolz.guru/threads/3784089/ https://pypi.org/project/vk-captchasolver/
# не получается выводить каптчу - не выходит

import vk_api
import random
import time
import logging

import sys
import os
from twocaptcha import TwoCaptcha

#solver = TwoCaptcha('4945b6384e61ba0351b671edf204c038')

session = vk_api.VkApi(token='vk1.a.UrMyw5v8ST--lhpnGwdWjo-Zzqxff6u5xNtnokHx3dOX8GoTBYYk80R6kJ9Ctj69OsaIkueLROxZ_NUD26mUBU9_9301WOTc8Isyu3B51YGPW9JG95ZI3T2s8UJCURxp1aJbNwni2GPz5-Db_kDf9EJ-xyLxb5d0YFc9L0nIYk_BLBhanGdJ6IoxaMcW9Y02')
listmsg = ['Спасибо, хороший пост👍🏻', 'Спасибо за информацию😊', '👍🏻', 'Люблю вас читать', '😊 Согласна с автором', '❤', 'Ждем следующий пост)', 'Интересно', 'У вас в паблике посты интересные, можно поучиться новому', '💚', '👍🏻👍🏻', '☺']

# recieve name of vk groups from txt file
with open('group.txt', 'r') as g_file:
    owner_id = g_file.read().splitlines()
y = 210997141 #идентификатор группы ШС

def spam(owner_id):
        for id in owner_id: #перебор владельцев пабликов
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
                        # except Exception as err:
                        #     print('%%% Произошла ошибка:', err)
                        #     pass
                        except vk_api.exceptions.Captcha as captcha:
                            print(captcha.sid)
                            print(captcha.get_url())
                            print(captcha.get_image())

                            sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
                            api_key = os.getenv('4945b6384e61ba0351b671edf204c038',
                                                'vk1.a.UrMyw5v8ST--lhpnGwdWjo-Zzqxff6u5xNtnokHx3dOX8GoTBYYk80R6kJ9Ctj69OsaIkueLROxZ_NUD26mUBU9_9301WOTc8Isyu3B51YGPW9JG95ZI3T2s8UJCURxp1aJbNwni2GPz5-Db_kDf9EJ-xyLxb5d0YFc9L0nIYk_BLBhanGdJ6IoxaMcW9Y02')
                            solver = TwoCaptcha(api_key)
                            try:
                                result = solver.normal('path/to/captcha.jpg')
                            except Exception as e:
                                sys.exit(e)
                            else:
                                sys.exit('solved: ' + str(result))


                        except Exception as err:
                            print('%%% Произошла ошибка:', err)
                else:
                    print('комментариев у поста >  5')
            print('------------------')





if __name__ == '__main__':
    spam(owner_id)

    # logging.basicConfig(
    #     level=logging.ERROR,
    #     filename="vkbot.log",
    #     format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    #     datefmt='%H:%M:%S',
    # )
    # logging.info('info message', err)

                    # if 0 < comments['count'] < 15:
                    #     print('комментарии есть, но нашего нет - оставляем')

                #     for comment in comments['items']:
                #         com_int = comment['from_id']
                #         if com_int == 225247:
                #             print('est nash komment')
                #         else:
                #             print('комментарии есть, но нашего нет - оставляем')
                #             session.method('wall.createComment',
                #                            {'owner_id': owner_id, 'post_id': x, 'message': random.choice(listmsg)})
                #             print('-comment ostavlen')
                #             session.method("likes.add", {'type': 'post', 'owner_id': owner_id, 'item_id': x})
                # elif comments['count'] > 6:
                #     print('слишком много коментариев')




                    #
                    # elif 0 < comments['count'] <5: # отсюда править
                    #     print('коментариев от 0 до 5')
                    #     if com_int == 225247:
                            #             print('our post is already exist')
                        # for comment in comments['items']:
                        #     com_int = comment['from_id']
                        #     print(comment)
                        #     print(com_int)
                        #     print('нашего комментария нет - оставляем свой')
                        #     session.method('wall.createComment',
                        #                     {'owner_id': owner_id, 'post_id': x, 'message': random.choice(listmsg)})
                        #     print('-comment ostavlen')
                        #     session.method("likes.add", {'type': 'post', 'owner_id': owner_id, 'item_id': x})


                # for comment in comments['items']:
                #     com_int = comment.get('from_id')
                #     print('номер поста', x, 'от кого комментарий', com_int)
                #print('comments uzhe est')

                # else:
                #     for comment in comments['items']: # проверка есть ли уже наш комментарий у поста
                #         com_int = comment['from_id']
                #         if com_int == 225247:
                #             print('our post is already exist')
                #         else:
                #             session.method('wall.createComment', {'owner_id': owner_id, 'post_id': x, 'message': random.choice(listmsg)})
                #             session.method("likes.add", {'type': 'post', 'owner_id': owner_id, 'item_id': x})



    # def spam(owner_id):
    #     try:
    #         for id in owner_id:
    #             g = session.method('wall.get', {'owner_id': owner_id, 'count': 1})
    #             for id_post in g['items']:
    #                 # time.sleep(60)
    #                 x = id_post.get('id')  # вывод номера поста последнего
    #                 print(x)
    #                 comments = session.method('wall.getComments', {'owner_id': owner_id, 'post_id': x})
    #                 if comments['count'] == 0:
    #                     print('no comments')
    #                     session.method('wall.createComment',
    #                                    {'owner_id': owner_id, 'post_id': x, 'message': random.choice(listmsg)})
    #                     session.method("likes.add", {'type': 'post', 'owner_id': owner_id, 'item_id': x})
    #                 else:
    #                     for comment in comments['items']:  # проверка есть ли уже наш комментарий у поста
    #                         com_int = comment['from_id']
    #                         if com_int == 225247:
    #                             print('our post is already exist')
    #                         else:
    #                             session.method('wall.createComment',
    #                                            {'owner_id': owner_id, 'post_id': x, 'message': random.choice(listmsg)})
    #                             session.method("likes.add", {'type': 'post', 'owner_id': owner_id, 'item_id': x})
    #     except Exception as err:
    #         print('Произошла ошибка')

    # # recieve id of post in group #wall.getById
    # def spisok_zapisei(owner_id):
    #     g = session.method('wall.get', {
    #         'owner_id': owner_id,
    #         'count': 1,
    #     })
    #     for id_post in g['items']:
    #         x = id_post.get('id')
    #         print(x)
    #         return x


    # for group_item in owner_id:
    #     g = session.method('wall.get', {
    #         'owner_id': owner_id,
    #         'count': 1,
    #     })

        # for id_post in g['items']:
        #     x = id_post.get('id')
        #     print(x)
        # print(group_item)
        # spisok_zapisei(-210997141)




# def comment_group(owner_id, post_id, texts):
#     session.method('wall.createComment', {
#         'owner_id': owner_id,
#         'post_id': post_id,
#         'message': texts,
#     })
# #comment_group(-210997141, 228, 'tests')




# def comment_group(owner_id, post_id, texts):
#     session.method('wall.createComment', {
#         'owner_id': owner_id,
#         'post_id': post_id,
#         'message': texts
#     })
# comment_group(225247, 3069, 'tests')


# def spam(group):
#     count = 0
#     kol = 0
#     while True:
#         try:
#             for g in group:
#                 resp = session.method("wall.createComment", {'owner_id': -210997141, 'post_id': 457239287, 'message': 'test'})
#                 #count += 1
#         except:
#             pass

# #get status of user and set it
# def get_user_status(user_id):
#     friends = session.method('friends.get', {'user_id': user_id})
#     #status = session.method('status.get', {'user_id': user_id})
#     #print(status['text'])
#     for friend in friends["items"]:
#         user = session.method("users.get", {'user_ids': friends})
#         print(user)
#
# # send message to user
# def send_message(user_id):
#     session.method("messages.send", {
#         "user_id": user_id,
#         "message": "Some text",
#         "random_id": 0
#     })
#
# # send like on post
# def send_like(owner_id, item_id):
#     session.method("likes.add", {
#         'type': 'post',
#         'owner_id': owner_id,
#         'item_id': item_id
#     })
#     #post = session.method('wall.get', {"user_id": user_id})
#     #print(post)
#
# send_like(1738628, 1624)
#

#send_message(1738628)
#get_user_status(225247)

