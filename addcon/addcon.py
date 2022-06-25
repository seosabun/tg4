from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser, PeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, ChatWriteForbiddenError, \
    UserAlreadyParticipantError
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.channels import GetFullChannelRequest, JoinChannelRequest
from telethon import types, utils, errors
import configparser
import sys
import csv
from csv import reader
import traceback
import time
import random


with open('../memory.csv', 'r') as hash_obj:
    csv_reader = reader(hash_obj)
    list_of_rows = list(csv_reader)
    row_number = 1
    col_number = 1
    numdel = list_of_rows[row_number - 1][col_number - 1]

Legend = int(numdel)
global nextLegend
nextLegend = Legend + 1

with open('../phone.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    list_of_rows = list(csv_reader)
    row_number = Legend
    col_number = 1
    value = list_of_rows[row_number - 1][col_number - 1]

pphone = value



def autos():
    phone = utils.parse_phone(pphone)

    client = TelegramClient(f"../sessions/{phone}", 2392599, '7e14b38d250953c8c1e94fd7b2d63550')

    client.connect()
    if not client.is_user_authorized():
        print('some thing has changed')
        client.send_code_request(phone)
        client.sign_in(phone, input('Enter the code: '))

    input_file = '../data.csv'
    users = []
    with open(input_file, encoding='UTF-8') as f:
        rows = csv.reader(f, delimiter=",", lineterminator="\n")
        next(rows, None)
        for row in rows:
            user = {}
            user['srno'] = row[0]
            user['username'] = row[1]
            user['id'] = int(row[2])
            # user['access_hash'] = int(row[2])
            user['name'] = row[3]
            users.append(user)

    with open('../memory.csv', 'r') as hash_obj:
        csv_reader = reader(hash_obj)
        list_of_rows = list(csv_reader)
        row_number = 1
        col_number = 2
        numnext = list_of_rows[row_number - 1][col_number - 1]

    startfrom = int(numnext)
    nextstart = startfrom + 60

    with open('../memory.csv', 'r') as hash_obj:
        csv_reader = reader(hash_obj)
        list_of_rows = list(csv_reader)
        row_number = 1
        col_number = 3
        numend = list_of_rows[row_number - 1][col_number - 1]

    endto = int(numend)
    nextend = endto + 60

    with open("../memory.csv", "w", encoding='UTF-8') as df:  # Enter your file name.
        writer = csv.writer(df, delimiter=",", lineterminator="\n")
        writer.writerow([nextLegend, nextstart, nextend])

    for user in users:
        if (int(startfrom) <= int(user['srno'])) and (int(user['srno']) <= int(endto)):
            try:
                status = 'Legend'
                if user['username'] == "":
                    print("no username, moving to next")
                    continue

                client(functions.contacts.AddContactRequest(
                    id=user['username'],
                    first_name=user['name'],
                    last_name='',
                    phone='',
                    add_phone_privacy_exception=True, )
                )
                status = 'DONE'
                
                time.sleep(random.randrange(0, 4))

            except UserPrivacyRestrictedError:
                status = 'PrivacyRestrictedError'


            except UserAlreadyParticipantError:
                status = 'ALREADY'


            except PeerFloodError as g:
                status = 'PeerFloodError :('
                print('Script Is Stopping Now, Dont Use This Account For The Next 24 Hours')
                time.sleep(86400)






            except errors.RPCError as e:
                status = e.__class__.__name__


            except Exception as d:
                status = d

            except:
                traceback.print_exc()
                print("Unexpected Error")
                continue


            print(f"ADDED > {status} ")
        elif int(user['srno']) > int(endto):
            print("Members Added To Contact. Successfully!")
            quit()


autos()


