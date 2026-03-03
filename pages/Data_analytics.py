import streamlit as st

st.set_page_config(
    page_title="Data Analytics Mastery Program", 
    page_icon="📊",
    layout="wide"
)

# --- Custom CSS for Data Analytics Branding ---
st.markdown("""
<style>
    .da-header {
        background: linear-gradient(90deg, #FF8C00 0%, #FFD700 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .da-header h1 {
        color: #2C3E50;
        text-shadow: 1px 1px 2px #FFFFFF;
    }
    .highlight-box {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #FF8C00;
    }
    .module-card {
        background-color: white;
        padding: 1.2rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
        border: 1px solid #e0e0e0;
        transition: transform 0.2s;
    }
    .module-card:hover {
        transform: scale(1.02);
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        border-color: #FF8C00;
    }
    .career-badge {
        background-color: #FF8C00;
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-weight: bold;
        display: inline-block;
    }
    .sql-box {
        background-color: #1e1e1e;
        color: #FFD700;
        padding: 0.5rem;
        border-radius: 5px;
        font-family: 'Courier New', monospace;
        border-left: 3px solid #FF8C00;
    }
    .project-badge {
        background-color: #2C3E50;
        color: #FFD700;
        padding: 0.2rem 0.5rem;
        border-radius: 5px;
        font-size: 0.8rem;
    }
    .tool-tag {
        background-color: #FFD700;
        color: #2C3E50;
        padding: 0.2rem 0.5rem;
        border-radius: 15px;
        font-size: 0.8rem;
        display: inline-block;
        margin: 0.2rem;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- Header Section ---
st.markdown("""
<div class="da-header">
    <h1>📊 Data Analytics Mastery Program</h1>
    <h3>Complete Data Analyst Journey | Excel • SQL • Python • Power BI • Tableau</h3>
    <p style="font-size: 1.2rem;">Become a Job-Ready Data Analyst in 4 Months</p>
</div>
""", unsafe_allow_html=True)

# --- Quick Stats ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Duration", "4 Months", "Weekend/Hybrid")
with col2:
    st.metric("Level", "Beginner to Pro", "No Prior Experience Needed")
with col3:
    st.metric("Projects", "8 Analytics Projects", "Portfolio Ready")
with col4:
    st.metric("Fee", "₹35,000", "EMI Available")

st.markdown("---")

# --- Why Data Analytics? Section ---
st.markdown("## 🎯 Why Data Analytics? The Most In-Demand Skill")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="highlight-box">
        <h4>📈 Career Opportunities</h4>
        <ul>
            <li><strong>Data Analyst</strong> - ₹4-10 LPA</li>
            <li><strong>Business Analyst</strong> - ₹5-12 LPA</li>
            <li><strong>BI Analyst</strong> - ₹5-11 LPA</li>
            <li><strong>Marketing Analyst</strong> - ₹4-9 LPA</li>
            <li><strong>Financial Analyst</strong> - ₹4-10 LPA</li>
            <li><strong>Operations Analyst</strong> - ₹4-8 LPA</li>
            <li><strong>Healthcare Analyst</strong> - ₹4-9 LPA</li>
            <li><strong>Supply Chain Analyst</strong> - ₹4-9 LPA</li>
        </ul>
        <p><span class="career-badge">🔥 2.5 Lakh+ Data Analyst Jobs in India</span></p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="highlight-box">
        <h4>🏢 Top Hiring Companies</h4>
        <ul>
            <li>Amazon • Flipkart • Google • Meta</li>
            <li>Deloitte • EY • KPMG • PwC</li>
            <li>JPMorgan • Goldman Sachs • Citi</li>
            <li>Tata • Reliance • Infosys • Wipro</li>
            <li>Zomato • Swiggy • Ola • Uber</li>
            <li>Myntra • Nykaa • PharmEasy</li>
            <li>And 10,000+ more companies</li>
        </ul>
        <p><span class="career-badge">🎯 100% Placement Assistance</span></p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- Complete Data Analytics Curriculum ---
st.markdown("## 📚 Complete Data Analytics Curriculum")
st.markdown("### Structured Learning Path - From Zero to Data Analyst")

# Create tabs for different domains
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "📊 Foundations", 
    "📗 Excel", 
    "🗄️ SQL", 
    "🐍 Python", 
    "📈 Power BI", 
    "📉 Tableau", 
    "🚀 Capstone"
])

with tab1:
    st.markdown("### Module 01: Analytics Foundations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>📌 Introduction to Data Analytics</h4>
            <ul>
                <li>What is Data Analytics?</li>
                <li>Data Analyst vs Data Scientist</li>
                <li>Types of Analytics: Descriptive, Diagnostic, Predictive, Prescriptive</li>
                <li>Data Analytics Lifecycle</li>
                <li>Industry Applications & Use Cases</li>
                <li>Day in Life of a Data Analyst</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📊 Types of Data</h4>
            <ul>
                <li>Structured vs Unstructured Data</li>
                <li>Numerical Data (Discrete, Continuous)</li>
                <li>Categorical Data (Nominal, Ordinal)</li>
                <li>Time Series Data</li>
                <li>Cross-Sectional vs Panel Data</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>🔧 Analytics Tools Overview</h4>
            <ul>
                <li>Excel for Analysis</li>
                <li>SQL for Databases</li>
                <li>Python for Advanced Analytics</li>
                <li>Power BI for Dashboards</li>
                <li>Tableau for Visualization</li>
                <li>When to Use Which Tool</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📈 Analytics Framework</h4>
            <ul>
                <li>Problem Definition</li>
                <li>Data Collection</li>
                <li>Data Cleaning</li>
                <li>Data Analysis</li>
                <li>Insights & Recommendations</li>
                <li>Storytelling with Data</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.markdown("### Module 02: Excel for Data Analytics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>📗 Excel Fundamentals</h4>
            <ul>
                <li>Excel Interface & Navigation</li>
                <li>Data Entry & Formatting</li>
                <li>Cell Referencing (Relative, Absolute, Mixed)</li>
                <li>Named Ranges</li>
                <li>Keyboard Shortcuts Mastery</li>
                <li>Templates & Themes</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>🧮 Essential Formulas</h4>
            <ul>
                <li>SUM, AVERAGE, COUNT, COUNTA</li>
                <li>MAX, MIN, LARGE, SMALL</li>
                <li>IF, Nested IF, IFS</li>
                <li>AND, OR, NOT</li>
                <li>SUMIF, COUNTIF, AVERAGEIF</li>
                <li>SUMIFS, COUNTIFS, AVERAGEIFS</li>
            </ul>
            <div class="sql-box">
                =SUMIFS(Sales, Region, "West", Month, "Jan")<br>
                =IF(A2>100, "High", "Low")
            </div>
        </div>
        
        <div class="module-card">
            <h4>🔍 Lookup Functions</h4>
            <ul>
                <li>VLOOKUP (Vertical Lookup)</li>
                <li>HLOOKUP (Horizontal Lookup)</li>
                <li>INDEX + MATCH (Advanced)</li>
                <li>XLOOKUP (Modern Replacement)</li>
                <li>CHOOSE, COLUMN, ROW</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>📊 PivotTables & PivotCharts</h4>
            <ul>
                <li>Creating PivotTables</li>
                <li>Grouping Data</li>
                <li>Calculated Fields & Items</li>
                <li>Slicers & Timelines</li>
                <li>PivotCharts</li>
                <li>GETPIVOTDATA Function</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📈 Data Visualization in Excel</h4>
            <ul>
                <li>Column, Bar, Line Charts</li>
                <li>Pie, Doughnut Charts</li>
                <li>Combo Charts</li>
                <li>Histograms & Pareto Charts</li>
                <li>Waterfall & Funnel Charts</li>
                <li>Sparklines & Conditional Formatting</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>🔄 Power Query in Excel</h4>
            <ul>
                <li>Get & Transform Data</li>
                <li>Merging & Appending Queries</li>
                <li>Data Cleaning Techniques</li>
                <li>Unpivoting Data</li>
                <li>Automating Data Refresh</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with tab3:
    st.markdown("### Module 03: SQL for Data Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>🗄️ SQL Fundamentals</h4>
            <ul>
                <li>What is SQL? Why SQL for Analysts?</li>
                <li>RDBMS Concepts</li>
                <li>Database Setup (MySQL, PostgreSQL)</li>
                <li>Data Types in SQL</li>
                <li>CREATE, ALTER, DROP Tables</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>🔍 Basic Queries</h4>
            <ul>
                <li>SELECT, FROM, WHERE</li>
                <li>DISTINCT, LIMIT, OFFSET</li>
                <li>ORDER BY (ASC, DESC)</li>
                <li>Filtering with AND, OR, NOT</li>
                <li>IN, BETWEEN, LIKE, IS NULL</li>
            </ul>
            <div class="sql-box">
                SELECT customer_id, SUM(sales) as total_sales<br>
                FROM orders<br>
                WHERE order_date >= '2024-01-01'<br>
                GROUP BY customer_id<br>
                HAVING total_sales > 1000;
            </div>
        </div>
        
        <div class="module-card">
            <h4>📊 Aggregate Functions</h4>
            <ul>
                <li>COUNT, SUM, AVG, MIN, MAX</li>
                <li>GROUP BY</li>
                <li>HAVING vs WHERE</li>
                <li>DISTINCT Aggregations</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>🔗 Joins</h4>
            <ul>
                <li>INNER JOIN</li>
                <li>LEFT JOIN, RIGHT JOIN</li>
                <li>FULL OUTER JOIN</li>
                <li>CROSS JOIN</li>
                <li>SELF JOIN</li>
                <li>Joining Multiple Tables</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📝 Subqueries & CTEs</h4>
            <ul>
                <li>Single-Row Subqueries</li>
                <li>Multi-Row Subqueries (IN, ANY, ALL)</li>
                <li>Correlated Subqueries</li>
                <li>Common Table Expressions (CTEs)</li>
                <li>WITH Clause</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📊 Window Functions</h4>
            <ul>
                <li>ROW_NUMBER, RANK, DENSE_RANK</li>
                <li>LAG, LEAD</li>
                <li>FIRST_VALUE, LAST_VALUE</li>
                <li>Running Totals</li>
                <li>Moving Averages</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with tab4:
    st.markdown("### Module 04: Python for Data Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>🐍 Python Fundamentals</h4>
            <ul>
                <li>Python Basics & Syntax</li>
                <li>Variables & Data Types</li>
                <li>Lists, Tuples, Dictionaries</li>
                <li>Control Flow (if/else, loops)</li>
                <li>Functions & Lambda</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>🔢 NumPy for Analytics</h4>
            <ul>
                <li>NumPy Arrays</li>
                <li>Array Operations</li>
                <li>Statistical Functions</li>
                <li>Broadcasting</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>🐼 Pandas for Data Analysis</h4>
            <ul>
                <li>Series & DataFrames</li>
                <li>Reading Data (CSV, Excel, JSON)</li>
                <li>Data Inspection (head, info, describe)</li>
                <li>Selecting & Filtering Data</li>
                <li>Adding/Removing Columns</li>
                <li>Handling Missing Data</li>
            </ul>
            <div class="sql-box">
                import pandas as pd<br>
                df = pd.read_csv('sales.csv')<br>
                df.groupby('region')['sales'].agg(['sum', 'mean'])
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>📊 Data Manipulation</h4>
            <ul>
                <li>GroupBy Operations</li>
                <li>Aggregation Functions</li>
                <li>Merging & Joining DataFrames</li>
                <li>Pivot Tables</li>
                <li>Applying Functions</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📈 Visualization with Matplotlib</h4>
            <ul>
                <li>Line Plots, Bar Charts</li>
                <li>Histograms, Scatter Plots</li>
                <li>Customizing Plots</li>
                <li>Subplots</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>🎨 Visualization with Seaborn</h4>
            <ul>
                <li>Statistical Plots</li>
                <li>Box Plots, Violin Plots</li>
                <li>Heatmaps for Correlation</li>
                <li>Pair Plots, Joint Plots</li>
                <li>Facet Grids</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with tab5:
    st.markdown("### Module 05: Power BI for Business Intelligence")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>📊 Power BI Fundamentals</h4>
            <ul>
                <li>Power BI Ecosystem</li>
                <li>Power BI Desktop Interface</li>
                <li>Connecting to Data Sources</li>
                <li>Data Import Modes</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>🔄 Power Query</h4>
            <ul>
                <li>Data Transformation</li>
                <li>Merging & Appending Queries</li>
                <li>Cleaning Data</li>
                <li>Custom Columns</li>
                <li>M Language Basics</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📐 Data Modeling</h4>
            <ul>
                <li>Star Schema</li>
                <li>Relationships</li>
                <li>Cardinality</li>
                <li>Hierarchies</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>🧮 DAX Fundamentals</h4>
            <ul>
                <li>Calculated Columns vs Measures</li>
                <li>SUM, AVERAGE, COUNT</li>
                <li>CALCULATE, FILTER</li>
                <li>Time Intelligence (YTD, QTD, MTD)</li>
                <li>ALL, ALLEXCEPT</li>
            </ul>
            <div class="sql-box">
                Total Sales = SUM(Sales[Amount])<br>
                YTD Sales = TOTALYTD([Total Sales], 'Date'[Date])
            </div>
        </div>
        
        <div class="module-card">
            <h4>📈 Visualizations</h4>
            <ul>
                <li>Bar, Column, Line Charts</li>
                <li>Pie, Donut, Treemap</li>
                <li>Maps, Scatter Plots</li>
                <li>Slicers, Filters</li>
                <li>Bookmarks & Buttons</li>
                <li>Mobile Layout</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>☁️ Power BI Service</h4>
            <ul>
                <li>Publishing Reports</li>
                <li>Dashboards</li>
                <li>Workspaces & Apps</li>
                <li>Scheduled Refresh</li>
                <li>Row-Level Security</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with tab6:
    st.markdown("### Module 06: Tableau for Visualization")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>📉 Tableau Fundamentals</h4>
            <ul>
                <li>Tableau Interface</li>
                <li>Dimensions vs Measures</li>
                <li>Discrete vs Continuous</li>
                <li>Connecting to Data Sources</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📊 Basic Visualizations</h4>
            <ul>
                <li>Bar Charts, Line Charts</li>
                <li>Pie Charts, Donut Charts</li>
                <li>Scatter Plots</li>
                <li>Histograms</li>
                <li>Heatmaps</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>🔍 Advanced Visualizations</h4>
            <ul>
                <li>Dual Axis Charts</li>
                <li>Gantt Charts</li>
                <li>Waterfall Charts</li>
                <li>Box Plots</li>
                <li>Treemaps</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>🧮 Calculated Fields</h4>
            <ul>
                <li>Creating Calculated Fields</li>
                <li>Table Calculations</li>
                <li>Level of Detail (LOD) Expressions</li>
                <li>Parameters</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📊 Dashboards & Stories</h4>
            <ul>
                <li>Dashboard Design</li>
                <li>Actions & Interactivity</li>
                <li>Filters & Parameters</li>
                <li>Stories for Presentations</li>
                <li>Best Practices</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>☁️ Tableau Online/Public</h4>
            <ul>
                <li>Publishing to Tableau Public</li>
                <li>Tableau Online</li>
                <li>Sharing & Collaboration</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with tab7:
    st.markdown("### Module 07: Statistics & Capstone Projects")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>📊 Statistics for Analysts</h4>
            <ul>
                <li>Descriptive Statistics</li>
                <li>Mean, Median, Mode</li>
                <li>Standard Deviation, Variance</li>
                <li>Correlation Analysis</li>
                <li>Hypothesis Testing Basics</li>
                <li>A/B Testing</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📈 Exploratory Data Analysis</h4>
            <ul>
                <li>Univariate Analysis</li>
                <li>Bivariate Analysis</li>
                <li>Outlier Detection</li>
                <li>Pattern Discovery</li>
                <li>Insight Generation</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>📊 Storytelling with Data</h4>
            <ul>
                <li>Data Storytelling Framework</li>
                <li>Creating Narratives</li>
                <li>Presentation Skills</li>
                <li>Dashboard Storytelling</li>
                <li>Executive Presentations</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📋 Resume & Interview Prep</h4>
            <ul>
                <li>Resume Building for Analysts</li>
                <li>LinkedIn Optimization</li>
                <li>Portfolio Creation</li>
                <li>Mock Interviews</li>
                <li>SQL & Excel Test Prep</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# --- 8 Real-World Analytics Projects ---
st.markdown("## 🏆 8 Portfolio-Ready Analytics Projects")
st.markdown("### Build These Real-World Projects")

project_cols = st.columns(2)

projects = [
    {
        "title": "📊 Sales Analytics Dashboard",
        "description": "Complete sales analysis with regional performance, product categories, and growth trends",
        "tools": "Power BI, DAX, SQL",
        "skills": "Data Modeling, DAX, Visualization"
    },
    {
        "title": "🛒 E-commerce Customer Analysis",
        "description": "Customer segmentation, purchase patterns, and cohort analysis",
        "tools": "Python, Pandas, Seaborn",
        "skills": "Cohort Analysis, RFM Analysis"
    },
    {
        "title": "🏥 Healthcare Analytics",
        "description": "Patient wait times, department performance, and resource allocation",
        "tools": "Tableau, Excel",
        "skills": "KPI Tracking, Dashboard Design"
    },
    {
        "title": "💰 Financial Performance Report",
        "description": "P&L analysis, budget vs actual, variance analysis",
        "tools": "Excel, Power Query, Power BI",
        "skills": "Financial Analysis, Variance Analysis"
    },
    {
        "title": "📱 Marketing Campaign Analysis",
        "description": "Campaign ROI, channel performance, conversion analysis",
        "tools": "SQL, Python, Tableau",
        "skills": "A/B Testing, Attribution Analysis"
    },
    {
        "title": "🏭 Supply Chain Optimization",
        "description": "Inventory analysis, supplier performance, delivery metrics",
        "tools": "Power BI, DAX, SQL",
        "skills": "Inventory Analytics, KPIs"
    },
    {
        "title": "👥 HR Analytics Dashboard",
        "description": "Employee attrition, diversity metrics, recruitment analysis",
        "tools": "Tableau, Excel",
        "skills": "HR Metrics, Attrition Analysis"
    },
    {
        "title": "🌐 COVID-19 Data Analysis",
        "description": "Trend analysis, country comparisons, visualization dashboard",
        "tools": "Python, Plotly, Tableau Public",
        "skills": "Time Series, Storytelling"
    }
]

for i, project in enumerate(projects):
    if i % 2 == 0:
        cols = st.columns(2)
    with cols[i % 2]:
        st.markdown(f"""
        <div class="module-card">
            <h4>{project['title']}</h4>
            <p>{project['description']}</p>
            <p><strong>Tools:</strong> {project['tools']}</p>
            <p><strong>Skills:</strong> {project['skills']}</p>
            <p><span class="project-badge">Portfolio Project</span></p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# --- Tools You'll Master ---
st.markdown("## 🛠️ Tools & Technologies You'll Master")

tech_cols = st.columns(4)

technologies = [
    {"name": "Excel", "icon": "📗"},
    {"name": "SQL", "icon": "🗄️"},
    {"name": "Python", "icon": "🐍"},
    {"name": "Pandas", "icon": "🐼"},
    {"name": "Power BI", "icon": "📊"},
    {"name": "Tableau", "icon": "📉"},
    {"name": "Power Query", "icon": "🔄"},
    {"name": "DAX", "icon": "🧮"},
    {"name": "NumPy", "icon": "🔢"},
    {"name": "Matplotlib", "icon": "📈"},
    {"name": "Seaborn", "icon": "🎨"},
    {"name": "MySQL", "icon": "🗄️"},
    {"name": "PostgreSQL", "icon": "🐘"},
    {"name": "Google Sheets", "icon": "📊"},
    {"name": "Jupyter", "icon": "📓"},
    {"name": "VS Code", "icon": "💻"}
]

for i, tech in enumerate(technologies):
    if i % 4 == 0:
        cols = st.columns(4)
    with cols[i % 4]:
        st.markdown(f"""
        <div style="text-align: center; padding: 1rem;">
            <h1>{tech['icon']}</h1>
            <h4>{tech['name']}</h4>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# --- Skills You'll Gain ---
st.markdown("## 🎯 Skills You'll Master")

skill_cols = st.columns(3)

skills = [
    "Data Cleaning", "Data Wrangling", "Exploratory Data Analysis",
    "Data Visualization", "Dashboard Design", "Storytelling with Data",
    "SQL Querying", "Database Management", "Excel Analytics",
    "Business Intelligence", "KPI Tracking", "A/B Testing",
    "Cohort Analysis", "RFM Analysis", "Trend Analysis",
    "Financial Analysis", "Marketing Analytics", "HR Analytics",
    "Sales Analytics", "Supply Chain Analytics", "Healthcare Analytics"
]

for i, skill in enumerate(skills):
    if i % 7 == 0:
        cols = st.columns(3)
    with cols[i % 3]:
        st.markdown(f"""
        <div style="margin: 0.2rem;">
            <span class="tool-tag">{skill}</span>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# --- Certification & Benefits ---
st.markdown("## 🎓 Certification & Career Support")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="highlight-box">
        <h4>📜 You'll Receive</h4>
        <ul>
            <li>✅ Data Analytics Certificate (Verified)</li>
            <li>✅ 8 Project Portfolios (GitHub/Tableau Public)</li>
            <li>✅ LinkedIn Profile Optimization</li>
            <li>✅ Resume Building for Analyst Roles</li>
            <li>✅ Interview Preparation Guide</li>
            <li>✅ Portfolio Website Creation</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="highlight-box">
        <h4>🎁 Bonuses Included</h4>
        <ul>
            <li>📚 300+ Interview Questions Bank</li>
            <li>📊 40+ Datasets for Practice</li>
            <li>🎥 Lifetime Access to Recordings</li>
            <li>👥 24/7 Doubt Support</li>
            <li>💼 Job Placement Assistance</li>
            <li>🔄 Free Updates for 1 Year</li>
            <li>📋 Resume Review Sessions</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- Success Stories ---
st.markdown("## ⭐ Success Stories")

testimonials = st.columns(3)

testimonial_data = [
    {
        "name": "Priya Sharma",
        "role": "Data Analyst at Amazon",
        "text": "This program transformed my career. From non-tech background to Amazon in 6 months!",
        "salary": "12 LPA"
    },
    {
        "name": "Rahul Mehta",
        "role": "BI Analyst at Deloitte",
        "text": "The projects and placement support were amazing. Got 3 offers after completion.",
        "salary": "9.5 LPA"
    },
    {
        "name": "Neha Gupta",
        "role": "Marketing Analyst at Flipkart",
        "text": "Best decision ever! The curriculum is exactly what industry needs.",
        "salary": "11 LPA"
    }
]

for i, testimonial in enumerate(testimonial_data):
    with testimonials[i]:
        st.markdown(f"""
        <div class="module-card" style="text-align: center;">
            <p>⭐⭐⭐⭐⭐</p>
            <p><i>"{testimonial['text']}"</i></p>
            <p><strong>{testimonial['name']}</strong></p>
            <p>{testimonial['role']}</p>
            <p><span class="career-badge">{testimonial['salary']}</span></p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# --- FAQ Section ---
st.markdown("## ❓ Frequently Asked Questions")

faq_col1, faq_col2 = st.columns(2)

with faq_col1:
    with st.expander("📌 Do I need coding experience?"):
        st.write("No! We start from basics. No coding experience required. We'll teach you everything from scratch.")
    
    with st.expander("📌 Is mathematics background required?"):
        st.write("Basic high school math is enough. We cover all statistics concepts from basics.")
    
    with st.expander("📌 Which tools will I learn?"):
        st.write("Excel, SQL, Python (Pandas, NumPy), Power BI, Tableau - complete analytics toolkit.")
    
    with st.expander("📌 Is this enough for a Data Analyst job?"):
        st.write("Absolutely! 8 projects, interview prep, and placement assistance make you job-ready.")

with faq_col2:
    with st.expander("📌 Do you provide placement assistance?"):
        st.write("Yes! We provide 100% placement assistance including:")
        st.write("✅ Resume building & optimization")
        st.write("✅ LinkedIn profile enhancement")
        st.write("✅ Mock interviews with industry experts")
        st.write("✅ Job referrals to 500+ partner companies")
        st.write("✅ Interview preparation workshops")
        st.write("✅ Portfolio review & GitHub/Tableau Public setup")
    
    with st.expander("📌 What if I miss a live class?"):
        st.write("All sessions are recorded and available in your learning dashboard forever. You can watch anytime, anywhere!")
    
    with st.expander("📌 Is there any certificate?"):
        st.write("Yes! You'll receive a verified Data Analytics certificate recognized by 1000+ companies.")
    
    with st.expander("📌 Can I switch from another career to Data Analytics?"):
        st.write("Absolutely! 70% of our students come from non-tech backgrounds. We provide extra support for career switchers.")

st.markdown("---")

# --- Footer with CTA ---
st.markdown("""
<div style="background: linear-gradient(90deg, #FF8C00 0%, #FFD700 100%); padding: 2.5rem; border-radius: 10px; text-align: center; color: #2C3E50;">
    <h1>🚀 Ready to Become a Data Analyst?</h1>
    <h2>Join 4000+ Successful Data Analytics Professionals</h2>
    <p style="font-size: 1.3rem;">Next Batch: Starting Soon | Limited to 8 Students Only</p>
    <p style="font-size: 2rem; font-weight: bold;">Early Bird: ₹29,999 (Regular ₹35,000)</p>
    <p>✨ Includes 8 Projects + 300+ Interview Questions + Placement Support</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- Apply Now Button ---
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.page_link("pages/Apply_Now.py", label="📩 APPLY NOW & GET FREE DEMO CLASS", icon="🎯")
    st.markdown("<p style='text-align: center;'>Limited Seats Available • Book Your Free Demo Today!</p>", unsafe_allow_html=True)

st.markdown("---")
st.caption("*Note: Clicking 'Apply Now' will work once the 'pages/Apply_Now.py' file is created.*")