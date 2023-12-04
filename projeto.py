from abc import ABC, abstractmethod

# Definindo uma classe abstrata para representar o canal de comunicação
class CanalComunicacao(ABC):
    @abstractmethod
    def enviar_mensagem(self, mensagem):
        pass

# Definindo classes para representar canais específicos
class WhatsApp(CanalComunicacao):
    def enviar_mensagem(self, mensagem):
        print(f"Enviando mensagem pelo WhatsApp: {mensagem}")

class Telegram(CanalComunicacao):
    def enviar_mensagem(self, mensagem):
        print(f"Enviando mensagem pelo Telegram: {mensagem}")

class Facebook(CanalComunicacao):
    def enviar_mensagem(self, mensagem):
        print(f"Enviando mensagem pelo Facebook: {mensagem}")

class Instagram(CanalComunicacao):
    def enviar_mensagem(self, mensagem):
        print(f"Enviando mensagem pelo Instagram: {mensagem}")

# Definindo uma classe para representar a aplicação de chatbots
class AplicacaoChatbot:
    def __init__(self, canais):
        self.canais = canais

    def enviar_mensagem_para_todos_canais(self, mensagem):
        for canal in self.canais:
            canal.enviar_mensagem(mensagem)

# Testando o código
if __name__ == "__main__":
    whatsapp = WhatsApp()
    telegram = Telegram()
    facebook = Facebook()
    instagram = Instagram()

    canais = [whatsapp, telegram, facebook, instagram]

    aplicacao_chatbot = AplicacaoChatbot(canais)
    mensagem_texto = "Olá, isso é um exemplo de mensagem de texto!"

    aplicacao_chatbot.enviar_mensagem_para_todos_canais(mensagem_texto)

