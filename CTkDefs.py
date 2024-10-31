import customtkinter as ctk
#CustomTkinterを書きやすくするための関数たち

#Label
def labelDef(name, root, text, row, column, sticky, font, fontSize, padx, pady) :

    name = ctk.CTkLabel(root, text=text, font=(font, fontSize))
    name.grid(row=row, column=column, sticky=sticky, padx=padx, pady=pady)

#Button
def buttonDef(name, root, text, row, column, padx, pady, Def) :

    name = ctk.CTkButton(root, text=text)
    name.grid(row=row, column=column, padx=padx, pady=pady)
    name.bind("<Button-1>", lambda e:Def)
    
#Entry 
def entryDef(name, root, width, row, column, padx, pady) :

    name = ctk.CTkEntry(root, width=width, border_width=0)
    name.grid(row=row, column=column, padx=padx, pady=pady)

#close
def close(name) :

    name.destroy()








