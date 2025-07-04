# ⏳ Event Countdown App

Create beautiful, timezone-aware event countdown pages with redirect links and logos — powered by Flask + MongoDB + Moment.js.


---

## 🚀 Features

- 🎯 Create event countdowns with:
  - Name
  - Timezone & Date/Time
  - Logo image
  - Redirect URL
- 🔗 Unique short-code URLs (like `/event/abc123`)
- ⏲ Live animated countdowns
- 🌍 Timezone conversion (local + event)
- 📱 Responsive design

---

## 🛠 Tech Stack

- **Backend**: Flask, PyMongo, shortuuid
- **Database**: MongoDB Atlas
- **Frontend**: HTML + CSS + JavaScript (Moment.js, Timezone)
- **UI**: Glassmorphism + particle background

---

## 📁 Folder Structure

```
project-root/
├── app.py
├── index.html         # Event creation form
├── event.html         # Countdown page
├── home.html          # Optional homepage
├── .env               # MongoDB URI (not public)
├── .gitignore
├── timezones.json     # Optional
└── requirements.txt
```

---

## 🔧 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/event-countdown.git
cd event-countdown
```

### 2. Install requirements

```bash
pip install -r requirements.txt
```

### 3. Create `.env` file

```env
MONGODB_URI=mongodb+srv://username:password@your-cluster.mongodb.net/?retryWrites=true&w=majority
```

### 4. Run locally

```bash
python app.py
```

Visit: [http://localhost:5000](http://localhost:5000)

---

## 🌐 Deploy to the Web

You can deploy easily using any of the following:

### ▶ Render

1. Go to [https://render.com](https://render.com)
2. Click “New Web Service”
3. Connect your GitHub repo
4. Add your `MONGODB_URI` in **Environment Variables**
5. Set:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python app.py`

### ▶ Replit

1. Create a new Python repl
2. Upload your files
3. Add `.env` using Secrets tab
4. Run `python app.py`

### ▶ Railway

1. Import GitHub repo
2. Add `MONGODB_URI` as environment variable
3. Deploy 🎉

---

## 📸 Screenshots

### 🎯 Create Event
![form](https://github.com/yourusername/event-countdown/assets/yourusername/form.png)

### ⏳ Countdown Page
![countdown](https://github.com/yourusername/event-countdown/assets/yourusername/countdown.png)

---

## 🧾 License

MIT License. Madeby [Sanjesh](https://github.com/Sanjesh-S)
