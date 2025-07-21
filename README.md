# JalenLaunchpad

A lightweight Python/Tkinter launcher that lets you sort executables into custom categories (Work, Games, Utilities, etc.) and fire them up with a single click.

---

## Features
- 📂 **Categorized library** – create, rename, and delete categories  
- ➕ **One-click add** – browse and store any `.exe` under the selected category  
- 🚀 **Run All / Run Selected** – launch everything in a category or just one app  
- 💾 **Persistent JSON config** – your layout survives restarts  
- 🎨 Simple, clean UI (white sidebar / black main pane by default)

---

## Quick Start
1. **Clone** this repo or download the ZIP.  
2. Ensure you have **Python 3.8+** installed (Tkinter ships with the standard installer).  
3. Run the launcher:  
   ```bash
   python GUI.py
   ```

   ## 🔧 How It Works

- Config is stored in `save.json` next to the script.
- Each category maps to a list of absolute file paths.
- Adding or deleting apps/categories auto-saves the file.

---

## 🧭 Roadmap / Ideas

- ✅ Drag-and-drop reordering  
- 🎨 Custom icons for each entry  
- 📥 System-tray minimization  
- ⌨️ Keyboard shortcuts (Ctrl + 1…9) to launch favorites

---

## 🤝 Contributing

Pull requests are welcome! Feel free to open an issue for bugs or feature suggestions.
