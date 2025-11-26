# N8N Workflows Documentation

This folder contains the static documentation website for the N8N Workflows collection.

## 🚨 Important: How to View the Website

**Do NOT open `index.html` directly in your browser!** This will cause the workflow data to fail to load because browsers block `fetch()` requests on the `file://` protocol for security reasons.

### ✅ Correct Way to View the Website:

#### Option 1: Using Python (Recommended)

```bash
# Navigate to the docs folder
cd docs

# Run the server script
python serve.py
```

Then open: http://localhost:8080

#### Option 2: Using PowerShell (Windows)

```powershell
# Navigate to the docs folder
cd docs

# Run the PowerShell script
.\serve.ps1
```

Then open: http://localhost:8080

#### Option 3: Using Python's Built-in Server

```bash
cd docs
python -m http.server 8080
```

Then open: http://localhost:8080

#### Option 4: Using the Main Application Server

```bash
# From the root directory
python run.py
```

Then open: http://localhost:8000

## 📁 Folder Structure

```
docs/
├── index.html          # Main HTML file
├── logo-web.png        # Website logo
├── serve.py           # Python server script
├── serve.ps1          # PowerShell server script
├── api/               # JSON data files
│   ├── search-index.json
│   ├── categories.json
│   ├── integrations.json
│   └── stats.json
├── css/
│   └── styles.css     # Stylesheets
└── js/
    ├── app.js         # Application logic
    └── search.js      # Search functionality
```

## 🔧 Troubleshooting

### Error: "Failed to load workflow data"

**Cause**: You opened the HTML file directly (file:// protocol)  
**Solution**: Use one of the server options above

### Error: "Address already in use"

**Cause**: Port 8080 is already being used  
**Solution**: Either:

- Stop the other service using port 8080
- Or modify the port number in the serve scripts

### No workflows showing

**Cause**: The `search-index.json` file might be missing or corrupted  
**Solution**: Run `python run.py --reindex` from the root directory to regenerate the index

## 📝 Notes

- This is a static website that can be deployed to GitHub Pages, Netlify, or any static hosting service
- The workflow data is loaded from `api/search-index.json`
- Font Awesome icons are loaded from CDN
- The website is fully responsive and works on mobile devices
