🛒 Supermarket Sales Dashboard

An interactive data analytics dashboard built with Python and Streamlit, designed to analyze and visualize sales performance across cities, products, and customer segments. This project transforms transactional data into actionable insights for business decision-making.

📌 Objectives
- Explore sales trends across cities and months
- Analyze customer behavior by type, gender, and payment method
- Identify top-performing product categories
- Enable filtered data export for custom insights

🧠 Key Features

🔍 Filters (Sidebar)
- Select City, Customer Type, and Product Line
- Instantly updates all charts and metrics

📈 Metrics & Visuals
💰 Total Sales – Displays overall sales within selected filters
⭐ Average Rating – Customer satisfaction by average rating
💼 Gross Income – Total gross income from sales
📦 Sales by Product Line – Horizontal bar chart showing product performance
📆 Monthly Sales Trend – Line chart showing sales by month
🎯 Rating Distribution – Boxplot comparing customer ratings by type
💳 Payment Breakdown – Pie chart showing usage of payment methods

📥 Download
- Filtered dataset can be downloaded as a .csv file directly from the dashboard

📁 Project Structure
supermarket-sales-dashboard/
├── app.py                        # Main Streamlit dashboard
├── cleaned_supermarket_sales.csv
├── city_sales_summary.csv        # (Optional summary export)
├── requirements.txt              # Project dependencies
├── README.md
└── plot_screenshots/             # (Optional folder for visual portfolio)

🛠️ Tech Stack
- Python: pandas, matplotlib, seaborn
- Streamlit: for UI and interactivity
- VS Code: development environment
- Optional: Canva/PowerPoint for presentation visuals

🚀 How to Run This Project
1. Clone this repository:
git clone https://github.com/your-username/supermarket-sales-dashboard.git
cd supermarket-sales-dashboard

2. Create virtual environment:
python -m venv env
env\Scripts\activate      # Windows
or
source env/bin/activate   # macOS/Linux

3. Install dependencies:
pip install -r requirements.txt

4. Run the Streamlit app:
streamlit run app.py

Then open http://localhost:8501 in your browser.

📸 Dashboard Preview (Optional)
(Add screenshots of your visuals in /plot_screenshots or paste image links here)

📊 Summary of Insights
- Yangon had the highest total sales among the three cities
- Health and beauty was the top-performing product line
- March 2019 was the peak sales month
- Members gave slightly higher ratings than normal customers
- E-wallet was the most commonly used payment method

💡 Potential Enhancements
- Add multi-page layout using Streamlit tabs
- Integrate external databases or live data
- Deploy online via Streamlit Cloud or Heroku
- Include machine learning for customer segmentation or forecasting

📬 Contact
Made with 💙 by Abdul Mukmin

📧 Email: mukmin020301@gmail.com
🔗 LinkedIn: https://www.linkedin.com/in/abdul-mukmin-b3576023b/
🐙 GitHub: https://github.com/Mukmin020301
