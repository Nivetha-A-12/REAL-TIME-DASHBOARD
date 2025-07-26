# REAL-TIME-DASHBOARD

COMPANY NAME : CODTECH IT SOLUTIONS PVT.LTD

NAME : NIVETHA A

INTERN ID : CT06DG1411

DOMAIN : POWER BI

DURATION : 6 WEEKS

MENTOR: NEELA SANTHOSH

TASK DESCRIPTION:

As part of Codtech Intern Task 3, I developed a real-time sensor data simulation system and connected it to a Power BI dashboard to visualize live updates. The core objective was to simulate streaming IoT sensor data via a custom-built API and integrate it with Power BI for real-time monitoring and analysis. To complete this task, I used a combination of:
Python (specifically the Flask web framework) to create the API simulator
Power BI Desktop to visualize the incoming data
JSON as the data exchange format between the API and Power BI
Random and datetime modules to simulate real-world sensor conditions
This task perfectly combined backend simulation with frontend analytics, providing end-to-end exposure to real-time data processing.

I started by creating a Python script using Flask to simulate real-time data. The API served at http://localhost:5000/data and returned a JSON array containing sensor readings.I used Flask’s built-in development server and added a thread to automatically open the browser to the /data endpoint. This made it easy to validate and test the API response. The server continuously served fresh data every time it was queried, mimicking the behavior of live IoT sensors. Once the API was up and running, I moved to Power BI Desktop. I used the Web connector to connect to the API URL (http://localhost:5000/data) and import the JSON response. Power BI flattened the nested JSON structure, allowing me to load and transform the fields into a tabular format using Power Query Editor. I converted timestamps to proper datetime types and ensured numerical columns like temperature and humidity were in the correct format. Although Power BI Desktop does not support true real-time streaming natively, I set up manual and interval refreshes to simulate near-real-time updates from the API. Every refresh pulled new simulated data from the backend.


OUTPUT:
<img width="1376" height="766" alt="Image" src="https://github.com/user-attachments/assets/429a880c-0216-49f9-bed7-e72dc559e519" />
