# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".

work_text = "ооооо абв оооабвоо ооооо абвооооо ооооо оооооабв"
text_lst = work_text.split()
result = [el for el in text_lst if not "абв" in el]         
print(' '.join(result))