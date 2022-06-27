import tkinter as tk

root = tk.Tk()
root.geometry('400x300')
root['bg'] = 'cyan'
root.title('Cmd')

inputTextVar = tk.StringVar(root)

outputText = tk.Text(root, height=11, width=45, state=tk.DISABLED)
outputText.place(x=20, y=100)

inputText = tk.Entry(root, textvariable=inputTextVar, width=50)
inputText.place(x=20, y=30)


def run(command):  # Распределитель команд если не kill
    command = command.split()
    command, *args = command
    if command == 'kill':
        kill(1)
    else:
         return connect(command, *args)

def connect(command, *args):  # Обработка командd
    if command == 'shampoo':
        try:
            via = args[0]
            mark = args[1]
            ml = args[2]
            flush = args[3]
        except Exception:
            return 'SyntaxError'
        if not checkCommand('shampoo', *args):  # 
            return 'SyntaxError'

        if flush == 'true':
            return f'FLUSHED SHAMPOO via {mark}, {ml} Ml'
        else:
            return f'RUN SHAMPOO -> {mark}, {ml} Ml'
    
    elif command == 'connect':
        try:
            ip = args[0]
            user = args[1]
        except Exception:
            return 'SyntaxError'
        if not checkCommand('connect', *args):
            return 'connection refused! Incorrect IPv4 Adress'
        return f'connecting to {user} via IPv4: {ip}'
    
    elif command == 'cls':
        outputText.configure(state='normal')
        outputText.delete(1.0, tk.END) 
        outputText.configure(state='disabled')
        return ''

    elif command == 'crush':
        try:
            flag = args[0]
            flag2 = args[1]
        except Exception:
            return 'to crush enter "crush -f 739"\nThis will crush Python!'
        if flag == '-f' and flag2 == '739':
            q = 999999999999**9999999999999999
        else:
            return 'to crush enter "crush -f 739"'

    elif command == 'help':
        if len(args) == 0:
            txt = """============HELP MENU=============
commands: shampoo, connect, cls, crush
Чтобы получить помощь по команде введи help и название команды, например:
help crush"""
            return txt
        else:
            arg = args[0]
            if arg == 'shampoo':
                return 'Просто команда для теста. \nСинтаксис: shampoo via <марка> <миллилитры> <true/false>'
            elif arg == 'connect':
                return 'Типо подключение на ip. \nСинтаксис: connect <ip> <user>'
            elif arg == 'cls':
                return 'Очистка поля вывода.'
            elif arg == 'crush':
                return 'Крашит программу путём вычисления большого числа. \nСинтаксис: crush -f 739'
            else:
                return 'Команды не существует. Введи help для получения списка программ'


    else:
        return 'IncorrectCommandError'

def checkCommand(cmd, *args):  # Проверка правильности введёной команды
    if cmd == 'shampoo':
        via = args[0]
        mark = args[1]
        ml = args[2]
        flush = args[3]
        return True if via == 'via' and flush == 'true' or flush == 'false' else False

    elif cmd == 'connect':
        try:
            ip = args[0]
            user = args[1]
            q = ip.split('.')
            for w in q:
                w = int(w)
                if not w <= 255 and w >= 0:
                    return False
        except Exception:
            return False
        return True
    
def kill(event):  # Выход
    exit(144)

def beautifulPrint(text):  #  Красивый вывод
    for letter in text:
        root.after(50)
        write(letter)
        root.update()
    write('\n')
 
def write(text):  # Запись в текстовое поле
    outputText.configure(state=tk.NORMAL)
    outputText.insert(tk.END, text)
    outputText.configure(state=tk.DISABLED)

def start(event=None):  # Запуск комманды
    command = inputTextVar.get()
    if len(command) == 0: output = 'EmptyStringError'
    else: output = run(command)
    beautifulPrint(output)

tk.Button(root, bg='cyan', text='Enter', command=start).place(x=345, y=25)
root.bind('<Alt_L>', start)
root.bind('<Escape>', kill)
root.mainloop()