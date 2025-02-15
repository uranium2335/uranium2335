from tkinter import *

money = 0
upgrade_money_1 = 0.1
auto_money_amount = 0.5

buttonup1_cost_1 = 25
autoupgrade_cost = 100

upgrade_money_clicked = False
auto_button_clicked = False
upgrade_money_1_clicked = False
upgrade_auto_click = False

# Format numbers based on value
def format_number(value):
    """Format number as scientific notation if large, else as a float."""
    return f'{value:.2e}' if value >= 1e8 else f'{value:.1f}'

# Update all numeric displays
def update_money_display():
    number.config(text=format_number(money))

def update_click_strength_display():
    click_strength.config(text=f'{format_number(upgrade_money_1)} /click')

def update_upgrade_button_display():
    upgrade_button1.config(text=f'upgrade click strength: {format_number(buttonup1_cost_1)}')

def update_automoney_amount_button_display():
    auto_button_upgrade1.config(text=f'{format_number(autoupgrade_cost)} money to buy')

# Click to make money button function
def click():
    global money
    print('made')
    money += upgrade_money_1
    update_money_display()
    if money >= 10 and not auto_button_clicked:
        auto_button.config(state=ACTIVE)
    else:
        auto_button.config(state=DISABLED)

# Enabling auto money
def auto_click():
    global money, auto_button_clicked
    print('auto mode')
    if money >= 10 and not auto_button_clicked:
        money -= 10
        auto_button_clicked = True
        update_money_display()
        auto_button.config(state=DISABLED)
        generate_auto_money()

# Generate money automatically
def generate_auto_money():
    global money
    if auto_button_clicked:
        money += auto_money_amount
        update_money_display()
        window.after(750, generate_auto_money)

# upgrades the auto money button
def auto_click_upgrade():
    global money, upgrade_auto_click, autoupgrade_cost ,auto_money_amount
    if money >= autoupgrade_cost:
        auto_money_amount += auto_money_amount * 1.2
        money-=autoupgrade_cost
        autoupgrade_cost += autoupgrade_cost * 1.5
        upgrade_auto_click = True
        update_money_display()
        update_automoney_amount_button_display()
        print(f'new auto money cost {autoupgrade_cost}')
        print(f'money per tick {auto_money_amount}')

# Upgrade button function
def upgrade_button_1():
    global upgrade_money_1, money, buttonup1_cost_1, upgrade_money_1_clicked
    if money >= buttonup1_cost_1 and not upgrade_money_clicked:
        upgrade_money_1 += upgrade_money_1 * 1.2
        money -= buttonup1_cost_1
        buttonup1_cost_1 += buttonup1_cost_1 * 1.25
        upgrade_money_1_clicked = True
        update_money_display()
        update_upgrade_button_display()
        update_click_strength_display()
        print(f'new cost {buttonup1_cost_1}')
        print(f'money per click {upgrade_money_1}')

# Create the main window
window = Tk()
window.geometry('1000x1000')
window.config(bg='grey')

# "Make Money" button
button = Button(window, text='Click to make money', command=click)
button.config(font=('Ink Free', 50, 'bold'), fg='blue', bg='red')
button.config(activebackground='blue')
button.config(activeforeground='red')
button.place(x=200, y=10)

# Upgrade button 1
upgrade_button1 = Button(window, text=f'upgrade click strength: {format_number(buttonup1_cost_1)}', command=upgrade_button_1)
upgrade_button1.config(font=('Monospace', 20, 'bold'), fg='#7f03fc', bg='#fce303')
upgrade_button1.config(activebackground='#7f03fc')
upgrade_button1.config(activeforeground='#fce303')
upgrade_button1.place(x=10, y=200)

# "Auto Money" button
auto_button = Button(window, text='10 money to buy', command=auto_click)
auto_button.config(font=('Monospace', 10, 'bold'), state=DISABLED)
auto_button.place(x=30, y=50)

# "Auto Money" upgrade button
auto_button_upgrade1 = Button(window,text='100 money to buy' , command=auto_click_upgrade)
auto_button_upgrade1.config(font=('Monospace', 10, 'bold'))
auto_button_upgrade1.place(x=30, y=100)

# Money per click label
click_strength = Label(window, text=f'{format_number(upgrade_money_1)} /click')
click_strength.config(font=('Monospace', 10, 'bold'), bg='grey', fg='pink')
click_strength.place(x=875, y=75)

# Money display
number = Label(window, text=format_number(money))
number.config(font=('Monospace', 50, 'bold'), fg='black', bg='grey')
number.place(x=475, y=500)

# Start the main loop
window.mainloop()
