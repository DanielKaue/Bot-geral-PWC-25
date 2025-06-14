import discord
from discord.ext import commands
import os
from keep_alive import keep_alive
from flask import Flask
from threading import Thread
import random
import re
import asyncio


cargo_mod1 = 1382505875549323349
cargo_mod2 = 1382838597790470337
cargo_geral = 1382505875549323346
role_inscrito_name = "Inscrito"

app = Flask('')


@app.route('/')
def home():
    return "Bot está online!"


def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()


intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Bot {bot.user} está online!")


@bot.command()
@commands.has_permissions(manage_messages=True)
async def chat(ctx, amount: int):
    """Apaga uma quantidade de mensagens no canal."""
    if amount < 1:
        await ctx.send("Digite um número maior que 0.")
        return
    deleted = await ctx.channel.purge(limit=amount + 1
                                      )  # +1 para apagar o comando também
    await ctx.send(f"{len(deleted)-1} mensagens apagadas.", delete_after=5)


@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    """Desliga o bot com segurança."""
    await ctx.send("Desligando o bot... Até mais!")
    await bot.close()


@bot.event
async def on_member_join(member):
    canal = bot.get_channel(1382838621782151348)
    if canal:
        await canal.send(
            f"👋 {member.mention} entrou no servidor! Seja bem-vindo(a)!")


@bot.event
async def on_member_remove(member):
    canal = bot.get_channel(1382838622692311171)
    if canal:
        await canal.send(f"😢 {member.name} saiu do servidor. Até logo!")

    @bot.command()
    @commands.is_owner()
    async def shutdown(ctx):
        """Desliga o bot com segurança."""
        await ctx.send("Desligando o bot... Até mais!")
        await bot.close()


@bot.command()
@commands.has_permissions(administrator=True)
async def remove(ctx):
    """Remove categorias, canais e cargos criados pelo bot."""
    guild = ctx.guild

    await ctx.send("🗑️ Removendo estrutura do servidor...")

    # Lista de nomes de cargos que o setup cria
    cargos_nominais = [
        "Membros",
        "Suporte",
    ]
    # Adicione aqui também os cargos de país, no mesmo formato do setup
    paises = [
        "Uruguai", "Alemanha", "Brasil", "Argentina", "França", "Inglaterra",
        "Portugal", "Holanda", "Espanha", "Japão", "Senegal", "EUA", "Polônia",
        "Austrália", "Croácia", "Marrocos"
    ]
    for pais in paises:
        cargos_nominais.append(f"🌍 {pais}")

    # Deleta cargos
    for role in guild.roles:
        if role.name in cargos_nominais:
            try:
                await role.delete()
            except:
                pass

    # Lista de categorias que o setup cria
    categorias_nominais = [
        "⟬🏠⟭ Recepção",
        "⟬📚⟭ Instrução",
        "⟬💬⟭ Geral",
        "⟬🎧⟭ Chamadas",
        "⟬🛠⟭ Suporte",
    ]
    for pais in paises:
        categorias_nominais.append(f"🌍 {pais}")

    # Deleta canais e categorias
    for category in guild.categories:
        if category.name in categorias_nominais:
            # deleta todos os canais dentro
            for ch in category.channels:
                try:
                    await ch.delete()
                except:
                    pass
            # deleta a própria categoria
            try:
                await category.delete()
            except:
                pass

    await ctx.send("✅ Estrutura removida com sucesso!")


@bot.command()
@commands.has_permissions(administrator=True)
async def deletar(ctx):
    """Remove categorias, canais e cargos criados pelo bot."""
    guild = ctx.guild

    await ctx.send("🗑️ Removendo estrutura do servidor...")

    # Lista de nomes de cargos que o setup cria
    cargos_nominais = [
        "Membros",
        "Suporte",
    ]
    # Adicione aqui também os cargos de país, no mesmo formato do setup
    paises = [
        "Uruguai", "Alemanha", "Brasil", "Argentina", "França", "Inglaterra",
        "Portugal", "Holanda", "Espanha", "Japão", "Senegal", "EUA", "Polônia",
        "Austrália", "Croácia", "Marrocos"
    ]
    for pais in paises:
        cargos_nominais.append(f"🌍 {pais}")

    # Deleta cargos
    for role in guild.roles:
        if role.name in cargos_nominais:
            try:
                await role.delete()
            except:
                pass

    # Lista de categorias que o setup cria
    categorias_nominais = [
        "⟬🏠⟭ Recepção",
        "⟬📚⟭ Instrução",
        "⟬💬⟭ Geral",
        "⟬🎧⟭ Chamadas",
        "⟬🛠⟭ Suporte",
    ]
    for pais in paises:
        categorias_nominais.append(f"🌍 {pais}")

    # Deleta canais e categorias
    for category in guild.categories:
        if category.name in categorias_nominais:
            # deleta todos os canais dentro
            for ch in category.channels:
                try:
                    await ch.delete()
                except:
                    pass
            # deleta a própria categoria
            try:
                await category.delete()
            except:
                pass

    await ctx.send("✅ Estrutura removida com sucesso!")


@bot.command()
async def criarserver(ctx):
    guild = ctx.guild

    await ctx.send("Criando estrutura do servidor...")

    cargos = {
        "Membros": discord.Permissions(permissions=0),
        "Suporte": discord.Permissions(administrator=True)
    }

    for nome, perm in cargos.items():
        await guild.create_role(name=nome, permissions=perm, mentionable=True)

    categorias = {
        "⟬🏠⟭ Recepção": ["⟬📢⟭ convocados", "⟬📢⟭ eliminados"],
        "⟬📚⟭ Instrução": [
            "⟬📘⟭ tipos", "⟬📘⟭ chaveamento", "⟬📘⟭ mods", "⟬📘⟭ ip-e-porta",
            "⟬📘⟭ regras"
        ],
        "⟬💬⟭ Geral": [
            "⟬🗣⟭ chat-geral", "⟬🔍⟭ poketwo", "⟬🤣⟭ memes", "⟬🖼⟭ imagens",
            "⟬📢⟭ divulgação"
        ],
        "⟬🎧⟭ Chamadas": [
            "⟬🔊⟭ Call 1", "⟬🔊⟭ Call 2", "⟬🔊⟭ Call 3", "⟬🏰⟭ Castelo",
            "⟬🎙️⟭ Gravando 1", "⟬🎙️⟭ Gravando 2", "⟬🎙️⟭ Gravando 3",
            "⟬🎙️⟭ Gravando 4"
        ],
        "⟬🛠⟭ Suporte": ["⟬🎫⟭ ticket", "⟬🚨⟭ denúncias", "⟬💡⟭ sugestões"]
    }

    for cat_nome, canais in categorias.items():
        categoria = await guild.create_category(cat_nome)
        for canal_nome in canais:
            if "Call" in canal_nome or "Castelo" in canal_nome or "Gravando" in canal_nome:
                user_limit = 5 if "Call" in canal_nome else 99 if "Castelo" in canal_nome else 4
                await guild.create_voice_channel(canal_nome,
                                                 category=categoria,
                                                 user_limit=user_limit)
            else:
                await guild.create_text_channel(canal_nome, category=categoria)

    await ctx.send("✅ Estrutura criada com sucesso!")


def has_any_role(user_roles, role_ids):
    return any(role.id in role_ids for role in user_roles)

@bot.command()
async def pix(ctx):
    guild = ctx.guild
    role_inscrito = discord.utils.get(guild.roles, name=role_inscrito_name)
    user_roles = ctx.author.roles

    # Verifica se tem cargo geral ou inscrito
    allowed_roles = [cargo_geral]
    if role_inscrito:
        allowed_roles.append(role_inscrito.id)

    if not has_any_role(user_roles, allowed_roles):
        await ctx.send(f"{ctx.author.mention}, você precisa estar com o cargo **{role_inscrito_name}** ou ser membro para usar esse comando.")
        return

    embed = discord.Embed(
        title="PIX - Taxa de Inscrição",
        description="O PIX para taxa de inscrição é:\n`000.000.000-00` (substitua pelo correto)",
        color=discord.Color.green()
    )
    await ctx.send(embed=embed)

@bot.command()
async def inscrito(ctx):
    user_roles = ctx.author.roles
    mod_roles = [cargo_mod1, cargo_mod2]

    # Só moderação pode usar
    if not has_any_role(user_roles, mod_roles):
        await ctx.send(f"{ctx.author.mention}, você não tem permissão para usar esse comando.")
        return

    guild = ctx.guild
    role = discord.utils.get(guild.roles, name=role_inscrito_name)

    # Cria o cargo se não existir
    if not role:
        role = await guild.create_role(name=role_inscrito_name, mentionable=True)
        await ctx.send(f"Cargo **{role_inscrito_name}** criado com sucesso!")

    # Adiciona cargo aos usuários mencionados
    if len(ctx.message.mentions) == 0:
        await ctx.send(f"Use `{bot.command_prefix}inscrito @usuário` para adicionar o cargo a alguém.")
        return

    for member in ctx.message.mentions:
        if role not in member.roles:
            await member.add_roles(role)
            await ctx.send(f"Cargo **{role_inscrito_name}** adicionado para {member.mention}!")
        else:
            await ctx.send(f"{member.mention} já possui o cargo **{role_inscrito_name}**.")


# Comando !ping
@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)  # em ms
    await ctx.send(f"🏓 Pong! Latência: {latency}ms")


# Comando !userinfo
@bot.command()
async def userinfo(ctx, member: discord.Member = None):
    member = member or ctx.author
    embed = discord.Embed(title=f"Informações de {member}",
                          color=discord.Color.blue())
    embed.set_thumbnail(
        url=member.avatar.url if member.avatar else member.default_avatar.url)
    embed.add_field(name="ID", value=member.id)
    embed.add_field(name="Nome", value=str(member))
    embed.add_field(name="Conta criada em",
                    value=member.created_at.strftime("%d/%m/%Y %H:%M"))
    embed.add_field(name="Entrou no servidor em",
                    value=member.joined_at.strftime("%d/%m/%Y %H:%M")
                    if member.joined_at else "Desconhecido")
    embed.add_field(
        name="Cargos",
        value=", ".join(
            [c.mention for c in member.roles if c != ctx.guild.default_role])
        or "Nenhum")
    embed.set_footer(
        text=f"Pedido por {ctx.author}",
        icon_url=ctx.author.avatar.url if ctx.author.avatar else None)
    await ctx.send(embed=embed)


# Comando !avatar
@bot.command()
async def avatar(ctx, member: discord.Member = None):
    member = member or ctx.author
    avatar_url = member.avatar.url if member.avatar else member.default_avatar.url
    embed = discord.Embed(title=f"Avatar de {member}",
                          color=discord.Color.purple())
    embed.set_image(url=avatar_url)
    await ctx.send(embed=embed)


# Comando !roll (rola um dado)
@bot.command()
async def roll(ctx, lados: int = 6):
    if lados < 2:
        await ctx.send("O dado precisa ter pelo menos 2 lados.")
        return
    resultado = random.randint(1, lados)
    await ctx.send(
        f"🎲 {ctx.author.mention} rolou um dado de {lados} lados e tirou: **{resultado}**"
    )


# Comando !serverinfo
@bot.command()
async def serverinfo(ctx):
    guild = ctx.guild
    embed = discord.Embed(title=f"Informações do servidor: {guild.name}",
                          color=discord.Color.gold())
    embed.set_thumbnail(url=guild.icon.url if guild.icon else None)
    embed.add_field(name="ID", value=guild.id)
    embed.add_field(name="Região", value=str(guild.region))
    embed.add_field(name="Criado em",
                    value=guild.created_at.strftime("%d/%m/%Y %H:%M"))
    embed.add_field(name="Dono", value=str(guild.owner))
    embed.add_field(name="Membros", value=guild.member_count)
    embed.add_field(name="Canais", value=len(guild.channels))
    embed.add_field(name="Cargos", value=len(guild.roles))
    await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(administrator=True)
async def mutecargo(ctx):
    guild = ctx.guild
    existing_role = discord.utils.get(guild.roles, name="Mutado")
    if existing_role:
        await ctx.send("O cargo 'Mutado' já existe neste servidor.")
        return

    # Cria o cargo Mutado
    mute_role = await guild.create_role(name="Mutado",
                                        reason="Cargo de mute criado pelo bot")

    # Ajusta as permissões em todos os canais
    for channel in guild.channels:
        if isinstance(channel, discord.TextChannel):
            await channel.set_permissions(mute_role,
                                          send_messages=False,
                                          add_reactions=False)
        elif isinstance(channel, discord.VoiceChannel):
            await channel.set_permissions(mute_role,
                                          speak=False,
                                          connect=False)

    await ctx.send(
        "Cargo 'Mutado' criado e permissões configuradas com sucesso!")


PAISES = [
    ("Brasil", "🇧🇷", None),
    ("França", "🇫🇷", None),
    ("Argentina", "🇦🇷", None),
    ("Inglaterra", "🏴", None),
    ("Holanda", "🇳🇱", None),
    ("Croácia", "🇭🇷", None),
    ("Marrocos", "🇲🇦", None),
    ("Portugal", "🇵🇹", None),
    ("Japão", "🇯🇵", None),
    ("Uruguai", "🇺🇾", 1382838598948360192),  # <- ID fixo
    ("Alemanha", "🇩🇪", None),
    ("Senegal", "🇸🇳", None),
    ("Austrália", "🇦🇺", None),
    ("Polônia", "🇵🇱", None),
    ("Espanha", "🇪🇸", None),
    ("Estados Unidos", "🇺🇸", None)
]

PAISES = [
    ("Brasil", "🇧🇷"),
    ("Argentina", "🇦🇷"),
    ("Alemanha", "🇩🇪"),
    ("França", "🇫🇷"),
    ("Uruguai", "🇺🇾"),
    ("Japão", "🇯🇵"),
    ("Espanha", "🇪🇸"),
    ("Portugal", "🇵🇹"),
    ("Holanda", "🇳🇱"),
    ("Inglaterra", "🏴"),
    ("Polônia", "🇵🇱"),
    ("Croácia", "🇭🇷"),
    ("Senegal", "🇸🇳"),
    ("Marrocos", "🇲🇦"),
    ("Austrália", "🇦🇺"),
    ("EUA", "🇺🇸"),
]


def gerar_todas_partidas(paises):
    partidas = []
    for i in range(len(paises)):
        for j in range(i + 1, len(paises)):
            partidas.append((paises[i], paises[j]))
    return partidas


def sortear_rodada(partidas_disponiveis, max_jogos):
    rodada = []
    times_usados = set()
    partidas_candidatas = partidas_disponiveis[:]
    random.shuffle(partidas_candidatas)

    for partida in partidas_candidatas:
        p1, p2 = partida
        pais1, _ = p1
        pais2, _ = p2

        # Garante que os times dessa partida ainda não jogaram na rodada
        if pais1 in times_usados or pais2 in times_usados:
            continue

        rodada.append(partida)
        times_usados.add(pais1)
        times_usados.add(pais2)

        if len(rodada) == max_jogos:
            break

    return rodada


def remover_partidas_usadas(partidas, partidas_usadas):
    return [p for p in partidas if p not in partidas_usadas]


@bot.command()
async def fdg(ctx):
    todas_partidas = gerar_todas_partidas(PAISES)
    max_jogos_por_rodada = len(
        PAISES) // 2  # 8 jogos por rodada para 16 países

    rodadas = []
    partidas_disponiveis = todas_partidas[:]

    for rodada_num in range(6):  # 6 rodadas da fase de grupos
        rodada_atual = sortear_rodada(partidas_disponiveis,
                                      max_jogos_por_rodada)

        # Se não teve jogos suficientes, para evitar rodadas vazias, quebra o loop
        if not rodada_atual:
            break

        rodadas.append(rodada_atual)
        partidas_disponiveis = remover_partidas_usadas(partidas_disponiveis,
                                                       rodada_atual)

    embed = discord.Embed(title="🗓️ Fase de Grupos - 6 Rodadas",
                          color=discord.Color.blue())

    def formatar_jogo(jogo):
        (pais1, emoji1), (pais2, emoji2) = jogo
        return f"{emoji1} **{pais1}**  x  {emoji2} **{pais2}**"

    for i, rodada in enumerate(rodadas, start=1):
        texto_rodada = "\n".join(formatar_jogo(j) for j in rodada)
        embed.add_field(name=f"Rodada {i}",
                        value=texto_rodada or "Nenhum jogo",
                        inline=False)

    await ctx.send(embed=embed)


trocas = {}  # Armazena quantas vezes cada user trocou de país


@bot.command(name="paises")
async def paises(ctx):
    embed = discord.Embed(
        title="🌍 Selecione seu país!",
        description=(
            "Clique no emoji correspondente ao seu país para receber o cargo.\n"
            "Clique novamente para remover.\n\n"
            "**⚠️ Você só pode trocar de país 3 vezes.**"
        ),
        color=discord.Color.blue())

    mensagem = ""
    emojis_map = {}
    for nome, emoji in PAISES:
        cargo_nome = f"🌍 {emoji} {nome}"
        mensagem += f"{emoji} - {nome}\n"
        emojis_map[emoji] = cargo_nome

    embed.add_field(name="Países disponíveis", value=mensagem, inline=False)
    msg = await ctx.send(embed=embed)

    for emoji in emojis_map:
        await msg.add_reaction(emoji)

    bot.reacao_paises_msg_id = msg.id
    bot.reacao_paises_map = emojis_map

@bot.event
async def on_raw_reaction_add(payload):
    if payload.message_id != getattr(bot, "reacao_paises_msg_id", None):
        return
    if payload.user_id == bot.user.id:
        return

    guild = bot.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)
    if not guild or not member:
        return

    emoji = str(payload.emoji)
    cargo_nome = bot.reacao_paises_map.get(emoji)
    if not cargo_nome:
        return

    channel = bot.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)

    # Verifica se país está lotado
    if emoji == "🇺🇾":
        role = guild.get_role(1382838598948360192)
    else:
        role = discord.utils.get(guild.roles, name=cargo_nome)

    if role and len(role.members) >= 4:
        await message.remove_reaction(emoji, member)
        try:
            await member.send("⚠️ País lotado, escolha outro!")
        except:
            pass
        return

    # Verifica se usuário já tem outro país
    cargos_paises = [
        discord.utils.get(guild.roles, name=nome)
        for nome in bot.reacao_paises_map.values()
    ]
    cargos_atuais = [r for r in cargos_paises if r and r in member.roles]

    user_id = member.id
    trocas.setdefault(user_id, 0)

    if len(cargos_atuais) >= 1:
        if trocas[user_id] >= 3:
            await message.remove_reaction(emoji, member)
            try:
                await member.send("❌ Você já atingiu o limite de 3 trocas de país.")
            except:
                pass
            return

        # Remove o país anterior
        for outro_cargo in cargos_atuais:
            await member.remove_roles(outro_cargo)
            for e, nome_c in bot.reacao_paises_map.items():
                if nome_c == outro_cargo.name:
                    await message.remove_reaction(e, member)

        trocas[user_id] += 1
        restantes = 3 - trocas[user_id]

        try:
            await member.send(f"🔁 Você trocou de país. Você ainda pode trocar **{restantes}** vez(es).")
        except:
            pass

    # Adiciona novo cargo
    if role and role not in member.roles:
        await member.add_roles(role)


# Função para pegar ou criar canal de logs
async def get_or_create_modlog_channel(guild):
    modlog = discord.utils.get(guild.text_channels, name="mod-logs")
    if modlog is None:
        overwrites = {
            guild.default_role:
            discord.PermissionOverwrite(read_messages=False),
            guild.me: discord.PermissionOverwrite(read_messages=True)
        }
        modlog = await guild.create_text_channel("mod-logs",
                                                 overwrites=overwrites)
    return modlog


@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')


# BAN
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    try:
        await member.ban(reason=reason)
        await ctx.send(
            f"{member.mention} foi banido do servidor. Motivo: {reason}")
        modlog = await get_or_create_modlog_channel(ctx.guild)
        await modlog.send(
            f"🔨 **BAN** | {member} ({member.id}) foi banido por {ctx.author}. Motivo: {reason}"
        )
    except Exception as e:
        await ctx.send(f"Não foi possível banir {member.mention}. Erro: {e}")


# KICK
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    try:
        await member.kick(reason=reason)
        await ctx.send(
            f"{member.mention} foi expulso do servidor. Motivo: {reason}")
        modlog = await get_or_create_modlog_channel(ctx.guild)
        await modlog.send(
            f"👢 **KICK** | {member} ({member.id}) foi expulso por {ctx.author}. Motivo: {reason}"
        )
    except Exception as e:
        await ctx.send(f"Não foi possível expulsar {member.mention}. Erro: {e}"
                       )


# MUTE
def parse_time(time_str):
    # aceita formatos: 10m, 2h, 1d (minutos, horas, dias)
    match = re.match(r"(\d+)([mhd])", time_str.lower())
    if not match:
        return None
    num, unit = match.groups()
    num = int(num)
    if unit == "m":
        return num * 60
    elif unit == "h":
        return num * 3600
    elif unit == "d":
        return num * 86400
    return None


@bot.command()
@commands.has_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member, time: str = None, *, reason=None):
    guild = ctx.guild
    mute_role = discord.utils.get(guild.roles, name="Mutado")
    if not mute_role:
        await ctx.send(
            "Cargo 'Mutado' não encontrado. Crie um cargo chamado 'Mutado' com permissão para silenciar."
        )
        return

    try:
        await member.add_roles(mute_role, reason=reason)
        await ctx.send(
            f"{member.mention} foi mutado. Motivo: {reason} Tempo: {time if time else 'indefinido'}"
        )
        modlog = await get_or_create_modlog_channel(guild)
        await modlog.send(
            f"🤐 **MUTE** | {member} ({member.id}) foi mutado por {ctx.author}. Motivo: {reason} Tempo: {time if time else 'indefinido'}"
        )

        if time:
            seconds = parse_time(time)
            if seconds is None:
                await ctx.send(
                    "Formato de tempo inválido! Use exemplos: 10m, 2h, 1d")
                return
            await asyncio.sleep(seconds)
            # Confere se o membro ainda está no servidor e se está mutado antes de remover
            member = guild.get_member(member.id)
            if member and mute_role in member.roles:
                await member.remove_roles(mute_role,
                                          reason="Tempo de mute expirado")
                await ctx.send(
                    f"{member.mention} foi desmutado automaticamente após {time}."
                )
                await modlog.send(
                    f"🔈 **UNMUTE** automático | {member} ({member.id}) após {time}."
                )
    except Exception as e:
        await ctx.send(f"Não foi possível mutar {member.mention}. Erro: {e}")


# UNMUTE
@bot.command()
@commands.has_permissions(manage_roles=True)
async def unmute(ctx, member: discord.Member):
    guild = ctx.guild
    mute_role = discord.utils.get(guild.roles, name="Mutado")
    if not mute_role:
        await ctx.send("Cargo 'Mutado' não encontrado.")
        return

    try:
        if mute_role in member.roles:
            await member.remove_roles(mute_role)
            await ctx.send(f"{member.mention} foi desmutado.")
            modlog = await get_or_create_modlog_channel(guild)
            await modlog.send(
                f"🔈 **UNMUTE** | {member} ({member.id}) desmutado por {ctx.author}."
            )
        else:
            await ctx.send(f"{member.mention} não está mutado.")
    except Exception as e:
        await ctx.send(f"Não foi possível desmutar {member.mention}. Erro: {e}"
                       )


# WARN
@bot.command()
@commands.has_permissions(manage_messages=True)
async def warn(ctx, member: discord.Member, *, reason=None):
    if reason is None:
        reason = "Não especificado"
    guild_id = ctx.guild.id
    user_id = member.id

    if guild_id not in warns:
        warns[guild_id] = {}
    if user_id not in warns[guild_id]:
        warns[guild_id][user_id] = []
    warns[guild_id][user_id].append({
        "moderator": ctx.author.id,
        "reason": reason
    })

    await ctx.send(f"{member.mention} recebeu um aviso. Motivo: {reason}")
    modlog = await get_or_create_modlog_channel(ctx.guild)
    await modlog.send(
        f"⚠️ **WARN** | {member} ({member.id}) avisado por {ctx.author}. Motivo: {reason}"
    )

    # Aqui pode colocar alguma ação automática ao atingir X warns, ex: mute automático
    if len(warns[guild_id][user_id]) >= 3:
        mute_role = discord.utils.get(ctx.guild.roles, name="Mutado")
        if mute_role and mute_role not in member.roles:
            await member.add_roles(mute_role,
                                   reason="Mute automático por 3 avisos")
            await ctx.send(
                f"{member.mention} foi mutado automaticamente por acumular 3 avisos."
            )
            await modlog.send(
                f"🤐 **MUTE AUTOMÁTICO** | {member} ({member.id}) após 3 avisos."
            )


# WARNINGS
@bot.command()
@commands.has_permissions(manage_messages=True)
async def warnings(ctx, member: discord.Member):
    guild_id = ctx.guild.id
    user_id = member.id
    if guild_id not in warns or user_id not in warns[guild_id]:
        await ctx.send(f"{member.mention} não tem avisos.")
        return

    user_warns = warns[guild_id][user_id]
    embed = discord.Embed(title=f"Avisos de {member}",
                          color=discord.Color.orange())
    for i, warn in enumerate(user_warns, 1):
        mod = ctx.guild.get_member(warn["moderator"])
        embed.add_field(name=f"Aviso {i}",
                        value=f"Moderador: {mod}\nMotivo: {warn['reason']}",
                        inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def ip(ctx):
    embed = discord.Embed(
        title="🌐 IP do Servidor",
        description="**IP e porta do servidor:**\n`Atualmente indisponível`",
        color=discord.Color.blue())
    embed.set_footer(text="Fique ligado para atualizações!")
    await ctx.send(embed=embed)


CARGO_RESTRITO_ID = 1382505875549323346
CARGOS_MODERACAO = [1382505875549323349, 1382838597790470337]


def tem_permissao_mod():

    async def predicate(ctx):
        return any(cargo.id in CARGOS_MODERACAO for cargo in ctx.author.roles)

    return commands.check(predicate)


@bot.command()
@tem_permissao_mod()
async def lock(ctx):
    cargo = ctx.guild.get_role(CARGO_RESTRITO_ID)
    await ctx.channel.set_permissions(cargo,
                                      send_messages=False,
                                      add_reactions=False,
                                      speak=False)
    await ctx.send(f"🔒 Canal bloqueado para {cargo.mention}.")


@bot.command()
@tem_permissao_mod()
async def unlock(ctx):
    cargo = ctx.guild.get_role(CARGO_RESTRITO_ID)
    await ctx.channel.set_permissions(cargo, overwrite=None)
    await ctx.send(f"🔓 Canal desbloqueado para {cargo.mention}.")

@bot.command()
@commands.has_permissions(administrator=True)
async def regrasdc(ctx):
    embed = discord.Embed(
        title="📜 Regras do Servidor",
        description="Leia com atenção e siga todas as regras para mantermos um ambiente saudável!",
        color=discord.Color.orange()
    )

    embed.add_field(name="🔒 Regras Gerais de Convivência", value=(
        "1. **Respeito acima de tudo**\n"
        "2. **Proibido conteúdo NSFW ou ofensivo**\n"
        "3. **Sem spam ou flood**\n"
        "4. **Sem divulgação sem permissão**\n"
        "5. **Nada de brigas ou discussões pesadas**"
    ), inline=False)

    embed.add_field(name="🛠️ Regras Técnicas", value=(
        "6. **Use os canais corretamente**\n"
        "7. **Nicknames e fotos de perfil apropriados**\n"
        "8. **Proibido uso de bots de spam ou comandos indevidos**"
    ), inline=False)

    embed.add_field(name="👑 Regras sobre a Staff", value=(
        "9. **Obedeça à equipe de moderação**\n"
        "10. **Não finja ser da staff**"
    ), inline=False)

    embed.add_field(name="⚠️ Sanções", value=(
        "11. **Avisos, mute, kick ou ban**\n"
        "As punições serão aplicadas conforme a gravidade da infração."
    ), inline=False)

    embed.set_footer(text="Ao permanecer no servidor, você concorda com estas regras.")

    await ctx.send(embed=embed)

@bot.command()
async def mods(ctx):
    embed = discord.Embed(
        title="🧱 Lista de Mods do Servidor Minecraft",
        description=(
            "A lista de mods do servidor ainda não está completa.\n"
            "Fique atento para futuras atualizações e novidades!"
        ),
        color=discord.Color.green()
    )
    embed.set_footer(text="Em breve mais mods serão adicionados!")
    await ctx.send(embed=embed)


keep_alive()
bot.run(os.getenv("TOKEN"))
