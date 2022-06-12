import discum
import random
import time
import os

print("Enter your token: \n(if you don't know how to have your token, follow the instructions in this video: https://www.youtube.com/watch?v=SK9k9Zp-Gq8)\n")
Token = input(">")

os.system("cls" or "clear")

bot = discum.Client(token=Token, log=False)

members = []
guilds = input("Guild ID: ")
channel = input("Channel ID  (in the same guild)")

print("Please input your message: ")

msgs = ""
while True:
    msg = input("Continue the message or press enter: ")
    if msg:
        msgs += msg + "\n"
    else:
        break
text = '\n'.join(msgs)

i_time = input("DMs interval in seconds (min: 0): ")

bl_guy = []
while True:
    msg = input("Enter a blacklisted ID or press enter to pass: ")
    if msg:
        bl_guy.append((msg))
    else:
        break

@bot.gateway.command
def memberTest(resp):
    if resp.event.ready_supplemental:
        bot.gateway.fetchMembers(guilds, channel)
    if bot.gateway.finishedMemberFetching(guilds):
        bot.gateway.removeCommand(memberTest)
        bot.gateway.close()
bot.gateway.run()
print("Searching all members")
for memberID in bot.gateway.session.guild(guilds).members:
    members.append(memberID)
print("Starting to DM.")
for memb_id in members:
    if memb_id not in bl_guy:
        try:
            anti_rate_limit = random.randint(0,20)
            if anti_rate_limit == 20:
                print(f'Sleeping for 45 seconds to prevent rate-limiting.')
                time.sleep(45)
                print(f'Done sleeping!')
            print(f"Preparing to DM {memb_id}.")
            time.sleep(int(i_time))
            newDM = bot.createDM([f"{memb_id}"]).json()["id"]
            bot.sendMessage(newDM, f"{msgs}")
            print(f'{memb_id} got dmed | {msgs}.')
        except Exception as E:
            print(E)
            print(f'Couldn\'t DM {memb_id}.')
    else:
        print("A blacklisted guy got skipped !")


    