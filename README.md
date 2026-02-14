<p align="center">
  <img src="./img.png" alt="Project Banner" width="100%">
</p>

# PERIODCARE🎯

## Basic Details

### Team Name: SheBugs

### Team Members
- Member 1: Fathimath Shirin Sana C A - LBS COLLEGE OF ENGINEERING KASARAGOD
- Member 2: Ezana T P - LBS COLLEGE OF ENGINEERING KASARAGOD

### Hosted Project Link
https://periodcare-epg2.vercel.app/

### Project Description
PeriodCare is a web-based menstrual health assistant developed using Flask and Python. It predicts upcoming period dates and ovulation cycles, provides personalized phase-based health tips, tracks symptoms with guided advice, manages essential product stock through a checklist system, and includes a structured full-day planner for period days.


### The Problem statement
Many students and young women face difficulty in accurately predicting their menstrual cycle, managing period symptoms, and staying prepared with essential products. Most existing applications are either complex, paid, or require personal data and login access.
There is a need for a simple, lightweight, privacy-friendly web application that helps users understand their menstrual cycle, manage symptoms, and plan their daily routine effectively.

### The Solution
PeriodCare is a simple, lightweight, and privacy-friendly web application developed using Flask and Python to assist users in understanding and managing their menstrual health effectively.
The system works by allowing users to enter their last period date and average cycle length. Based on this input, the application calculates and predicts:
The next expected period date
The estimated ovulation date
The fertile window range
The current menstrual phase
Beyond prediction, PeriodCare enhances user support by providing phase-based health guidance. Depending on the calculated cycle phase (Period, Follicular, Ovulation, or Luteal), the system displays personalized health tips to encourage better physical and emotional well-being.
To further support users, the application includes a symptom tracking module. Users can select common symptoms such as cramps, mood swings, headache, or bloating. The system then generates specific care suggestions and practical self-care instructions tailored to the selected symptoms.
Additionally, PeriodCare provides a Product Stock Checklist feature that helps users ensure they are prepared with essential menstrual products. If any required item is missing, the system alerts the user, promoting better preparedness.
The application also includes a Full-Day Period Planner, which offers a structured daily routine for period days. This planner suggests rest periods, hydration reminders, light activity guidance, and self-care recommendations to help users manage their day comfortably and efficiently.
Overall, PeriodCare acts as a digital menstrual companion that combines prediction, health guidance, symptom management, preparedness tracking, and daily planning — all within a simple and easy-to-use web interface.

## Technical Details

### Technologies/Components Used

**For Software:**
- Languages used: Python
- Frameworks used: flask
- frontend-html,css 
- Tools used: VS Code, Git,


## Features

List the key features of your project:
- Feature 1: Menstrual Cycle Prediction – Predicts the next period date based on the user’s last period date and cycle length.
- Feature 2: Ovulation & Fertile Window Calculation – Calculates ovulation day and displays the fertile window range.
- Feature 3: Current Phase Detection – Identifies the current menstrual phase (Period, Follicular, Ovulation, or Luteal).
- Feature 4:Phase-Based Health Tips – Provides personalized care suggestions based on the current cycle phase 
- feature 5:Symptom Tracker – Allows users to select symptoms and receive tailored self-care tips and instructions
- feature 6:Product Stock Checklist – Helps users check essential menstrual products and alerts if any item is missing.
- feature 7:Full-Day Period Planner – Offers a structured daily plan with rest, hydration, and self-care guidance.
- feature 8: User-Friendly Interface – Clean, simple, and beginner-friendly web design.


---

## Implementation

### For Software:
Any modern web browser (Chrome, Edge, Firefox, etc.)
Internet connection (for Supabase database)
#### Installation
bash
pip install flask
git clone https://github.com/your-username/PeriodCare.git
cd PeriodCare



#### Run
bash
python app.py


---

## Project Documentation

### For Software:

#### Screenshots (Add at least 3)
<img width="1905" height="911" alt="Screenshot 2026-02-14 200426" src="https://github.com/user-attachments/assets/179d3cb9-f198-4188-82a5-c1e5daec49df" />

This screenshot shows the main interface of PeriodCare. Users can enter their last period date and cycle length to predict upcoming periods and ovulation cycles. The dashboard also provides quick navigation links to additional features including Product Stock Checklist, Symptom Tracker, and Full Day Planner.

<img width="1239" height="898" alt="Screenshot 2026-02-14 200616" src="https://github.com/user-attachments/assets/50c0ee20-8e60-4849-b567-e9404110b23d" />

This screenshot displays the prediction results after entering the last period date and cycle length. The system calculates the next period date, ovulation date, and fertile window. It also identifies the current menstrual phase and provides a personalized health tip based on the phase.

<img width="795" height="639" alt="Screenshot 2026-02-14 200634" src="https://github.com/user-attachments/assets/411c3435-bfd4-45cf-a426-5be7fe7e5c87" />
This screenshot shows the Product Stock Checklist feature of PeriodCare. Users can select available menstrual essentials such as sanitary pads, tampons, pain relief tablets, herbal tea, heating pad, and period panties. The system checks for missing items and alerts users to ensure they are prepared in advance.

<img width="660" height="439" alt="Screenshot 2026-02-14 200737" src="https://github.com/user-attachments/assets/9de72a76-0e40-47ba-b9e5-e86b81a54f39" />
This screenshot shows the Today's Symptoms page of PeriodCare. Users can select symptoms such as cramps, mood swings, headache, or bloating. After clicking “Get Tips,” the system provides personalized self-care suggestions to help manage the selected symptoms.

<img width="831" height="810" alt="Screenshot 2026-02-14 200752" src="https://github.com/user-attachments/assets/56a3ba6e-2e94-480f-b632-10601aec8e4d" />
This screenshot displays the symptom selection and personalized care tips feature of PeriodCare. After selecting specific symptoms such as cramps or headache, the system generates tailored self-care advice including home remedies, hydration tips, and lifestyle suggestions to help manage discomfort effectively.

<img width="908" height="900" alt="Screenshot 2026-02-14 200818" src="https://github.com/user-attachments/assets/7b6721b2-6fe1-464f-b8d6-2b3136114a0f" />
This screenshot shows the Full Day Period Planner feature of PeriodCare. It provides a structured daily self-care plan divided into Morning, Afternoon, and Evening sections. Each section includes simple health recommendations such as hydration, light exercise, rest, and relaxation techniques to help manage period days comfortably.

#### Diagrams

**System Architecture:**

![WhatsApp Image 2026-02-14 at 9 07 40 AM](https://github.com/user-attachments/assets/c210a14a-02f0-4936-b13f-c0ba43ff734e)
PeriodCare follows a simple client-server architecture:
Client Layer (Frontend)
Built using HTML and CSS
Collects user inputs through forms
Displays prediction results and care suggestions
Application Layer (Flask Backend)
Handles routing (/, /symptoms, /stock, /planner)
Processes menstrual cycle calculations
Generates phase-based tips
Checks product availability
Returns rendered templates
Logic Layer (Business Logic)
Date calculations using datetime
Conditional logic for phase detection
Dictionary mapping for symptom advice
List comparison for stock validation
Data Handling
No database used
Data processed temporarily (session-based)
Privacy-friendly (no storage)
🎯 Tech Stack Interaction
Browser → sends form data
Flask → processes request
Python → performs calculations
HTML Templates → render output
Browser → displays results

**Application Workflow:**
![WhatsApp Image 2026-02-14 at 9 09 33 AM](https://github.com/user-attachments/assets/d2275225-0586-4dd2-98ca-3616b6e3c515)

PeriodCare follows a simple and user-friendly workflow:
User Input Stage
The user enters the last menstrual date and average cycle length.
The user clicks the Predict button.
Backend Processing
The Flask server receives the form data.
Python’s datetime module calculates:
Next period date
Ovulation date
Fertile window
The system determines the current menstrual phase.
A personalized health tip is generated based on the detected phase.
Result Display
The calculated results are rendered using HTML templates.
The prediction results are shown in a styled output card.
Additional Feature Navigation The user can navigate to:
Symptoms Page → Select symptoms and receive care tips.
Stock Checklist Page → Check essential period products.
Full Day Planner Page → View structured morning, afternoon, and evening care plan.
User Experience
No data is stored permanently.
All processing is done instantly on the server.
The interface remains simple and easy to use.


---

### For Hardware:

#### Schematic & Circuit

![Circuit](Add your circuit diagram here)
*Add caption explaining connections*

![Schematic](Add your schematic diagram here)
*Add caption explaining the schematic*

project demo video

