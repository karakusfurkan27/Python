import random

# Chatbot yanıtları
responses = {
    'merhaba': ['Merhaba! Size nasıl yardımcı olabilirim?', 'Selam! Ne yapabilirim?'],
    'nasılsın': ['İyiyim, teşekkür ederim! Siz nasılsınız?', 'Ben robotum, her zaman iyiyim!'],
    'ne yapabilirsin': ['Sizinle sohbet edebilirim, sorularınızı yanıtlayabilirim.', 'Yardım etmek için buradayım!'],
    'görüşürüz': ['Hoşça kalın!', 'Görüşürüz, tekrar beklerim!'],
    'adın ne': ['Ben bir chatbotum, adım yok ama istediğiniz bir isim verebilirsiniz!', 'Benim adım yok, siz istediğiniz gibi çağırabilirsiniz.'],
    'hangi dilde konuşuyorsun': ['Türkçe konuşabiliyorum!', 'Ben Türkçe konuşuyorum.'],
    'bugün hava nasıl': ['Maalesef hava durumu verisini alamıyorum, ancak dışarıya bakabilirsiniz.', 'Bugünün havasını öğrenmek için yerel hava durumu sitesine bakmanızı tavsiye ederim.'],
    'en sevdiğin renk ne': ['Ben bir yapay zeka olduğum için rengim yok, ama mavi çok sevilen bir renk!'],
    'ne zaman doğdun': ['Ben bir yazılımım, doğum günüm yok. Ama yine de bir şeyler öğrenebilirim!'],
    'kaç yaşındasın': ['Yaşım yok, çünkü bir yazılımım. Zaman kavramım yok!'],
    'ne tür filmler seversin': ['Ben bir yapay zeka olduğum için film izleyemem, ama aksiyon ve bilim kurgu popüler türlerdir!']
}

def chatbot():
    print("Chatbot: Merhaba, nasıl yardımcı olabilirim?")
    
    while True:
        user_input = input("Kullanıcı: ").lower()
        
        # Eğer kullanıcı "çıkış" derse sohbeti bitir
        if 'çıkış' in user_input:
            print("Chatbot: Görüşürüz!")
            break
        
        # Kullanıcının girdiği metne göre yanıt
        for key in responses:
            if key in user_input:
                print("Chatbot:", random.choice(responses[key]))
                break
        else:
            print("Chatbot: Bunu anlamadım, tekrar edebilir misiniz?")

# Chatbot'u başlat
chatbot()
