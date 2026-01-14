# 🏋️‍♂️ Workout Tracker — Nutritionix + Google Sheets (Sheety)

Track your daily workouts and automatically calculate calories burned based on workout **type + intensity**, using the **Nutritionix API**, while storing everything neatly inside **Google Sheets** via **Sheety API** ✅

---

## ✨ Features

✅ Log daily workouts using natural language
✅ Automatically fetch calories burned (based on intensity + duration)
✅ Save workout data directly into Google Sheets
✅ View exercise logs in a clean spreadsheet format
✅ Authentication supported via Sheety Bearer Token

---

## 🧠 How It Works

This app connects two powerful services:

### 1️⃣ Nutritionix Exercise API

You input exercises like:

> `ran 3 km and did 20 minutes weight training`

Nutritionix interprets it and returns:

* Exercise name
* Duration
* Calories burned
* MET values (intensity)

### 2️⃣ Google Sheets via Sheety

Sheety converts your Google Sheet into a REST API.
Workout logs are pushed to your sheet automatically.

---

## 🛠 Tech Stack

* **Python**
* **Nutritionix API**
* **Sheety API**
* **Google Sheets**
* `requests` library

---

## 📌 Requirements

Before running the app, make sure you have:

✅ A Google Sheet connected to Sheety
✅ Sheety Bearer Token Authentication
✅ Nutritionix API credentials

---

## 🔐 Getting API Keys & Auth Setup

### ✅ Step 1 — Create Sheet in Google Sheets

Create a sheet with columns like:

| Date | Exercise | Duration | Calories |
| ---- | -------- | -------- | -------- |

Example sheet name:
`workoutTracker`

---

### ✅ Step 2 — Enable Sheety API

1. Go to: [https://sheety.co/](https://sheety.co/)
2. Login using your **Google Account**
3. Create a new Sheety Project linked to your Google Sheet
4. Enable **Bearer Authentication**
5. Copy your API endpoint, example:

```
https://api.sheety.co/<project_id>/workoutTracker/workouts
```

---

### ✅ Step 3 — Generate Sheety Bearer Token

In Sheety:

* Go to your project settings
* Enable **Bearer Authentication**
* Copy your **Bearer Token** ✅

You’ll use it like:

```
Authorization: Bearer YOUR_SHEETY_TOKEN
```

---

### ✅ Step 4 — Get Nutritionix API Credentials

1. Go to: [https://www.nutritionix.com/business/api](https://www.nutritionix.com/business/api)
2. Create an account & register an application
3. Get:

   * **APP_ID**
   * **API_KEY**

---

## ⚙️ Environment Variables

Create a `.env` file (recommended):

```env
NUTRITIONIX_APP_ID=your_app_id_here
NUTRITIONIX_API_KEY=your_api_key_here
SHEETY_BEARER_TOKEN=your_sheety_token_here
SHEETY_ENDPOINT=https://api.sheety.co/<project_id>/workoutTracker/workouts
```

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/workout-tracker.git
cd workout-tracker
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the application:

```bash
python main.py
```

Enter exercise details like:

✅ `walked 45 minutes`
✅ `did 25 minutes yoga`
✅ `ran 5 km and cycled 30 minutes`

The app will:

1. Send the input to Nutritionix API
2. Fetch calories burned based on workout intensity
3. Push the workout data into Google Sheets via Sheety ✅

---

## 📄 Example Output in Google Sheets

| Date       | Exercise        | Duration | Calories |
| ---------- | --------------- | -------- | -------- |
| 2026-01-14 | Running         | 30       | 320      |
| 2026-01-14 | Weight Training | 20       | 150      |

---

## 📁 Project Structure

```
workout-tracker/
│
├── main.py
├── requirements.txt
├── .env
└── README.md
```

---

## 🚀 Future Enhancements (Ideas)

✨ Add a Streamlit/Web UI
✨ Add exercise history & filters
✨ Monthly calorie summary dashboard
✨ Auto-sync workouts from fitness devices

---

## 🤝 Contributing

Pull requests are welcome!
If you have feature suggestions, feel free to open an issue ⭐

---

## 📜 License

This project is licensed under the MIT License.

---

## ⭐ Support

If this project helped you, please consider giving it a ⭐ on GitHub — it motivates me to build more!
