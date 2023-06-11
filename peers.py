from tkinter import *
from tkinter import ttk
import sqlite3
import pyautogui
import time
import win32clipboard
import os
from datetime import datetime



tree_fields = [
    'id',
    'username',
    'comments_given',
    'retweets_given',
    'comments_received',
    'retweets_received',
    'priority',
]


##############################################################
# DATABASE
##############################################################
database_name = 'database.db'



def drop_table(table):
	conn = sqlite3.connect(database_name)
	c = conn.cursor()
	c.execute(f'drop table {table}')
	conn.commit()
	conn.close()


def db_create_table_peers():
	conn = sqlite3.connect(database_name)
	c = conn.cursor()
	c.execute(f'''
		create table if not exists peers (
			username text,
			comments_given text,
			retweets_given text,
			comments_received text,
			retweets_received text,
            priority_integer
		)
	''')
	conn.commit()
	conn.close()


def db_get_all_rows_peers():
	conn = sqlite3.connect(database_name)
	c = conn.cursor()
	c.execute('select rowid, * from peers')
	records = c.fetchall()	
	conn.commit()
	conn.close()
	return records


def db_get_selected_rows_peers(username):
	conn = sqlite3.connect(database_name)
	c = conn.cursor()
	sql = '''select rowid, * from peers where username = ?'''
	c.execute(sql, (username,))
	records = c.fetchall()
	conn.commit()
	conn.close()
	return records


def db_insert_row_peers(data):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute('insert into peers values (:username, :comments_given, :retweets_given, :comments_received, :retweets_received, :priority)',
        {
            'username': data,
            'comments_given': 0,
            'retweets_given': 0,
            'comments_received': 0,
            'retweets_received': 0,
            'priority': 0,
        }
    )
    conn.commit()
    conn.close()
    

def db_delete_row_peers(data):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    selected = tree.focus()
    values = tree.item(selected, 'values')
    c.execute(f'delete from peers where username={values[1]}')
    conn.commit()
    conn.close()


def db_update_row(values):
	data = values[1:]
	data.append(values[0])

	conn = sqlite3.connect(database_name)
	c = conn.cursor()
	sql = '''update peers set
		username = ?,
		comments_given = ?,
		retweets_given = ?,
		comments_received = ?,
		comments_received = ?,
		priority = ?

		where oid = ?'''
	c.execute(sql, data)
	conn.commit()
	conn.close()







def tk_get_entries_vals():
	return [entry.get() for entry in entries]


def tk_refresh_tree(rows):
    tree.delete(*tree.get_children())
    for index, row in enumerate(rows):
        tree.insert(parent='', index=index, iid=index, text='', values=row)





def tk_add(e):
    add_window = Toplevel(root)
    add_window.title('Add Peer')

    add_frame = Frame(add_window)
    add_frame.pack(padx=16, pady=16)
    add_label = Label(add_frame, text='Add Peer')
    add_label.grid(row=0, column=0, sticky=W)
    add_entry = Entry(add_frame)
    add_entry.grid(row=0, column=1, sticky=W)

    add_entry.focus_set()

    def tk_add_binding_return(e):
        data = add_entry.get()
        rows = db_get_all_rows_peers()
        accounts = [row[1] for row in rows]
        if data == '' or data in accounts: return
        db_insert_row_peers(data)
        add_entry.delete(0, END)
        tk_refresh_tree(db_get_all_rows_peers())

    add_entry.bind('<Return>', tk_add_binding_return)


def tk_delete(e):
    db_delete_row_peers()
    tk_refresh_tree(db_get_all_rows_peers())
    tk_clear_entries()


def tk_update_record():
	values = tk_get_entries_vals()
	db_update_row(values)
	tree.item(tree.focus(), text='', values=values)



root = Tk()
root.geometry('800x600')

frame_fields = Frame(root, padx=20, pady=10)
frame_fields.pack(side=LEFT, fill=Y)

labels = []
entries = []
for i, field in enumerate(tree_fields):
	labels.append(Label(frame_fields, text=field).grid(row=i, column=0, sticky=W))
	tmp_entry = Entry(frame_fields)
	if field == 'id':
		tmp_entry.insert(0, '-')
		tmp_entry.config(state='readonly')
	tmp_entry.grid(row=i, column=1, sticky=W)
	entries.append(tmp_entry)
i += 1
update_button = Button(frame_fields, text='Update', command=tk_update_record)
update_button.grid(row=i, column=0, sticky=W)
i += 1



frame_tree = Frame(root)
frame_tree.pack(side=LEFT, expand=True, fill=BOTH)

tree = ttk.Treeview(frame_tree)
tree.pack(expand=True, fill=BOTH)

tree['columns'] = tree_fields

tree.column('#0', width=0, stretch=NO)
tree.heading('#0', text='', anchor=W)
for field in tree_fields:
	tree.column(field, width=80, anchor=W)
	tree.heading(field, text=field, anchor=W)
    


def tk_tree_select_next_row(e):
    try:
        next_row = int(tree.focus()) + 1
        tree.focus(next_row)
        tree.selection_set(next_row)
    except: pass


def tk_tree_select_prev_row(e):
    try:
        next_row = int(tree.focus()) - 1
        tree.focus(next_row)
        tree.selection_set(next_row)
    except: pass


def tk_tree_comments_given(e):
    item_iid = tree.focus()
    username = tree.item(item_iid)['values'][1]
    row = list(db_get_selected_rows_peers(username)[0])
    row[2] = int(row[2]) + 1
    db_update_retweets_given_peers(row)
    tk_refresh_tree(db_get_all_rows_peers())
    tree.focus(item_iid)
    tree.selection_set(item_iid)


def tk_tree_retweets_given(e):
    item_iid = tree.focus()
    username = tree.item(item_iid)['values'][1]
    row = list(db_get_selected_rows_peers(username)[0])
    row[3] = int(row[3]) + 1
    db_update_retweets_given_peers(row)
    tk_refresh_tree(db_get_all_rows_peers())
    tree.focus(item_iid)
    tree.selection_set(item_iid)

    
def tk_tree_comments_received(e):
    item_iid = tree.focus()
    username = tree.item(item_iid)['values'][1]
    row = list(db_get_selected_rows_peers(username)[0])
    row[4] = int(row[4]) + 1
    db_update_retweets_given_peers(row)
    tk_refresh_tree(db_get_all_rows_peers())
    tree.focus(item_iid)
    tree.selection_set(item_iid)
    

def tk_tree_retweets_received(e):
    item_iid = tree.focus()
    username = tree.item(item_iid)['values'][1]
    row = list(db_get_selected_rows_peers(username)[0])
    row[5] = int(row[5]) + 1
    db_update_retweets_given_peers(row)
    tk_refresh_tree(db_get_all_rows_peers())
    tree.focus(item_iid)
    tree.selection_set(item_iid)


def gui_search_twitter(e):
    pos = pyautogui.locateOnScreen('twitter-ico.png')
    pyautogui.moveTo(pos)
    pyautogui.click()
    time.sleep(1)

    pyautogui.moveTo(150, 50)
    pyautogui.click()

    with pyautogui.hold('ctrl'):
        pyautogui.press('a')
    pyautogui.press('delete')

    item_iid = tree.focus()
    oid = int(item_iid) + 1
    username = tree.item(item_iid)['values'][1]
    row = list(db_get_selected_rows_peers(username)[0])

    pyautogui.write(f'https://twitter.com/{row[1]}')
    pyautogui.press('enter')


def gui_chatgpt(e):
    pos = pyautogui.locateOnScreen('chatgpt-tab-ico.png')
    pyautogui.moveTo(pos)
    pyautogui.click()
    pos = pyautogui.locateOnScreen('chatgpt-edit.png')
    pyautogui.moveTo(pos)
    pyautogui.click()
    pyautogui.moveTo(pos[0]-300, pos[1]-50)
    pyautogui.click()
    with pyautogui.hold('ctrl'):
        pyautogui.press('a')
    pyautogui.press('delete')
    time.sleep(1)

    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()

    text = f'''write 5 replies to this tweet:
    
    {data}

    Here are a few rules to follow:
    - make the reply 2 sentences long 
    - expand on the tweet with an actionable step, tips, or advice that wasn't mentioned in the previous tweet (but that's related)
    '''

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(text, win32clipboard.CF_TEXT)
    win32clipboard.CloseClipboard()

    # text = text.strip()
    # print(text)
    # pyautogui.write(text)
    
    with pyautogui.hold('ctrl'):
        pyautogui.press('v')
    time.sleep(1)

    pos = pyautogui.locateOnScreen('chat-save.png')
    print(pos)
    pyautogui.moveTo(pos)
    pyautogui.click()


def gui_post(e):
    pos = pyautogui.locateOnScreen('twitter-ico.png')
    pyautogui.moveTo(pos)
    pyautogui.click()
    time.sleep(1)
    
    pos = pyautogui.locateOnScreen('twitter-smile.png')
    pyautogui.moveTo(pos[0], pos[1]-50)
    pyautogui.click()
    time.sleep(1)
    
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    pyautogui.write(data)

def gui_order_by_name(e):    
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute('select * from peers order by username')
    records = c.fetchall()	
    conn.commit()
    conn.close()
	
    for r in records:
        print(r)

def gui_order_by_priority(e):    
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute('select oid, * from peers order by priority desc')
    records = c.fetchall()	
    conn.commit()
    conn.close()
	
    for r in records:
        print(r)

    tk_refresh_tree(records)


    
def tk_select_record(e):
	selected = tree.focus()
	values = tree.item(selected, 'values')

	for k, entry in enumerate(entries):
		if k == 0:
			entry.config(state='normal')
			entry.delete(0, END)
			entry.insert(0, values[k])
			entry.config(state='readonly')
		else:
			entry.delete(0, END)
			entry.insert(0, values[k])

##############################################################
# KEY BINDING
##############################################################
tree.bind('<ButtonRelease-1>', tk_select_record)

tree.bind("a", tk_add)
tree.bind("<Delete>", tk_delete)
tree.bind('j', tk_tree_select_next_row)
tree.bind('k', tk_tree_select_prev_row)
tree.bind('e', tk_tree_comments_given)
tree.bind('r', tk_tree_retweets_given)
tree.bind('u', tk_tree_comments_received)
tree.bind('i', tk_tree_retweets_received)

tree.bind('o', gui_search_twitter)
tree.bind('c', gui_chatgpt)
tree.bind('1', gui_order_by_name)
tree.bind('2', gui_order_by_priority)

# tree.bind('f', gui_post)


##############################################################
# INIT
##############################################################

with open('update.csv') as f:
    date = f.read()

today_date = datetime.now().date()

if str(date) != str(today_date):
    records = db_get_all_rows_peers()

    records_updated = ()
    for record in records:
        record = list(record)
        try:
            record[6] = int(record[6]) - 1
        except:
            pass
        print(record)

        db_update_row(record)
    
with open('update.csv', 'w') as f:
    f.write(str(today_date))

db_create_table_peers()
tk_refresh_tree(db_get_all_rows_peers())
tree.focus_set()
tree.focus(0)
tree.selection_set(0)


root.mainloop()



##############################################################
# MOD DB
##############################################################

# conn = sqlite3.connect(database_name)
# c = conn.cursor()
# c.execute('ALTER TABLE peers add priority integer')
# conn.commit()
# conn.close()






