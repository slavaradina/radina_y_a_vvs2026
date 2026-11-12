import tkinter as tk
from tkinter import messagebox

#проверка регистрации
def check_registration():
  nick = entry_nick.get()
  email = entry_email.get()
  password = entry_pass.get()

  if len(nick) < 3:
    messagebox.showerror("ошибка", "никнейм слишком короткий")
    return

  if "@" not in email or "." not in email:
    messagebox.showerror("ошибка", "введи почту нормально")
    return

  if len(password) < 5:
    messagebox.showerror("ошибка", "пароль слишком короткий")
    return

  messagebox.showinfo(
      "ура",
      f"привет, {nick}! ты успешно зарегистровался. теперь выбери тариф"
      " подписки, это обязательно)))",
  )
  frame_reg.pack_forget()  #убрать блок регистрации
  frame_sub.pack(expand=True)

#проверка карты и покупка
def buy_subscription():
  card = entry_card.get()
  plan = sub_var.get()  #узнаем какой тариф выбрал пользователь

  if len(card) != 16 or not card.isdigit():
    messagebox.showerror("ошибка оплаты", "неверный номер карты")
    return

  messagebox.showinfo(
      "поздравляем!",
      f"ура, ты купил самую бесполезную подписку на DeepSeekPro ({plan})! с"
      " карты списана куча денег)))",
  )

#главное окно
window = tk.Tk()
window.title("подписка на DeepSeekPro")
window.geometry("600x600")  #ширина 600, высота 600 

frame_reg = tk.Frame(window)
frame_reg.pack(expand=True)

#блок регистрации
label_title = tk.Label(
    frame_reg, text="регистрация в DeepSeekPro", font=("Arial", 16, "bold")
)
label_title.pack(pady=10)

#никнейм 
tk.Label(frame_reg, text="твой никнейм:").pack()
entry_nick = tk.Entry(frame_reg)
entry_nick.pack(pady=5)

#почта 
tk.Label(frame_reg, text="твоя почта:").pack()
entry_email = tk.Entry(frame_reg)
entry_email.pack(pady=5)

#пароль 
tk.Label(frame_reg, text="придумай пароль:").pack()
entry_pass = tk.Entry(frame_reg, show="*")
entry_pass.pack(pady=5)

#пол
tk.Label(frame_reg, text="выбери пол:").pack(pady=5)
gender_var = tk.StringVar(value="женский")
tk.Radiobutton(
    frame_reg, text="женский", variable=gender_var, value="женский"
).pack()
tk.Radiobutton(
    frame_reg, text="мужской", variable=gender_var, value="мужской"
).pack()

#"зарегистрироваться" 
btn_reg = tk.Button(
    frame_reg,
    text="зарегистрироваться",
    bg="lightblue",
    command=check_registration,
)
btn_reg.pack(pady=15)

#подписка
frame_sub = tk.Frame(window)

tk.Label(
    frame_sub,
    text="выбери тариф DeepSeekPro (бесплатного нет):",
    font=("Arial", 12, "bold"),
).pack(pady=5)

sub_var = tk.StringVar(value="1 месяц за $5,000")

tk.Radiobutton(
    frame_sub,
    text="на 1 месяц - $5,000",
    variable=sub_var,
    value="1 месяц за $5,000",
).pack()
tk.Radiobutton(
    frame_sub,
    text="на 3 месяца - $10,000",
    variable=sub_var,
    value="3 месяца за $10,000",
).pack()
tk.Radiobutton(
    frame_sub,
    text="на 1 год — $100,000",
    variable=sub_var,
    value="1 год за $100,000",
).pack()

#ввод номера карты
tk.Label(frame_sub, text="введи номер карты:").pack(pady=10)
entry_card = tk.Entry(frame_sub)
entry_card.pack(pady=5)

#оплата
btn_buy = tk.Button(
    frame_sub, text="купить подписку", bg="lightgreen", command=buy_subscription
)
btn_buy.pack(pady=15)

#запуск окна
window.mainloop()
