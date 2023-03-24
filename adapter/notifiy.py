import requests
import discord


class Notifier:
    def __init__(self, wechat_send_key:str=None, discord_webhook:str=None):
        '''
        wechat、discord notifier

        Args:
            wechat_send_key (str): Wecom机器人的send_key
            discord_webhook (str): discord机器人的webhook
        '''
        self.send_key = wechat_send_key
        self.discord_webhook = discord_webhook

    def send_discord_msg(self, msg, tts:bool=False):
        hook = discord.SyncWebhook.from_url(self.discord_webhook)
        hook.send(msg, tts=tts)

    def send_discord_image(self, image_path:str):
        hook = discord.SyncWebhook.from_url(self.discord_webhook)
        hook.send(file=discord.File(image_path))


    def send_wechat_msg(self, msg):
        '''
        使用server酱发送微信消息
        :param msg: 消息内容
        '''
        proxy = {"http": None, "https": None}
        url = 'http://push.everains.com/wecomchan?sendkey={send_key}&msg={msg}&msg_type=text'.format(send_key=self.send_key, msg=msg)
        requests.get(url, proxies=proxy)

    def combined_send(self, msg:str, tts=True):
        '''
        send wechat and discord

        Args:
            msg (str): message to send
            tts (bool, optional): is tts. Defaults to True.
        '''
        self.send_discord_msg(msg=msg, tts=tts)
        self.send_wechat_msg(msg=msg)

if __name__ == '__main__':
    noty = Notifier(wechat_send_key='')
    noty.send_wechat_msg('test')
