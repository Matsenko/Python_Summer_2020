import discord
import random
TOKEN = 'NzIxMzk5NTExNzcxMTE5NjE2.XuUWYA.UMjYaIpJsylWSC4caFoOdyNTDEA'
list1=[]
client = discord.Client()
bot_player={}
win_bot=[]
win_bot.append(0)
win_player=[]
win_player.append(0)
bot_player={"Бот":win_bot,
"Игрок":win_player
}
first_comand=[
"##################################################",
" Что бы начать игру нужно ввести команду !start   ",
"##################################################"
]
second_comand=[
"#################",
" Выход из игры...",
"#################"
]
# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------

# def get_bot_player():
#     return bot_player
#######################################
            # Не працює
#######################################
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    # async def choice_3():
        # print(message.author.mention + "\n" + "поставил\n"+list1[0].lower()+".\n\n")
        # list2=['Бумага','Камень','Ножницы']
        # rand=random.choice(list2)
        # if(list1[0]==rand):
        #     await message.channel.send("Бот поставил  " + rand.lower()+".")
        #     await message.channel.send("Ничья!")
        #     bot_player={"Бот":win_bot[-1],
        #     "Игрок":win_player[-1]
        #     }
        #     await message.channel.send("Бот - "+ str(bot_player["Бот"]) +"\n")
        #     await message.channel.send("Игрок - "+ str(bot_player["Игрок"]) +"\n")
        #     print("\n\nБот - "+ str(bot_player["Бот"]) +"\n")
        #     print("Игрок - "+ str(bot_player["Игрок"]) +"\n")
        # if(list1[0]=='Бумага'and rand=='Камень'):
        #     await message.channel.send("Бот поставил  " + rand.lower()+".")
        #     await message.channel.send("Вы победили!")
        #     win_player.append(win_player[-1]+1)
        #     bot_player={"Бот":win_bot[-1],
        #     "Игрок":win_player[-1]
        #     }
        #     await message.channel.send("Бот - "+ str(bot_player["Бот"]) +"\n")
        #     await message.channel.send("Игрок - "+ str(bot_player["Игрок"]) +"\n")
        #     print("\n\nБот - "+ str(bot_player["Бот"]) +"\n")
        #     print("Игрок - "+ str(bot_player["Игрок"]) +"\n")
        # if(list1[0]=='Камень'and rand=='Бумага'):
        #     await message.channel.send("Бот поставил  " + rand.lower()+".")
        #     await message.channel.send("Вы проиграли!")
        #     win_bot.append(win_bot[-1]+1)
        #     bot_player={"Бот":win_bot[-1],
        #     "Игрок":win_player[-1]
        #     }
        #     await message.channel.send("Бот - "+ str(bot_player["Бот"]) +"\n")
        #     await message.channel.send("Игрок - "+ str(bot_player["Игрок"]) +"\n")
        #     print("\n\nБот - "+ str(bot_player["Бот"]) +"\n")
        #     print("Игрок - "+ str(bot_player["Игрок"]) +"\n")
        # if(list1[0]=='Ножницы'and rand=='Камень'):
        #     await message.channel.send("Бот поставил  " + rand.lower()+".")
        #     await message.channel.send("Вы проиграли!")
        #     win_bot.append(win_bot[-1]+1)
        #     bot_player={"Бот":win_bot[-1],
        #     "Игрок":win_player[-1]
        #     }
        #     await message.channel.send("Бот - "+ str(bot_player["Бот"]) +"\n")
        #     await message.channel.send("Игрок - "+ str(bot_player["Игрок"]) +"\n")
        #     print("\n\nБот - "+ str(bot_player["Бот"]) +"\n")
        #     print("Игрок - "+ str(bot_player["Игрок"]) +"\n")
        # if(list1[0]=='Камень'and rand=='Ножницы'):
        #     await message.channel.send("Бот поставил  " + rand.lower()+".")
        #     await message.channel.send("Вы победили!")
        #     win_player.append(win_player[-1]+1)
        #     bot_player={"Бот":win_bot[-1],
        #     "Игрок":win_player[-1]
        #     }
        #     await message.channel.send("Бот - "+ str(bot_player["Бот"]) +"\n")
        #     await message.channel.send("Игрок - "+ str(bot_player["Игрок"]) +"\n")
        #     print("\n\nБот - "+ str(bot_player["Бот"]) +"\n")
        #     print("Игрок - "+ str(bot_player["Игрок"]) +"\n")
        # if(list1[0]=='Бумага'and rand=='Ножницы'):
        #     await message.channel.send("Бот поставил  " + rand.lower()+".")
        #     await message.channel.send("Вы проиграли!")
        #     win_bot.append(win_bot[-1]+1)
        #     bot_player={"Бот":win_bot[-1],
        #     "Игрок":win_player[-1]
        #     }
        #     await message.channel.send("Бот - "+ str(bot_player["Бот"]) +"\n")
        #     await message.channel.send("Игрок - "+ str(bot_player["Игрок"]) +"\n")
        #     print("\n\nБот - "+ str(bot_player["Бот"]) +"\n")
        #     print("Игрок - "+ str(bot_player["Игрок"]) +"\n")
        # if(list1[0]=='Ножницы'and rand=='Бумага'):
        #     await message.channel.send("Бот поставил  " + rand.lower()+".")
        #     await message.channel.send("Вы победили!")
        #     win_player.append(win_player[-1]+1)
        #     bot_player={"Бот":win_bot[-1],
        #     "Игрок":win_player[-1]
        #     }
        #     await message.channel.send("Бот - "+ str(bot_player["Бот"]) +"\n")
        #     await message.channel.send("Игрок - "+ str(bot_player["Игрок"]) +"\n")
        #     print("\n\nБот - "+ str(bot_player["Бот"]) +"\n")
        #     print("Игрок - "+ str(bot_player["Игрок"]) +"\n")
        #######################################
                    # Не працює
        #######################################
    if message.author == client.user:
        return
    if message.content.startswith('!help'):
        await message.channel.send(first_comand[0]+'\n'+first_comand[1]+'\n'+first_comand[2])
    if message.content.startswith('!start'):
        await message.channel.send("Привет,это игра'Камень, ножницы, бумага'")
        await message.channel.send("Ты хочешь сыграть?!Да/!Нет.")
    if message.content.startswith('!Да'):
        await message.channel.send("Если что,вот правила игры:\n")
        await message.channel.send("##############################################################################################################################################################################################################################")
        await message.channel.send("|Правила игры:\n")
        await message.channel.send("|Игроки считают вместе вслух «Камень… Ножницы… Бумага… Раз… Два… Три», одновременно качая кулаками.\n")
        await message.channel.send("|Существуют и другие варианты счёта, распространённость которых различается в разных городах и регионах, например, «Рас(е)л-двас(е)л-трис(е)л!», «Эна-бена-цо!», «Су-ли-фа», «Ю-зе-фа», «Бу-це-фа», «Аль… ман… джуз!» и др.\n")
        await message.channel.send("|На счёт «Три» они одновременно показывают при помощи руки один из трёх знаков: камень, ножницы или бумагу.\n ")
        await message.channel.send("|Победитель определяется по следующим правилам: \n\n")
        await message.channel.send("|Бумага побеждает камень («бумага обёртывает камень»).\n")
        await message.channel.send("|Ножницы побеждают бумагу («ножницы разрезают бумагу»).\n")
        await message.channel.send("|Камень побеждает ножницы («камень затупляет или ломает ножницы»).\n")
        await message.channel.send("|Если игроки показали одинаковый знак, то засчитывается ничья и игра переигрывается.")
        await message.channel.send("##############################################################################################################################################################################################################################")
        await message.channel.send("Введи !камень,!ножницы или !бумага.PS:С большой буквы.")
    elif message.content.startswith('!Нет'):
        await message.channel.send(second_comand[0]+'\n'+second_comand[1]+'\n'+second_comand[2])
# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
    if message.content.startswith('!Камень'):
        list1=[]
        list1.append("Камень")
        print(message.author.mention + "\n" + "поставил\n"+list1[0].lower()+".\n\n")
        list2=['Бумага','Камень','Ножницы']
        rand=random.choice(list2)
        if(list1[0]==rand):
            await message.channel.send("Бот поставил  " + rand.lower()+".")
            await message.channel.send("Ничья!")
            bot_player={"Бот":win_bot[-1],
            "Игрок":win_player[-1]
            }
            await message.channel.send("Бот - "+ str(bot_player["Бот"]) +"\n")
            await message.channel.send("Игрок - "+ str(bot_player["Игрок"]) +"\n")
            print("\n\nБот - "+ str(bot_player["Бот"]) +"\n")
            print("Игрок - "+ str(bot_player["Игрок"]) +"\n")
        if(list1[0]=='Бумага'and rand=='Камень'):
            await message.channel.send("Бот поставил  " + rand.lower()+".")
            await message.channel.send("Вы победили!")
            win_player.append(win_player[-1]+1)
            bot_player={"Бот":win_bot[-1],
            "Игрок":win_player[-1]
            }
            await message.channel.send("Бот - "+ str(bot_player["Бот"]) +"\n")
            await message.channel.send("Игрок - "+ str(bot_player["Игрок"]) +"\n")
            print("\n\nБот - "+ str(bot_player["Бот"]) +"\n")
            print("Игрок - "+ str(bot_player["Игрок"]) +"\n")
        if(list1[0]=='Камень'and rand=='Бумага'):
            await message.channel.send("Бот поставил  " + rand.lower()+".")
            await message.channel.send("Вы проиграли!")
            win_bot.append(win_bot[-1]+1)
            bot_player={"Бот":win_bot[-1],
            "Игрок":win_player[-1]
            }
            await message.channel.send("Бот - "+ str(bot_player["Бот"]) +"\n")
            await message.channel.send("Игрок - "+ str(bot_player["Игрок"]) +"\n")
            print("\n\nБот - "+ str(bot_player["Бот"]) +"\n")
            print("Игрок - "+ str(bot_player["Игрок"]) +"\n")
        if(list1[0]=='Ножницы'and rand=='Камень'):
            await message.channel.send("Бот поставил  " + rand.lower()+".")
            await message.channel.send("Вы проиграли!")
            win_bot.append(win_bot[-1]+1)
            bot_player={"Бот":win_bot[-1],
            "Игрок":win_player[-1]
            }
            await message.channel.send("Бот - "+ str(bot_player["Бот"]) +"\n")
            await message.channel.send("Игрок - "+ str(bot_player["Игрок"]) +"\n")
            print("\n\nБот - "+ str(bot_player["Бот"]) +"\n")
            print("Игрок - "+ str(bot_player["Игрок"]) +"\n")
        if(list1[0]=='Камень'and rand=='Ножницы'):
            await message.channel.send("Бот поставил  " + rand.lower()+".")
            await message.channel.send("Вы победили!")
            win_player.append(win_player[-1]+1)
            bot_player={"Бот":win_bot[-1],
            "Игрок":win_player[-1]
            }
            await message.channel.send("Бот - "+ str(bot_player["Бот"]) +"\n")
            await message.channel.send("Игрок - "+ str(bot_player["Игрок"]) +"\n")
            print("\n\nБот - "+ str(bot_player["Бот"]) +"\n")
            print("Игрок - "+ str(bot_player["Игрок"]) +"\n")
        if(list1[0]=='Бумага'and rand=='Ножницы'):
            await message.channel.send("Бот поставил  " + rand.lower()+".")
            await message.channel.send("Вы проиграли!")
            win_bot.append(win_bot[-1]+1)
            bot_player={"Бот":win_bot[-1],
            "Игрок":win_player[-1]
            }
            await message.channel.send("Бот - "+ str(bot_player["Бот"]) +"\n")
            await message.channel.send("Игрок - "+ str(bot_player["Игрок"]) +"\n")
            print("\n\nБот - "+ str(bot_player["Бот"]) +"\n")
            print("Игрок - "+ str(bot_player["Игрок"]) +"\n")
        if(list1[0]=='Ножницы'and rand=='Бумага'):
            await message.channel.send("Бот поставил  " + rand.lower()+".")
            await message.channel.send("Вы победили!")
            win_player.append(win_player[-1]+1)
            bot_player={"Бот":win_bot[-1],
            "Игрок":win_player[-1]
            }
            await message.channel.send("Бот - "+ str(bot_player["Бот"]) +"\n")
            await message.channel.send("Игрок - "+ str(bot_player["Игрок"]) +"\n")
            print("\n\nБот - "+ str(bot_player["Бот"]) +"\n")
            print("Игрок - "+ str(bot_player["Игрок"]) +"\n")
# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
    if message.content.startswith('!Бумага'):
        list1=[]
        list1.append("Бумага")
        print(message.author.mention + "\n" + "поставил\n"+list1[0].lower()+".\n\n")
        list2=['Бумага','Камень','Ножницы']
        rand=random.choice(list2)
        if(list1[0]==rand):
            await message.channel.send("Бот поставил  " + rand.lower()+".")
            await message.channel.send("Ничья!")
            bot_player={"Бот":win_bot[-1],
            "Игрок":win_player[-1]
            }
            await message.channel.send("Бот - "+ str(bot_player["Бот"]) +"\n")
            await message.channel.send("Игрок - "+ str(bot_player["Игрок"]) +"\n")
            print("\n\nБот - "+ str(bot_player["Бот"]) +"\n")
            print("Игрок - "+ str(bot_player["Игрок"]) +"\n")
        if(list1[0]=='Бумага'and rand=='Камень'):
            await message.channel.send("Бот поставил  " + rand.lower()+".")
            await message.channel.send("Вы победили!")
            win_player.append(win_player[-1]+1)
            bot_player={"Бот":win_bot[-1],
            "Игрок":win_player[-1]
            }
            await message.channel.send("Бот - "+ str(bot_player["Бот"]) +"\n")
            await message.channel.send("Игрок - "+ str(bot_player["Игрок"]) +"\n")
            print("\n\nБот - "+ str(bot_player["Бот"]) +"\n")
            print("Игрок - "+ str(bot_player["Игрок"]) +"\n")
        if(list1[0]=='Камень'and rand=='Бумага'):
            await message.channel.send("Бот поставил  " + rand.lower()+".")
            await message.channel.send("Вы проиграли!")
            win_bot.append(win_bot[-1]+1)
            bot_player={"Бот":win_bot[-1],
            "Игрок":win_player[-1]
            }
            await message.channel.send("Бот - "+ str(bot_player["Бот"]) +"\n")
            await message.channel.send("Игрок - "+ str(bot_player["Игрок"]) +"\n")
            print("\n\nБот - "+ str(bot_player["Бот"]) +"\n")
            print("Игрок - "+ str(bot_player["Игрок"]) +"\n")
        if(list1[0]=='Ножницы'and rand=='Камень'):
            await message.channel.send("Бот поставил  " + rand.lower()+".")
            await message.channel.send("Вы проиграли!")
            win_bot.append(win_bot[-1]+1)
            bot_player={"Бот":win_bot[-1],
            "Игрок":win_player[-1]
            }
            await message.channel.send("Бот - "+ str(bot_player["Бот"]) +"\n")
            await message.channel.send("Игрок - "+ str(bot_player["Игрок"]) +"\n")
            print("\n\nБот - "+ str(bot_player["Бот"]) +"\n")
            print("Игрок - "+ str(bot_player["Игрок"]) +"\n")
        if(list1[0]=='Камень'and rand=='Ножницы'):
            await message.channel.send("Бот поставил  " + rand.lower()+".")
            await message.channel.send("Вы победили!")
            win_player.append(win_player[-1]+1)
            bot_player={"Бот":win_bot[-1],
            "Игрок":win_player[-1]
            }
            await message.channel.send("Бот - "+ str(bot_player["Бот"]) +"\n")
            await message.channel.send("Игрок - "+ str(bot_player["Игрок"]) +"\n")
            print("\n\nБот - "+ str(bot_player["Бот"]) +"\n")
            print("Игрок - "+ str(bot_player["Игрок"]) +"\n")
        if(list1[0]=='Бумага'and rand=='Ножницы'):
            await message.channel.send("Бот поставил  " + rand.lower()+".")
            await message.channel.send("Вы проиграли!")
            win_bot.append(win_bot[-1]+1)
            bot_player={"Бот":win_bot[-1],
            "Игрок":win_player[-1]
            }
            await message.channel.send("Бот - "+ str(bot_player["Бот"]) +"\n")
            await message.channel.send("Игрок - "+ str(bot_player["Игрок"]) +"\n")
            print("\n\nБот - "+ str(bot_player["Бот"]) +"\n")
            print("Игрок - "+ str(bot_player["Игрок"]) +"\n")
        if(list1[0]=='Ножницы'and rand=='Бумага'):
            await message.channel.send("Бот поставил  " + rand.lower()+".")
            await message.channel.send("Вы победили!")
            win_player.append(win_player[-1]+1)
            bot_player={"Бот":win_bot[-1],
            "Игрок":win_player[-1]
            }
            await message.channel.send("Бот - "+ str(bot_player["Бот"]) +"\n")
            await message.channel.send("Игрок - "+ str(bot_player["Игрок"]) +"\n")
            print("\n\nБот - "+ str(bot_player["Бот"]) +"\n")
            print("Игрок - "+ str(bot_player["Игрок"]) +"\n")
# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
    if message.content.startswith('!Ножницы'):
        list1=[]
        list1.append("Ножницы")
        print(message.author.mention + "\n" + "поставил\n"+list1[0].lower()+".\n\n")
        list2=['Бумага','Камень','Ножницы']
        rand=random.choice(list2)
        if(list1[0]==rand):
            await message.channel.send("Бот поставил  " + rand.lower()+".")
            await message.channel.send("Ничья!")
            bot_player={"Бот":win_bot[-1],
            "Игрок":win_player[-1]
            }
            await message.channel.send("Бот - "+ str(bot_player["Бот"]) +"\n")
            await message.channel.send("Игрок - "+ str(bot_player["Игрок"]) +"\n")
            print("\n\nБот - "+ str(bot_player["Бот"]) +"\n")
            print("Игрок - "+ str(bot_player["Игрок"]) +"\n")
        if(list1[0]=='Бумага'and rand=='Камень'):
            await message.channel.send("Бот поставил  " + rand.lower()+".")
            await message.channel.send("Вы победили!")
            win_player.append(win_player[-1]+1)
            bot_player={"Бот":win_bot[-1],
            "Игрок":win_player[-1]
            }
            await message.channel.send("Бот - "+ str(bot_player["Бот"]) +"\n")
            await message.channel.send("Игрок - "+ str(bot_player["Игрок"]) +"\n")
            print("\n\nБот - "+ str(bot_player["Бот"]) +"\n")
            print("Игрок - "+ str(bot_player["Игрок"]) +"\n")
        if(list1[0]=='Камень'and rand=='Бумага'):
            await message.channel.send("Бот поставил  " + rand.lower()+".")
            await message.channel.send("Вы проиграли!")
            win_bot.append(win_bot[-1]+1)
            bot_player={"Бот":win_bot[-1],
            "Игрок":win_player[-1]
            }
            await message.channel.send("Бот - "+ str(bot_player["Бот"]) +"\n")
            await message.channel.send("Игрок - "+ str(bot_player["Игрок"]) +"\n")
            print("\n\nБот - "+ str(bot_player["Бот"]) +"\n")
            print("Игрок - "+ str(bot_player["Игрок"]) +"\n")
        if(list1[0]=='Ножницы'and rand=='Камень'):
            await message.channel.send("Бот поставил  " + rand.lower()+".")
            await message.channel.send("Вы проиграли!")
            win_bot.append(win_bot[-1]+1)
            bot_player={"Бот":win_bot[-1],
            "Игрок":win_player[-1]
            }
            await message.channel.send("Бот - "+ str(bot_player["Бот"]) +"\n")
            await message.channel.send("Игрок - "+ str(bot_player["Игрок"]) +"\n")
            print("\n\nБот - "+ str(bot_player["Бот"]) +"\n")
            print("Игрок - "+ str(bot_player["Игрок"]) +"\n")
        if(list1[0]=='Камень'and rand=='Ножницы'):
            await message.channel.send("Бот поставил  " + rand.lower()+".")
            await message.channel.send("Вы победили!")
            win_player.append(win_player[-1]+1)
            bot_player={"Бот":win_bot[-1],
            "Игрок":win_player[-1]
            }
            await message.channel.send("Бот - "+ str(bot_player["Бот"]) +"\n")
            await message.channel.send("Игрок - "+ str(bot_player["Игрок"]) +"\n")
            print("\n\nБот - "+ str(bot_player["Бот"]) +"\n")
            print("Игрок - "+ str(bot_player["Игрок"]) +"\n")
        if(list1[0]=='Бумага'and rand=='Ножницы'):
            await message.channel.send("Бот поставил  " + rand.lower()+".")
            await message.channel.send("Вы проиграли!")
            win_bot.append(win_bot[-1]+1)
            bot_player={"Бот":win_bot[-1],
            "Игрок":win_player[-1]
            }
            await message.channel.send("Бот - "+ str(bot_player["Бот"]) +"\n")
            await message.channel.send("Игрок - "+ str(bot_player["Игрок"]) +"\n")
            print("\n\nБот - "+ str(bot_player["Бот"]) +"\n")
            print("Игрок - "+ str(bot_player["Игрок"]) +"\n")
        if(list1[0]=='Ножницы'and rand=='Бумага'):
            await message.channel.send("Бот поставил  " + rand.lower()+".")
            await message.channel.send("Вы победили!")
            win_player.append(win_player[-1]+1)
            bot_player={"Бот":win_bot[-1],
            "Игрок":win_player[-1]
            }
            await message.channel.send("Бот - "+ str(bot_player["Бот"]) +"\n")
            await message.channel.send("Игрок - "+ str(bot_player["Игрок"]) +"\n")
            print("\n\nБот - "+ str(bot_player["Бот"]) +"\n")
            print("Игрок - "+ str(bot_player["Игрок"]) +"\n")
    if message.content.startswith('!Стоп'):
        await message.channel.send(second_comand[0]+'\n'+second_comand[1]+'\n'+second_comand[2])
# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
client.run(TOKEN)
