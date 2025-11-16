# 🚀 Praktiska Projekt: Bygg verkliga API-applikationer

> **2 omfattande projekt från beginner till expert**
>
> **Total tidsåtgång**: 20-30 timmar

---

## 📚 Innehåll

1. [Projekt 1: Väderapp med API-integration](#projekt-1-väderapp-med-api-integration) (Nivå 3-4)
2. [Projekt 2: Säker GraphQL E-handelsplattform](#projekt-2-säker-graphql-e-handelsplattform) (Nivå 5)

---

## ☀️ Projekt 1: Väderapp med API-integration

### 📋 Projektöversikt

**Nivå:** Nivå 3-4 (Intermediate till Advanced)

**Tidsåtgång:** 10-15 timmar

**Beskrivning:**
Bygg en fullständig väderapplikation med:
- Frontend (HTML/CSS/JavaScript eller React)
- Backend API (Node.js/Express)
- Integration med externa API:er
- Databas för favoritplatser
- Autentisering och användarhantering

**Teknologier:**
- **Frontend:** HTML, CSS, JavaScript (eller React)
- **Backend:** Node.js, Express
- **Databas:** MongoDB eller PostgreSQL
- **Externa API:er:** OpenWeatherMap, Geolocation API
- **Autentisering:** JWT
- **Deployment:** Heroku, Vercel, eller Netlify

---

### 🎯 Funktionskrav

#### MVP (Minimum Viable Product)
1. ✅ Sök väder efter stad
2. ✅ Visa aktuellt väder (temperatur, beskrivning, ikon)
3. ✅ Visa 5-dagars prognos
4. ✅ Responsiv design

#### Avancerade funktioner
5. ✅ Användarregistrering och inloggning (JWT)
6. ✅ Spara favoritplatser
7. ✅ Automatisk geolocation (hitta användarens position)
8. ✅ Väderkartor (radar, molntäcke)
9. ✅ Notifikationer för vädervarningar
10. ✅ Dark mode / Light mode

---

### 🏗️ Arkitektur

```
┌──────────────────────────────────────────────────────────┐
│                     FRONTEND                             │
│  (React eller Vanilla JavaScript)                        │
│                                                          │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐        │
│  │  Search    │  │  Current   │  │  Forecast  │        │
│  │  Component │  │  Weather   │  │  Component │        │
│  └────────────┘  └────────────┘  └────────────┘        │
└──────────────────┬───────────────────────────────────────┘
                   │
                   │ HTTP Requests (fetch/axios)
                   │
                   ↓
┌──────────────────────────────────────────────────────────┐
│                   BACKEND API                            │
│              (Node.js + Express)                         │
│                                                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │  Routes:                                        │    │
│  │  - POST /auth/register                          │    │
│  │  - POST /auth/login                             │    │
│  │  - GET  /weather/current?city=Stockholm         │    │
│  │  - GET  /weather/forecast?city=Stockholm        │    │
│  │  - GET  /favorites (protected)                  │    │
│  │  - POST /favorites (protected)                  │    │
│  └─────────────────────────────────────────────────┘    │
│                   │             │                        │
│                   │             │                        │
│          ┌────────▼─────┐  ┌───▼──────────┐            │
│          │   MongoDB    │  │ OpenWeather  │            │
│          │   (Users,    │  │     API      │            │
│          │  Favorites)  │  └──────────────┘            │
│          └──────────────┘                               │
└──────────────────────────────────────────────────────────┘
```

---

### 💻 Implementation

#### Steg 1: Setup Backend

**1.1 Initiera projekt**

```bash
mkdir weather-app
cd weather-app
mkdir backend frontend
cd backend

npm init -y
npm install express mongoose dotenv cors bcrypt jsonwebtoken axios
npm install --save-dev nodemon
```

**1.2 Projektstruktur**

```
backend/
├── .env
├── .gitignore
├── package.json
├── server.js
├── config/
│   └── database.js
├── models/
│   ├── User.js
│   └── Favorite.js
├── routes/
│   ├── auth.js
│   ├── weather.js
│   └── favorites.js
├── middleware/
│   └── auth.js
└── controllers/
    ├── authController.js
    ├── weatherController.js
    └── favoritesController.js
```

**1.3 Environment variables (.env)**

```bash
PORT=5000
MONGODB_URI=mongodb://localhost:27017/weather-app
JWT_SECRET=din_hemliga_nyckel_här_använd_lång_och_komplex
OPENWEATHER_API_KEY=din_openweathermap_api_nyckel
```

**1.4 Server setup (server.js)**

```javascript
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
require('dotenv').config();

const app = express();

// Middleware
app.use(cors());
app.use(express.json());

// Database connection
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
.then(() => console.log('MongoDB connected'))
.catch(err => console.error('MongoDB connection error:', err));

// Routes
app.use('/api/auth', require('./routes/auth'));
app.use('/api/weather', require('./routes/weather'));
app.use('/api/favorites', require('./routes/favorites'));

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({
    error: 'Something went wrong!',
    message: err.message
  });
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

#### Steg 2: Models

**2.1 User Model (models/User.js)**

```javascript
const mongoose = require('mongoose');
const bcrypt = require('bcrypt');

const userSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
    trim: true
  },
  email: {
    type: String,
    required: true,
    unique: true,
    lowercase: true,
    trim: true
  },
  password: {
    type: String,
    required: true,
    minlength: 8
  },
  favorites: [{
    type: mongoose.Schema.Types.ObjectId,
    ref: 'Favorite'
  }],
  createdAt: {
    type: Date,
    default: Date.now
  }
});

// Hash password before saving
userSchema.pre('save', async function(next) {
  if (!this.isModified('password')) return next();

  try {
    const salt = await bcrypt.genSalt(10);
    this.password = await bcrypt.hash(this.password, salt);
    next();
  } catch (error) {
    next(error);
  }
});

// Method to compare passwords
userSchema.methods.comparePassword = async function(candidatePassword) {
  return await bcrypt.compare(candidatePassword, this.password);
};

module.exports = mongoose.model('User', userSchema);
```

**2.2 Favorite Model (models/Favorite.js)**

```javascript
const mongoose = require('mongoose');

const favoriteSchema = new mongoose.Schema({
  user: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User',
    required: true
  },
  city: {
    type: String,
    required: true
  },
  country: {
    type: String,
    required: true
  },
  coordinates: {
    lat: Number,
    lon: Number
  },
  createdAt: {
    type: Date,
    default: Date.now
  }
});

// Prevent duplicate favorites
favoriteSchema.index({ user: 1, city: 1 }, { unique: true });

module.exports = mongoose.model('Favorite', favoriteSchema);
```

#### Steg 3: Authentication

**3.1 Auth Middleware (middleware/auth.js)**

```javascript
const jwt = require('jsonwebtoken');

module.exports = function(req, res, next) {
  // Get token from header
  const token = req.header('Authorization')?.replace('Bearer ', '');

  if (!token) {
    return res.status(401).json({
      error: 'No token, authorization denied'
    });
  }

  try {
    // Verify token
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = decoded.user;
    next();
  } catch (error) {
    res.status(401).json({
      error: 'Token is not valid'
    });
  }
};
```

**3.2 Auth Controller (controllers/authController.js)**

```javascript
const User = require('../models/User');
const jwt = require('jsonwebtoken');

// Generate JWT
const generateToken = (userId) => {
  return jwt.sign(
    { user: { id: userId } },
    process.env.JWT_SECRET,
    { expiresIn: '7d' }
  );
};

// Register user
exports.register = async (req, res) => {
  try {
    const { name, email, password } = req.body;

    // Check if user exists
    let user = await User.findOne({ email });
    if (user) {
      return res.status(400).json({
        error: 'User already exists'
      });
    }

    // Create user
    user = new User({
      name,
      email,
      password
    });

    await user.save();

    // Generate token
    const token = generateToken(user.id);

    res.status(201).json({
      token,
      user: {
        id: user.id,
        name: user.name,
        email: user.email
      }
    });

  } catch (error) {
    console.error(error);
    res.status(500).json({
      error: 'Server error'
    });
  }
};

// Login user
exports.login = async (req, res) => {
  try {
    const { email, password } = req.body;

    // Check if user exists
    const user = await User.findOne({ email });
    if (!user) {
      return res.status(400).json({
        error: 'Invalid credentials'
      });
    }

    // Validate password
    const isMatch = await user.comparePassword(password);
    if (!isMatch) {
      return res.status(400).json({
        error: 'Invalid credentials'
      });
    }

    // Generate token
    const token = generateToken(user.id);

    res.json({
      token,
      user: {
        id: user.id,
        name: user.name,
        email: user.email
      }
    });

  } catch (error) {
    console.error(error);
    res.status(500).json({
      error: 'Server error'
    });
  }
};
```

**3.3 Auth Routes (routes/auth.js)**

```javascript
const express = require('express');
const router = express.Router();
const { register, login } = require('../controllers/authController');
const { body, validationResult } = require('express-validator');

// Validation middleware
const validate = (req, res, next) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(422).json({ errors: errors.array() });
  }
  next();
};

// POST /api/auth/register
router.post('/register', [
  body('name').trim().notEmpty().withMessage('Name is required'),
  body('email').isEmail().withMessage('Valid email is required'),
  body('password')
    .isLength({ min: 8 })
    .withMessage('Password must be at least 8 characters'),
  validate
], register);

// POST /api/auth/login
router.post('/login', [
  body('email').isEmail().withMessage('Valid email is required'),
  body('password').notEmpty().withMessage('Password is required'),
  validate
], login);

module.exports = router;
```

#### Steg 4: Weather API Integration

**4.1 Weather Controller (controllers/weatherController.js)**

```javascript
const axios = require('axios');

const OPENWEATHER_BASE_URL = 'https://api.openweathermap.org/data/2.5';
const API_KEY = process.env.OPENWEATHER_API_KEY;

// Get current weather
exports.getCurrentWeather = async (req, res) => {
  try {
    const { city, lat, lon } = req.query;

    let url;
    if (city) {
      url = `${OPENWEATHER_BASE_URL}/weather?q=${city}&appid=${API_KEY}&units=metric&lang=sv`;
    } else if (lat && lon) {
      url = `${OPENWEATHER_BASE_URL}/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric&lang=sv`;
    } else {
      return res.status(400).json({
        error: 'City or coordinates required'
      });
    }

    const response = await axios.get(url);

    // Transform data
    const weather = {
      city: response.data.name,
      country: response.data.sys.country,
      temperature: response.data.main.temp,
      feelsLike: response.data.main.feels_like,
      humidity: response.data.main.humidity,
      pressure: response.data.main.pressure,
      description: response.data.weather[0].description,
      icon: response.data.weather[0].icon,
      windSpeed: response.data.wind.speed,
      clouds: response.data.clouds.all,
      coordinates: response.data.coord,
      timestamp: new Date()
    };

    res.json(weather);

  } catch (error) {
    if (error.response?.status === 404) {
      return res.status(404).json({
        error: 'City not found'
      });
    }

    console.error('Weather API error:', error);
    res.status(500).json({
      error: 'Failed to fetch weather data'
    });
  }
};

// Get 5-day forecast
exports.getForecast = async (req, res) => {
  try {
    const { city, lat, lon } = req.query;

    let url;
    if (city) {
      url = `${OPENWEATHER_BASE_URL}/forecast?q=${city}&appid=${API_KEY}&units=metric&lang=sv`;
    } else if (lat && lon) {
      url = `${OPENWEATHER_BASE_URL}/forecast?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric&lang=sv`;
    } else {
      return res.status(400).json({
        error: 'City or coordinates required'
      });
    }

    const response = await axios.get(url);

    // Transform and group by day
    const forecast = response.data.list.map(item => ({
      date: item.dt_txt,
      temperature: item.main.temp,
      description: item.weather[0].description,
      icon: item.weather[0].icon,
      humidity: item.main.humidity,
      windSpeed: item.wind.speed
    }));

    res.json({
      city: response.data.city.name,
      country: response.data.city.country,
      forecast
    });

  } catch (error) {
    if (error.response?.status === 404) {
      return res.status(404).json({
        error: 'City not found'
      });
    }

    console.error('Forecast API error:', error);
    res.status(500).json({
      error: 'Failed to fetch forecast data'
    });
  }
};
```

**4.2 Weather Routes (routes/weather.js)**

```javascript
const express = require('express');
const router = express.Router();
const {
  getCurrentWeather,
  getForecast
} = require('../controllers/weatherController');

// GET /api/weather/current?city=Stockholm
// GET /api/weather/current?lat=59.3293&lon=18.0686
router.get('/current', getCurrentWeather);

// GET /api/weather/forecast?city=Stockholm
router.get('/forecast', getForecast);

module.exports = router;
```

#### Steg 5: Favorites

**5.1 Favorites Controller (controllers/favoritesController.js)**

```javascript
const Favorite = require('../models/Favorite');
const User = require('../models/User');

// Get user's favorites
exports.getFavorites = async (req, res) => {
  try {
    const favorites = await Favorite.find({ user: req.user.id })
      .sort({ createdAt: -1 });

    res.json(favorites);
  } catch (error) {
    console.error(error);
    res.status(500).json({
      error: 'Server error'
    });
  }
};

// Add favorite
exports.addFavorite = async (req, res) => {
  try {
    const { city, country, coordinates } = req.body;

    // Check if already exists
    let favorite = await Favorite.findOne({
      user: req.user.id,
      city: city
    });

    if (favorite) {
      return res.status(400).json({
        error: 'City already in favorites'
      });
    }

    // Create favorite
    favorite = new Favorite({
      user: req.user.id,
      city,
      country,
      coordinates
    });

    await favorite.save();

    // Add to user's favorites array
    await User.findByIdAndUpdate(req.user.id, {
      $push: { favorites: favorite._id }
    });

    res.status(201).json(favorite);

  } catch (error) {
    console.error(error);
    res.status(500).json({
      error: 'Server error'
    });
  }
};

// Delete favorite
exports.deleteFavorite = async (req, res) => {
  try {
    const favorite = await Favorite.findOneAndDelete({
      _id: req.params.id,
      user: req.user.id
    });

    if (!favorite) {
      return res.status(404).json({
        error: 'Favorite not found'
      });
    }

    // Remove from user's favorites array
    await User.findByIdAndUpdate(req.user.id, {
      $pull: { favorites: favorite._id }
    });

    res.json({ message: 'Favorite deleted' });

  } catch (error) {
    console.error(error);
    res.status(500).json({
      error: 'Server error'
    });
  }
};
```

**5.2 Favorites Routes (routes/favorites.js)**

```javascript
const express = require('express');
const router = express.Router();
const auth = require('../middleware/auth');
const {
  getFavorites,
  addFavorite,
  deleteFavorite
} = require('../controllers/favoritesController');

// All routes require authentication
router.use(auth);

// GET /api/favorites
router.get('/', getFavorites);

// POST /api/favorites
router.post('/', addFavorite);

// DELETE /api/favorites/:id
router.delete('/:id', deleteFavorite);

module.exports = router;
```

#### Steg 6: Frontend

**6.1 Basic HTML/CSS/JS Frontend**

```html
<!-- frontend/index.html -->
<!DOCTYPE html>
<html lang="sv">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Väder App</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div class="container">
    <header>
      <h1>🌤️ Väder App</h1>
      <div id="auth-section">
        <button id="login-btn">Logga in</button>
        <button id="register-btn">Registrera</button>
      </div>
      <div id="user-section" class="hidden">
        <span id="user-name"></span>
        <button id="logout-btn">Logga ut</button>
      </div>
    </header>

    <main>
      <!-- Search -->
      <div class="search-container">
        <input
          type="text"
          id="city-input"
          placeholder="Sök efter stad..."
        />
        <button id="search-btn">Sök</button>
        <button id="location-btn">📍 Min position</button>
      </div>

      <!-- Current Weather -->
      <div id="current-weather" class="weather-card hidden">
        <h2 id="city-name"></h2>
        <div class="weather-main">
          <img id="weather-icon" src="" alt="Weather icon">
          <div class="temperature">
            <span id="temp"></span>°C
          </div>
        </div>
        <p id="description"></p>
        <div class="weather-details">
          <div>
            <span>Känns som:</span>
            <span id="feels-like"></span>°C
          </div>
          <div>
            <span>Luftfuktighet:</span>
            <span id="humidity"></span>%
          </div>
          <div>
            <span>Vind:</span>
            <span id="wind"></span> m/s
          </div>
        </div>
        <button id="add-favorite-btn">⭐ Lägg till favorit</button>
      </div>

      <!-- Forecast -->
      <div id="forecast" class="hidden">
        <h3>5-dagars prognos</h3>
        <div id="forecast-cards"></div>
      </div>

      <!-- Favorites -->
      <div id="favorites" class="hidden">
        <h3>Mina favoriter</h3>
        <div id="favorites-list"></div>
      </div>
    </main>
  </div>

  <!-- Modals -->
  <div id="login-modal" class="modal hidden">
    <div class="modal-content">
      <h2>Logga in</h2>
      <input type="email" id="login-email" placeholder="Email">
      <input type="password" id="login-password" placeholder="Lösenord">
      <button id="login-submit">Logga in</button>
      <button id="login-close">Stäng</button>
    </div>
  </div>

  <script src="app.js"></script>
</body>
</html>
```

**6.2 JavaScript (frontend/app.js)**

```javascript
const API_URL = 'http://localhost:5000/api';
let currentUser = null;
let currentCity = null;

// Initialize
document.addEventListener('DOMContentLoaded', () => {
  checkAuth();
  setupEventListeners();
});

// Check if user is logged in
function checkAuth() {
  const token = localStorage.getItem('token');
  if (token) {
    currentUser = JSON.parse(localStorage.getItem('user'));
    updateUI();
    loadFavorites();
  }
}

// Setup event listeners
function setupEventListeners() {
  document.getElementById('search-btn').addEventListener('click', searchWeather);
  document.getElementById('location-btn').addEventListener('click', getLocationWeather);
  document.getElementById('city-input').addEventListener('keypress', (e) => {
    if (e.key === 'Enter') searchWeather();
  });

  // Auth
  document.getElementById('login-btn').addEventListener('click', showLoginModal);
  document.getElementById('register-btn').addEventListener('click', showRegisterModal);
  document.getElementById('logout-btn').addEventListener('click', logout);

  // Favorites
  document.getElementById('add-favorite-btn').addEventListener('click', addFavorite);
}

// Search weather
async function searchWeather() {
  const city = document.getElementById('city-input').value.trim();
  if (!city) return;

  try {
    showLoading();

    const response = await fetch(`${API_URL}/weather/current?city=${city}`);
    if (!response.ok) throw new Error('City not found');

    const weather = await response.json();
    currentCity = weather;

    displayCurrentWeather(weather);
    loadForecast(city);

  } catch (error) {
    showError(error.message);
  }
}

// Get location weather
function getLocationWeather() {
  if (!navigator.geolocation) {
    showError('Geolocation not supported');
    return;
  }

  navigator.geolocation.getCurrentPosition(async (position) => {
    const { latitude, longitude } = position.coords;

    try {
      showLoading();

      const response = await fetch(
        `${API_URL}/weather/current?lat=${latitude}&lon=${longitude}`
      );
      const weather = await response.json();
      currentCity = weather;

      displayCurrentWeather(weather);
      loadForecast(null, latitude, longitude);

    } catch (error) {
      showError(error.message);
    }
  });
}

// Display current weather
function displayCurrentWeather(weather) {
  document.getElementById('city-name').textContent =
    `${weather.city}, ${weather.country}`;

  document.getElementById('temp').textContent =
    Math.round(weather.temperature);

  document.getElementById('description').textContent =
    weather.description;

  document.getElementById('feels-like').textContent =
    Math.round(weather.feelsLike);

  document.getElementById('humidity').textContent =
    weather.humidity;

  document.getElementById('wind').textContent =
    weather.windSpeed;

  document.getElementById('weather-icon').src =
    `https://openweathermap.org/img/wn/${weather.icon}@2x.png`;

  document.getElementById('current-weather').classList.remove('hidden');
}

// Load forecast
async function loadForecast(city, lat, lon) {
  try {
    let url = `${API_URL}/weather/forecast?`;
    if (city) {
      url += `city=${city}`;
    } else {
      url += `lat=${lat}&lon=${lon}`;
    }

    const response = await fetch(url);
    const data = await response.json();

    displayForecast(data.forecast);

  } catch (error) {
    console.error('Forecast error:', error);
  }
}

// Display forecast
function displayForecast(forecast) {
  const container = document.getElementById('forecast-cards');
  container.innerHTML = '';

  // Group by day (show one per day)
  const dailyForecasts = [];
  const seen = new Set();

  forecast.forEach(item => {
    const date = item.date.split(' ')[0];
    if (!seen.has(date)) {
      seen.add(date);
      dailyForecasts.push(item);
    }
  });

  dailyForecasts.slice(0, 5).forEach(item => {
    const card = document.createElement('div');
    card.className = 'forecast-card';
    card.innerHTML = `
      <p>${new Date(item.date).toLocaleDateString('sv-SE', { weekday: 'short' })}</p>
      <img src="https://openweathermap.org/img/wn/${item.icon}.png" alt="Weather">
      <p>${Math.round(item.temperature)}°C</p>
      <p>${item.description}</p>
    `;
    container.appendChild(card);
  });

  document.getElementById('forecast').classList.remove('hidden');
}

// Add to favorites
async function addFavorite() {
  if (!currentUser) {
    showError('Please login first');
    return;
  }

  if (!currentCity) return;

  try {
    const token = localStorage.getItem('token');

    const response = await fetch(`${API_URL}/favorites`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify({
        city: currentCity.city,
        country: currentCity.country,
        coordinates: currentCity.coordinates
      })
    });

    if (!response.ok) throw new Error('Failed to add favorite');

    showSuccess('Added to favorites');
    loadFavorites();

  } catch (error) {
    showError(error.message);
  }
}

// Load favorites
async function loadFavorites() {
  if (!currentUser) return;

  try {
    const token = localStorage.getItem('token');

    const response = await fetch(`${API_URL}/favorites`, {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    });

    const favorites = await response.json();
    displayFavorites(favorites);

  } catch (error) {
    console.error('Load favorites error:', error);
  }
}

// Display favorites
function displayFavorites(favorites) {
  const container = document.getElementById('favorites-list');
  container.innerHTML = '';

  favorites.forEach(fav => {
    const item = document.createElement('div');
    item.className = 'favorite-item';
    item.innerHTML = `
      <span>${fav.city}, ${fav.country}</span>
      <button onclick="loadFavoriteWeather('${fav.city}')">Visa</button>
      <button onclick="deleteFavorite('${fav._id}')">❌</button>
    `;
    container.appendChild(item);
  });

  if (favorites.length > 0) {
    document.getElementById('favorites').classList.remove('hidden');
  }
}

// Helper functions (showError, showSuccess, updateUI, etc.)
function showLoading() {
  // Implement loading spinner
}

function showError(message) {
  alert('Error: ' + message);
}

function showSuccess(message) {
  alert(message);
}

function updateUI() {
  if (currentUser) {
    document.getElementById('auth-section').classList.add('hidden');
    document.getElementById('user-section').classList.remove('hidden');
    document.getElementById('user-name').textContent = currentUser.name;
  } else {
    document.getElementById('auth-section').classList.remove('hidden');
    document.getElementById('user-section').classList.add('hidden');
  }
}
```

---

### 🧪 Testning

```bash
npm install --save-dev jest supertest

# package.json
"scripts": {
  "test": "jest --watchAll"
}
```

**Test exempel (tests/auth.test.js):**

```javascript
const request = require('supertest');
const app = require('../server');
const User = require('../models/User');

describe('Auth API', () => {
  beforeEach(async () => {
    await User.deleteMany({});
  });

  test('Register new user', async () => {
    const response = await request(app)
      .post('/api/auth/register')
      .send({
        name: 'Test User',
        email: 'test@example.com',
        password: 'password123'
      });

    expect(response.statusCode).toBe(201);
    expect(response.body).toHaveProperty('token');
    expect(response.body.user).toHaveProperty('email', 'test@example.com');
  });

  test('Login with valid credentials', async () => {
    // First register
    await request(app)
      .post('/api/auth/register')
      .send({
        name: 'Test User',
        email: 'test@example.com',
        password: 'password123'
      });

    // Then login
    const response = await request(app)
      .post('/api/auth/login')
      .send({
        email: 'test@example.com',
        password: 'password123'
      });

    expect(response.statusCode).toBe(200);
    expect(response.body).toHaveProperty('token');
  });

  test('Login with invalid credentials', async () => {
    const response = await request(app)
      .post('/api/auth/login')
      .send({
        email: 'wrong@example.com',
        password: 'wrongpassword'
      });

    expect(response.statusCode).toBe(400);
    expect(response.body).toHaveProperty('error');
  });
});
```

---

### 📦 Deployment

**Heroku:**

```bash
# Install Heroku CLI
# heroku login

# Create app
heroku create weather-app-yourname

# Add MongoDB (Atlas)
# Set environment variables
heroku config:set JWT_SECRET=your_secret
heroku config:set OPENWEATHER_API_KEY=your_key

# Deploy
git push heroku main
```

**Vercel (Frontend):**

```bash
npm install -g vercel
vercel
```

---

### ✅ Checklista

- [ ] Backend API körs lokalt
- [ ] MongoDB connection fungerar
- [ ] Kan registrera och logga in
- [ ] Kan söka väder efter stad
- [ ] Kan hämta väder för min position
- [ ] Kan se 5-dagars prognos
- [ ] Kan lägga till/ta bort favoriter
- [ ] Frontend visar väderdata korrekt
- [ ] Error handling fungerar
- [ ] Responsiv design
- [ ] Tests skrivna och kör
- [ ] Deployad till produktion

---

## 🛒 Projekt 2: Säker GraphQL E-handelsplattform

### 📋 Projektöversikt

**Nivå:** Nivå 5 (Expert)

**Tidsåtgång:** 15-20 timmar

**Beskrivning:**
Bygg en fullständig e-handelsplattform med:
- GraphQL API (Apollo Server)
- Serverless backend (AWS Lambda eller Vercel)
- Produktkatalog med search och filter
- Kundvagn och checkout
- JWT + OAuth 2.0 autentisering
- Betalningsintegration (Stripe)
- Admin-panel
- Real-time uppdateringar (WebSocket subscriptions)

**Teknologier:**
- **GraphQL:** Apollo Server, Apollo Client
- **Backend:** Node.js, TypeScript
- **Databas:** PostgreSQL (Prisma ORM)
- **Auth:** JWT, OAuth 2.0 (Google)
- **Payment:** Stripe API
- **Frontend:** React, Apollo Client
- **Real-time:** GraphQL Subscriptions
- **Deployment:** Vercel (Serverless)

---

### 🎯 Funktionskrav

#### MVP
1. ✅ Produktkatalog (lista, sök, filter)
2. ✅ Produktdetaljer
3. ✅ Kundvagn
4. ✅ Checkout med Stripe
5. ✅ Användarregistrering (email/password)
6. ✅ Orderhistorik

#### Avancerade funktioner
7. ✅ OAuth 2.0 (Google login)
8. ✅ Admin-panel (CRUD produkter)
9. ✅ Real-time inventory updates
10. ✅ Product reviews och ratings
11. ✅ Wishlist
12. ✅ Search med filter (pris, kategori, rating)
13. ✅ GraphQL Subscriptions för cart updates
14. ✅ Role-based access control (RBAC)

---

### 🏗️ GraphQL Schema

```graphql
# schema.graphql

scalar DateTime
scalar JSON

# ============ TYPES ============

type User {
  id: ID!
  email: String!
  name: String!
  role: Role!
  orders: [Order!]!
  cart: Cart
  wishlist: [Product!]!
  createdAt: DateTime!
}

enum Role {
  USER
  ADMIN
  SUPER_ADMIN
}

type Product {
  id: ID!
  name: String!
  description: String!
  price: Float!
  category: Category!
  images: [String!]!
  stock: Int!
  reviews: [Review!]!
  averageRating: Float
  createdAt: DateTime!
  updatedAt: DateTime!
}

type Category {
  id: ID!
  name: String!
  slug: String!
  products: [Product!]!
}

type Cart {
  id: ID!
  user: User!
  items: [CartItem!]!
  total: Float!
  updatedAt: DateTime!
}

type CartItem {
  id: ID!
  product: Product!
  quantity: Int!
  subtotal: Float!
}

type Order {
  id: ID!
  user: User!
  items: [OrderItem!]!
  total: Float!
  status: OrderStatus!
  paymentIntent: String
  shippingAddress: Address!
  createdAt: DateTime!
}

enum OrderStatus {
  PENDING
  PAID
  SHIPPED
  DELIVERED
  CANCELLED
}

type OrderItem {
  id: ID!
  product: Product!
  quantity: Int!
  price: Float!  # Price at time of order
}

type Address {
  street: String!
  city: String!
  postalCode: String!
  country: String!
}

type Review {
  id: ID!
  product: Product!
  user: User!
  rating: Int!  # 1-5
  comment: String
  createdAt: DateTime!
}

type AuthPayload {
  token: String!
  user: User!
}

# ============ QUERIES ============

type Query {
  # Products
  products(
    search: String
    category: String
    minPrice: Float
    maxPrice: Float
    minRating: Float
    limit: Int
    offset: Int
  ): ProductsResponse!

  product(id: ID!): Product

  # Categories
  categories: [Category!]!

  # User
  me: User

  # Cart
  cart: Cart

  # Orders
  myOrders: [Order!]!
  order(id: ID!): Order

  # Admin
  allOrders(status: OrderStatus): [Order!]! @auth(role: ADMIN)
  stats: StatsResponse! @auth(role: ADMIN)
}

type ProductsResponse {
  products: [Product!]!
  total: Int!
  hasMore: Boolean!
}

type StatsResponse {
  totalRevenue: Float!
  totalOrders: Int!
  totalProducts: Int!
  totalUsers: Int!
}

# ============ MUTATIONS ============

type Mutation {
  # Auth
  register(input: RegisterInput!): AuthPayload!
  login(input: LoginInput!): AuthPayload!
  loginWithGoogle(token: String!): AuthPayload!

  # Cart
  addToCart(productId: ID!, quantity: Int!): Cart!
  updateCartItem(itemId: ID!, quantity: Int!): Cart!
  removeFromCart(itemId: ID!): Cart!
  clearCart: Cart!

  # Orders
  createOrder(input: CreateOrderInput!): Order!
  cancelOrder(orderId: ID!): Order!

  # Reviews
  createReview(input: CreateReviewInput!): Review!

  # Wishlist
  addToWishlist(productId: ID!): User!
  removeFromWishlist(productId: ID!): User!

  # Admin
  createProduct(input: CreateProductInput!): Product! @auth(role: ADMIN)
  updateProduct(id: ID!, input: UpdateProductInput!): Product! @auth(role: ADMIN)
  deleteProduct(id: ID!): Boolean! @auth(role: ADMIN)
  updateOrderStatus(orderId: ID!, status: OrderStatus!): Order! @auth(role: ADMIN)
}

# ============ SUBSCRIPTIONS ============

type Subscription {
  cartUpdated(userId: ID!): Cart!
  productStockUpdated(productId: ID!): Product!
  orderStatusUpdated(userId: ID!): Order!
}

# ============ INPUTS ============

input RegisterInput {
  email: String!
  password: String!
  name: String!
}

input LoginInput {
  email: String!
  password: String!
}

input CreateOrderInput {
  shippingAddress: AddressInput!
  paymentMethodId: String!  # Stripe payment method
}

input AddressInput {
  street: String!
  city: String!
  postalCode: String!
  country: String!
}

input CreateReviewInput {
  productId: ID!
  rating: Int!  # 1-5
  comment: String
}

input CreateProductInput {
  name: String!
  description: String!
  price: Float!
  categoryId: ID!
  images: [String!]!
  stock: Int!
}

input UpdateProductInput {
  name: String
  description: String
  price: Float
  categoryId: ID
  images: [String!]
  stock: Int
}

# ============ DIRECTIVES ============

directive @auth(role: Role) on FIELD_DEFINITION
```

---

### 💻 Implementation Guide

*(Av utrymmesskäl, här är high-level struktur. Fullständig kod finns i GitHub-repo)*

**Projektstruktur:**

```
ecommerce-graphql/
├── backend/
│   ├── prisma/
│   │   └── schema.prisma
│   ├── src/
│   │   ├── resolvers/
│   │   │   ├── user.ts
│   │   │   ├── product.ts
│   │   │   ├── cart.ts
│   │   │   └── order.ts
│   │   ├── directives/
│   │   │   └── auth.ts
│   │   ├── utils/
│   │   │   ├── auth.ts
│   │   │   └── stripe.ts
│   │   ├── schema.graphql
│   │   └── index.ts
│   └── package.json
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── graphql/
│   │   ├── apollo.ts
│   │   └── App.tsx
│   └── package.json
└── README.md
```

**Viktiga delar att implementera:**

1. **Prisma Schema (Databas)**
2. **GraphQL Resolvers**
3. **Authentication (JWT + OAuth 2.0)**
4. **Stripe Integration**
5. **Real-time Subscriptions**
6. **Frontend (React + Apollo Client)**

---

### ✅ Projekt 2 Checklista

- [ ] GraphQL schema definierat
- [ ] Prisma setup med PostgreSQL
- [ ] Auth resolver (register, login, OAuth)
- [ ] Product resolvers (CRUD, search, filter)
- [ ] Cart resolver med subscriptions
- [ ] Order resolver med Stripe integration
- [ ] RBAC implementation (@auth directive)
- [ ] Frontend: Product katalog
- [ ] Frontend: Cart och checkout
- [ ] Frontend: Admin panel
- [ ] Real-time updates fungerar
- [ ] Deployment till Vercel

---

## 🎓 Sammanfattning

**Du har nu:**
- ✅ Byggt en fullständig REST API-app (Projekt 1)
- ✅ Byggt en fullständig GraphQL-app (Projekt 2)
- ✅ Lärt dig autentisering (JWT, OAuth 2.0)
- ✅ Integrerat externa API:er (OpenWeatherMap, Stripe)
- ✅ Implementerat real-time features
- ✅ Deployat till produktion
- ✅ Skrivit tester

**Nästa steg:**
1. Visa dina projekt i din portfolio
2. Bidra till open source-projekt
3. Bygg egna idéer med API:er
4. Ansök till jobb som API-utvecklare!

---

[🏠 Tillbaka till huvudindex](./README.md) | [📝 Gå till Övningar](./övningar.md)
