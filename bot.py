import requests
import discord
from typing import Optional
import json
import os
import random
import string

###### Moon02
###### Moon02
###### Moon02

predictor_name = "Your Predictor name here"
color = 0x191970

bot = discord.Bot()
token = "Discord Bot Token here"
user = "user.json"

def unrig_client(a):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(a))

def read_database():
    if os.path.exists(user):
        with open(user, "r") as file:
            return json.load(file)
    return {}

def write_database(data):
    with open(user, "w") as file:
        json.dump(data, file, indent=4)

def crashpoint(num):
    headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'x-currency': 'BLOXCOIN',
    }
    info = requests.get('https://api.bloxgame.com/games/crash', headers=headers).json()["history"][num]["crashPoint"]
    return info

@bot.command()
async def crash(ctx):
    member = ctx.author
    img_user = member.avatar
    headers = {
    'accept': 'application/json, text/plain, /',
    'accept-language': 'en-US,en;q=0.9',
    'baggage': 'sentry-environment=production,sentry-release=5546729a791bd946f85f786952871b2f3ae273b0,sentry-public_key=bc36d69d2f2352a821d2c96afe447fb6,sentry-trace_id=4a9d8f6c1751428cb4e9fd92648c45d3,sentry-replay_id=6b6042fef2d04361b5fe72eac0a6b55e,sentry-sample_rate=0.1,sentry-transaction=%2Fcrash,sentry-sampled=true',
    'if-modified-since': 'Sat, 08 Feb 2025 11:07:57 GMT',
    'origin': 'https://bloxgame.com/',
    'priority': 'u=1, i',
    'referer': 'https://bloxgame.com/',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Brave";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'sentry-trace': '4a9d8f6c1751428cb4e9fd92648c45d3-a8afca7ab614ec4d-1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'x-client-version': '1.0.0',
    'x-currency': 'BLOXCOIN',
    }

    response = requests.get('https://api.bloxgame.com/games/crash', headers=headers)
    rq = response.json()["current"]
    round_id = rq.get("_id")
    nonce = rq.get("nonce")

    last_three_crashpoints = [crashpoint(0), crashpoint(1), crashpoint(2)]
    average = sum(last_three_crashpoints) / 3
    prediction = (1 / (average - 2) / 1)
    prediction = abs(prediction)
    if 0.01 <= prediction < 1.0:
        prediction += 1
    
    riskly = prediction + (prediction / 2)
    safe = prediction - (prediction / 2)

    if 0.01 <= safe < 1.0:
        safe += 0.75
    safe = float("{:.2f}".format(safe))
    prediction = float("{:.2f}".format(prediction))
    riskly = float("{:.2f}".format(riskly))

    safe_str = f"{safe}x"
    if safe < 1:
        safe_str = f"Don't bet"

    embed = discord.Embed(
        title=f"{predictor_name}・Crash",
        description="",
        color=0x191970
    )
    prediction_info = f"> `🎯` Safe: `{safe_str}`\n"
    prediction_info += f"> `🚀` Prediction: `{prediction}x`\n"
    embed.add_field(name="`📋` **Prediction Info:**", value=prediction_info, inline=False)
    game_info = f"> `🆔` Round ID: `{round_id}`\n"
    game_info += f"> `🧁` Nonce: `{nonce}`\n"
    embed.add_field(name="`📔` **Game Info:**", value=game_info, inline=False)
    embed.set_footer(icon_url=img_user, text=f"💖・Thank you for using・{predictor_name}")
    await ctx.respond(embed=embed)

def winningColor(start, end):
    history = requests.get("https://api.bloxgame.com/games/roulette").json()["history"]
    info = [game['winningColor'] for game in history[start:end]]
    return info

###### Moon02
###### Moon02
###### Moon02
###### Moon02
###### Moon02

@bot.command()
async def slide(ctx):
    member = ctx.author
    img_user = member.avatar


    headers = {
        'sec-ch-ua-platform': '"Linux"',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
        'cookie': 'intercom-id-hggppoyd=f9cf531c-b708-4c7b-bb3b-9bef9adba3bd; intercom-device-id-hggppoyd=21574c1e-8866-41e8-aca6-5a0113a7d037; __cf_bm=Z5asac.vmVqRgMBJPiTx_4ipZhw_.f2MyAgN__1kdzM-1739123410-1.0.1.1-6sboTdQLPt79_D0lY9x17uYG3c2PD547y39O_Npxvoh9w8r5A8ofkzddk.rm8.ptGSpMRGnynsOt3bqsOs5GzA; cf_clearance=XYEfBcFrNLcQBWC8YaN6OxmxYRa_oqc9yJ3lcAxyaQM-1739123661-1.2.1.1-ybcXinGGlEgx_jf.WNhsRpITSzEpb1o2iVVIVFIA02mb_bBGuzUfppiQ6qNF0VFJKi6GncKWYSQY_FfIT2kCZ6zhfPa3hv3JOX3EOhTODn.mGJjDbokQiF4RvLd4ElTbrRK_BQAnkJia2fBQBJv4RNIHFaEjqTMYIlmEPUpQ3KCEsQItzkU7VVHTCu8Qn02anFS225KCGtsO0U3hmJOC0GI8QXXgv1MRXLFTffhv4aNNjmCmG5G9tb.mOkjdErm8gJhGk_Jnkr.afYbF8HW7Izd__Ngjbky1dgC79Gc3HC4; mp_15a3d0672e94cb1fe536417fad0996cb_mixpanel=%7B%22distinct_id%22%3A%20%224f7ff0ea-d785-466c-a81e-73fb5364d1ee%22%2C%22%24device_id%22%3A%20%22194e531f4baa1c84-0a6c8185e958d1-14462c6e-1c0980-194e531f4bba1c85%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fsearch.brave.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22search.brave.com%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%2C%22%24user_id%22%3A%20%224f7ff0ea-d785-466c-a81e-73fb5364d1ee%22%7D; intercom-session-hggppoyd=T0tqRHBQZ1NyYXJiZldENk9hbjhFU0tqc0dXR1RiUjBodGgyMC9HLzRyYzF3ekRrTWxIVDVwcElLYklLWTd0aWtpak5CL1hGcW96VEpQZ05nTUVBRElWUkFZVHViWFVwTHl2NVRQanJTbkk9LS0xVXJYM09aMXBpMjRtaDI1dWtNU1pBPT0=--66765fae1e8b2ac80ce1f7f05a7650c5639d3b52',
    }
    response = requests.get('https://api.bloxgame.com/games/roulette', headers=headers)
    rq = response.json()["current"]
    id = rq.get("_id")
    nonce = rq.get("nonce")

    past_games_amount = 10
    past_games = winningColor(-past_games_amount, None)
    bCount = past_games.count("blue")
    pCount = past_games.count("purple")
    yCount = past_games.count("yellow")
    bChance = bCount / past_games_amount * 100
    pChance = pCount / past_games_amount * 100
    yChance = yCount / past_games_amount * 100
    bChance = "{:.2f}".format(bChance)
    pChance = "{:.2f}".format(pChance)
    yChance = "{:.2f}".format(yChance)

    embed = discord.Embed(
        title=f"{predictor_name}・Slide",
        description="",
        color=color,
    )
    prediction = f"> `🔵` Prediction: `{bChance}`\n"
    prediction += f"> `🟣` Prediction: `{pChance}`\n"
    prediction += f"> `🟡` Prediction: `{yChance}`\n"
    game_info = f"> `🆔` Round ID: `{id}`\n"
    game_info += f"> `🧁` Nonce: `{nonce}`\n"
    embed.add_field(name="`📋` **Prediction Info:**", value=prediction , inline=False)
    embed.add_field(name="`📔` **Game Info:**", value=game_info, inline=False)
    embed.set_footer(icon_url=img_user, text=f"💖・Thank you for using・{predictor_name}")
    await ctx.respond(embed=embed)

@bot.command()
async def link(ctx, token: str):
    member = ctx.author
    img_user = member.avatar
    db = read_database()
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'baggage': 'sentry-environment=production,sentry-release=5546729a791bd946f85f786952871b2f3ae273b0,sentry-public_key=bc36d69d2f2352a821d2c96afe447fb6,sentry-trace_id=b4db6cff086c43c5a124835bf4dd2b45,sentry-replay_id=a6abe265cce14fbf9abe9a8dc35d4433,sentry-sample_rate=0.1,sentry-transaction=%2Fprofile,sentry-sampled=true',
    'origin': 'https://bloxgame.com',
    'priority': 'u=1, i',
    'referer': 'https://bloxgame.com/',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Brave";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'sentry-trace': 'b4db6cff086c43c5a124835bf4dd2b45-990ba4c78950bd80-1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'x-auth-token': token,
    'x-client-version': '1.0.0',
    'x-currency': 'BLOXCOIN',
    'x-timezone': 'Europe/Athens',
    }
    response = requests.get('https://api.bloxgame.com/user', headers=headers)
    rq = response.json()
    invaild_tk = rq.get("success")
    if invaild_tk == False:
        Hasik = discord.Embed(
            title="Invaild Token",
            description="Invaild Bloxgame Token",
            color=discord.Color.brand_red(),
        )
        await ctx.respond(embed=Hasik, ephemeral=True)
        return
    user = rq.get("user").get("username")
    wallet = rq.get("user").get("wallet")
    _id = rq.get("user").get("_id")
    db[member.name] = {
        "x-auth-token": token,
        "username": user,
        "wallet": wallet,
    }
    write_database(db)
    embed = discord.Embed(
        title=f"Successfully linked・`{predictor_name}`",
        description="",
        color=color,
    )
    link = f"> `🪪` Username: **`{user}`**\n"
    link += f"> `🏧` Balance: `{wallet}`\n"
    link += f"> `🆔` ID: `{_id}`\n"
    embed.add_field(name="`📊` Status:", value=link, inline=False)
    embed.set_footer(icon_url=img_user, text=f"💖・Thank you for using・{predictor_name}")
    await ctx.respond(embed=embed, ephemeral=True)

@bot.command()
async def account(ctx):
    member = ctx.author
    name = member.name
    img_user = member.avatar
    db = read_database()
    
    if name not in db:
        not_linked = discord.Embed(
            title=f"You are not linked to `{predictor_name}`",
            description="",
            color=discord.Color.blurple(),
        )
        await ctx.respond(embed=not_linked)
        return
    
    if name in db:
        data = db[name]

    token = data["x-auth-token"]

    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'baggage': 'sentry-environment=production,sentry-release=5546729a791bd946f85f786952871b2f3ae273b0,sentry-public_key=bc36d69d2f2352a821d2c96afe447fb6,sentry-trace_id=b4db6cff086c43c5a124835bf4dd2b45,sentry-replay_id=a6abe265cce14fbf9abe9a8dc35d4433,sentry-sample_rate=0.1,sentry-transaction=%2Fprofile,sentry-sampled=true',
    'origin': 'https://bloxgame.com',
    'priority': 'u=1, i',
    'referer': 'https://bloxgame.com/',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Brave";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'sentry-trace': 'b4db6cff086c43c5a124835bf4dd2b45-990ba4c78950bd80-1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'x-auth-token': token,
    'x-client-version': '1.0.0',
    'x-currency': 'BLOXCOIN',
    'x-timezone': 'Europe/Athens',
    }
    response = requests.get('https://api.bloxgame.com/user', headers=headers)
    rq = response.json()
    user = rq.get("user").get("username")
    wallet = rq.get("user").get("wallet")
    _id = rq.get("user").get("_id")
    totalDeposited = rq.get("user").get("totalDeposited")
    totalWithdrawn = rq.get("user").get("totalWithdrawn")
    embed = discord.Embed(
        title="Account information",
        description="",
        color=color,
    )

    account_info = f"> `🪪` Username: **`{user}`**\n"
    account_info += f"> `🏧` Balance: `{wallet}`\n"
    account_info += f"> `🧁` Total Deposited: `{totalDeposited}`\n"
    account_info += f"> `🍰` Total Withdrawn: `{totalWithdrawn}`\n"
    account_info += f"> `🆔` ID: `{_id}`\n"
    embed.add_field(name="`👤` Profile:", value=account_info, inline=False)
    embed.set_footer(icon_url=img_user, text=f"💖・Thank you for using・{predictor_name}")
    await ctx.respond(embed=embed, ephemeral=True)

###### Moon02
###### Moon02
###### Moon02
###### Moon02

@bot.command(description="Unring")
async def unrig(ctx):
    db = read_database()
    member = ctx.author
    name = member.name

    if name not in db:
        not_linked = discord.Embed(
            title=f"You are not linked to `{predictor_name}`",
            description="",
            color=discord.Color.blurple(),
        )
        await ctx.respond(embed=not_linked)
        return
    
    if name in db:
        data = db[name]

    unrig_token = data["x-auth-token"] 
    provably_fair = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'baggage': 'sentry-environment=production,sentry-release=5546729a791bd946f85f786952871b2f3ae273b0,sentry-public_key=bc36d69d2f2352a821d2c96afe447fb6,sentry-trace_id=ae454ad540dd4105b7a2ecf63c6cc3b8,sentry-replay_id=8eadd3db5c8b40b0903b814ccf27323a,sentry-sample_rate=0.1,sentry-transaction=%2Fcrash,sentry-sampled=false',
    'origin': 'https://bloxgame.com',
    'priority': 'u=1, i',
    'referer': 'https://bloxgame.com/',
    'sec-ch-ua-platform': '"Linux"',
    'sentry-trace': 'ae454ad540dd4105b7a2ecf63c6cc3b8-821847c86cb772be-0',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'x-auth-token': unrig_token,
    'x-client-version': '1.0.0',
    'x-currency': 'BLOXCOIN',
    'x-timezone': 'Europe/Athens',
    'x-visitor-id': 'e34f76f9e85caa429f9de2749b472926',
    }
    provably_data = requests.get('https://api.bloxgame.com/provably-fair', headers=provably_fair)
    rq1 = provably_data.json()
    clientSeed1 = rq1.get("clientSeed")
    nonce = rq1.get("nonce")
    unrigged = unrig_client(24)
    Unringer = f"{predictor_name}-{unrigged}"
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'baggage': 'sentry-environment=production,sentry-release=5546729a791bd946f85f786952871b2f3ae273b0,sentry-public_key=bc36d69d2f2352a821d2c96afe447fb6,sentry-trace_id=ae454ad540dd4105b7a2ecf63c6cc3b8,sentry-replay_id=8eadd3db5c8b40b0903b814ccf27323a,sentry-sample_rate=0.1,sentry-transaction=%2Fcrash,sentry-sampled=false',
    'content-type': 'application/json',
    'origin': 'https://bloxgame.com',
    'priority': 'u=1, i',
    'referer': 'https://bloxgame.com/',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sentry-trace': 'ae454ad540dd4105b7a2ecf63c6cc3b8-821847c86cb772be-0',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'x-auth-token': unrig_token,
    'x-client-version': '1.0.0',
    'x-currency': 'BLOXCOIN',
    'x-timezone': 'Europe/Athens',
    'x-visitor-id': 'e34f76f9e85caa429f9de2749b472926',
    }

    json_data = {
        'clientSeed': Unringer,
    }
    unring = requests.post('https://api.bloxgame.com/provably-fair/clientSeed', headers=headers, json=json_data)
    unring
    embed = discord.Embed(
        title=f"{predictor_name}・Unrigged your account.",
        description="",
        color=color,
    )
    embed.add_field(name="`🆔` New ClientSeed", value=f"```{Unringer}```", inline=False)
    embed.add_field(name="`📔` Old ClientSeed", value=f"```{clientSeed1}```", inline=False)
    embed.add_field(name="`🔢` Nonce", value=f"```{nonce}```", inline=False)
    await ctx.respond(embed=embed)

###### Moon02
###### Moon02
###### Moon02
###### Moon02

@bot.command()
async def mines(ctx, tiles: Optional[int] = 4):
    db = read_database()
    member = ctx.author
    name = member.name
    img_user = member.avatar

    if name not in db:
        no_db = discord.Embed(
            title=f"Not Linked To `{predictor_name}`",
            description="",
            color=discord.Color.dark_theme(),
        )
        await ctx.respond(embed=no_db)
        return

    if name in db:
        data = db[name]

    bloxgame_token = data["x-auth-token"]

    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'baggage': 'sentry-environment=production,sentry-release=5546729a791bd946f85f786952871b2f3ae273b0,sentry-public_key=bc36d69d2f2352a821d2c96afe447fb6,sentry-trace_id=ae454ad540dd4105b7a2ecf63c6cc3b8,sentry-replay_id=8eadd3db5c8b40b0903b814ccf27323a,sentry-sample_rate=0.1,sentry-transaction=%2Fcrash,sentry-sampled=false',
    'content-type': 'application/json',
    'origin': 'https://bloxgame.com',
    'priority': 'u=1, i',
    'referer': 'https://bloxgame.com/',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sentry-trace': 'ae454ad540dd4105b7a2ecf63c6cc3b8-821847c86cb772be-0',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'x-auth-token': bloxgame_token,
    'x-client-version': '1.0.0',
    'x-currency': 'BLOXCOIN',
    'x-timezone': 'Europe/Athens',
    'x-visitor-id': 'e34f76f9e85caa429f9de2749b472926',
    }
    rq = requests.get("http://api.bloxgame.com/games/mines", headers=headers)
    data = rq.json()
    hasgame = data.get("hasGame")
    if hasgame == False:
        no_hashgame = discord.Embed(
            title="No active games at the moment",
            description="You must start a game to predict Mines",
            color=discord.Color.dark_theme()
        )
        await ctx.respond(embed=no_hashgame)
        return
    
    safe = "🧁"
    nigger = "❌"
    mines_amount = data["game"]["minesAmount"]
    betAmount = data["game"]["betAmount"]
    uuid = data["game"]["uuid"]
    _id = data["game"]["_id"]["$oid"]
    nonce = data["game"]["nonce"]
    if mines_amount > 11:
        mines = discord.Embed(
            title="Invalid mines amount",
            description="doesn't predict for games over 11 bombs",
            color=discord.Color.dark_theme(),
        )
        await ctx.respond(embed=mines)
        return
    
    history = requests.get("https://api.bloxgame.com/games/mines/history", headers=headers, params={'size': 5, 'page': 0})
    history_data = history.json()["data"]

    last_games = history_data
    mines_check = any(game["minesAmount"] > 11 for game in last_games)

    if mines_check:
        embed = discord.Embed(
                title='Invalid mines amount',
                description=f"doesn't predict for games over 11 bombs",
                color=discord.Color.dark_theme)
        await ctx.respond(embed=embed)
        return
    
    safe_spot_amount = 25 - mines_amount
    if tiles > safe_spot_amount:
        tiles = safe_spot_amount

    cell_counts = [0] * 25
    for game in history_data:
        mines = game["mineLocations"]
        for mine in mines:
            cell_counts[mine] += 1

    top_spots = sorted(range(len(cell_counts)), key=lambda i: cell_counts[i], reverse=True)[:tiles]
    prediction = [[nigger for _ in range(5)] for _ in range(5)]
    for i in top_spots:
        prediction[i // 5][i % 5] = safe

    prediction = [row[::-1] for row in prediction]
    grid = "\n".join("".join(row) for row in prediction)

    embed = discord.Embed(
        title=f"{predictor_name} V1",
        description="",
        color=color,
    )
    embed.add_field(name="`💎` Predictions", value=f"```{grid}```", inline=False)
    embed.add_field(name="`💸` Bet Amount", value=f"```{betAmount}```", inline=False)
    embed.add_field(name="`💣` Mines Amount", value=f"```{mines_amount}```", inline=False)
    embed.add_field(name="`🆔` Round ID", value=f"```{uuid}```", inline=False)
    embed.add_field(name="`🔢` Nonce", value=f"```{nonce}```", inline=False)
    embed.set_footer(icon_url=img_user, text=f"💖・Thank you for using・{predictor_name}")
    await ctx.respond(embed=embed)

@bot.command()
async def credits(ctx):
    embed = discord.Embed(
        title="",
        description="",
        color=color,
    )
    rule1 = "> Harado It's __**open source**__ Bloxgame Predictor\n"
    rule1 += "> Programmed By `Moon02` & `Coxy.57`\n"
    rule1 += "> OFFICAL SERVER: ```discord.gg/rAmRRtZbEJ```"
    embed.add_field(name="` 1 ` **Credit's Goes to Harado**", value=rule1, inline=False)
    await ctx.respond(embed=embed)

bot.run(token)
