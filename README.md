# personal-healthcare-assistant
Project Overview

The Personal Healthcare Assistant is an interactive web application that provides real-time healthcare recommendations for:

Pregnant women (diet, supplements, next checkup)

Patients with conditions like diabetes or tumors (medications, diet, exercise)

The application features dynamic charts, a searchable history, and a responsive web interface, all without requiring Node.js.

Features
1️⃣ Pregnant Recommendations

Input: Trimester (1, 2, or 3)

Output: Diet, Supplements, Next Checkup

Visualization: Pie chart showing diet composition

Example:

{
  "diet": "Leafy Greens, Whole Grains",
  "supplements": "Iron, Folic Acid",
  "next_checkup": "2025-09-15"
}

2️⃣ Patient Recommendations

Input: Condition (e.g., diabetes, tumor)

Output: Medications, Diet, Exercise

Visualization: Pie chart for diet composition or other metrics

Example:

{
  "medications": "Metformin, Insulin",
  "diet": "Low sugar, High fiber",
  "exercise": "30 min walk"
}

3️⃣ History & Search

Stores all user submissions

Searchable and filterable by trimester, condition, or result keywords

Table updates dynamically with new submissions

4️⃣ Charts & Visuals

Pie charts for diet composition

Can be extended for medications or exercise visualization

Dynamic updates based on latest recommendations
