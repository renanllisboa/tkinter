import tkinter as tk, tkinter.ttk as ttk

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

   
def main():
    root = tk.Tk()
    root.title("World of Warcraft Character Creator")
    
    label = tk.Label(root, text="Welcome to the World of Warcraft Character Creator")
    label.pack(pady=20)

    label_char_class = tk.Label(root, text="Class:")
    label_char_class.pack(pady=10)
    char_class = ttk.Combobox(root, values=["Warrior", "Mage", "Priest", "Rogue", "Hunter", "Warlock", "Shaman", "Druid", "Paladin"])
    char_class.pack(pady=10)

    label_faction = tk.Label(root, text="Faction:")
    label_faction.pack(pady=10) 
    faction = ttk.Combobox(root, values=["Alliance", "Horde"])
    faction.pack(pady=10)

    label_spec = tk.Label(root, text="Spec")
    label_spec.pack(pady=10)
    spec = ttk.Combobox(root, values=["Tank", "DPS", "Healer"])
    spec.pack(pady=10)

    label_race = tk.Label(root, text="Race") # O rodrigo tem obesidade morbida
    label_race.pack(pady=10)
    races = [
        "Human", "Dwarf", "Night Elf", "Gnome", "Orc", "Undead", "Tauren", "Troll", "Blood Elf", "Draenei",
        "Worgen", "Goblin", "Pandaren", "Void Elf", "Lightforged Draenei", "Nightborne", "Highmountain Tauren",
        "Zandalari Troll", "Kul Tiran", "Dark Iron Dwarf", "Mechagnome", "Vulpera", "Mag'har Orc"
    ]
    race = ttk.Combobox(root, values=races)
    race.pack(pady=10)

    def on_confirm():
        result = f"Your class is: {char_class.get()}, your faction is: {faction.get()} your spec is: {spec.get()} and your race is: {race.get()}" 
        print(result)
        root.destroy()

    button_confirm = tk.Button(root, text="Confirmar", command=on_confirm)
    button_confirm.pack(pady=10)
    center_window(root)
    
    root.mainloop()

if __name__ == "__main__":
    main()
