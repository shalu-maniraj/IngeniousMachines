from googletrans import Translator

translater = Translator()

out = translater.translate("I Like Food", dest="te")

print(out)