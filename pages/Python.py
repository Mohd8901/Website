import streamlit as st

st.set_page_config(
    page_title="Python for Data Analysis", 
    page_icon="🐍",
    layout="wide"
)

# --- Custom CSS for Python Branding ---
st.markdown("""
<style>
    .python-header {
        background: linear-gradient(90deg, #306998 0%, #FFE873 50%, #306998 100%);
        padding: 2rem;
        border-radius: 10px;
        color: #000000;
        text-align: center;
    }
    .python-header h1 {
        color: #306998;
        text-shadow: 2px 2px 4px #FFE873;
    }
    .highlight-box {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #306998;
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
        border-color: #FFE873;
    }
    .career-badge {
        background-color: #306998;
        color: #FFE873;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-weight: bold;
        display: inline-block;
    }
    .code-snippet {
        background-color: #1e1e1e;
        color: #FFE873;
        padding: 0.5rem;
        border-radius: 5px;
        font-family: monospace;
    }
</style>
""", unsafe_allow_html=True)

# --- Header Section with Python Branding ---
st.markdown("""
<div class="python-header">
    <h1>🐍 Python for Data Analysis Master Program</h1>
    <h3>From Python Basics to Data Analysis Expert | 100% Job-Ready Skills</h3>
    <p style="font-size: 1.2rem;">Master Pandas • NumPy • Data Visualization • EDA • Real-World Projects</p>
</div>
""", unsafe_allow_html=True)

# --- Quick Stats ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Duration", "3 Months", "Weekend/Hybrid")
with col2:
    st.metric("Level", "Beginner to Pro", "No Coding Experience Needed")
with col3:
    st.metric("Projects", "6 Analysis Projects", "Portfolio Ready")
with col4:
    st.metric("Fee", "₹20,000", "EMI Available")

st.markdown("---")

# --- Why Python for Data Analysis? ---
st.markdown("## 🎯 Why Python for Data Analysis?")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="highlight-box">
        <h4>📈 Career Opportunities</h4>
        <ul>
            <li><strong>Data Analyst</strong> - ₹4-8 LPA</li>
            <li><strong>Business Analyst</strong> - ₹5-10 LPA</li>
            <li><strong>Data Analyst (Python)</strong> - ₹5-9 LPA</li>
            <li><strong>Reporting Analyst</strong> - ₹4-7 LPA</li>
            <li><strong>Financial Analyst</strong> - ₹4-8 LPA</li>
            <li><strong>Marketing Analyst</strong> - ₹4-7 LPA</li>
        </ul>
        <p><span class="career-badge">🔥 Python is #1 for Data Analysis</span></p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="highlight-box">
        <h4>🏢 Top Hiring Companies</h4>
        <ul>
            <li>Amazon • Flipkart • Google</li>
            <li>Deloitte • EY • KPMG • PwC</li>
            <li>JPMorgan • Goldman Sachs</li>
            <li>Tata • Reliance • Infosys</li>
            <li>Zomato • Swiggy • Ola</li>
            <li>And 5000+ more</li>
        </ul>
        <p><span class="career-badge">🎯 70% of Analyst Jobs Require Python</span></p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- Comprehensive Python Curriculum ---
st.markdown("## 📚 Complete Python for Data Analysis Curriculum")
st.markdown("### Structured Learning Path - No Coding Experience Required")

# Create tabs for different modules
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🔰 Python Basics", 
    "📊 NumPy", 
    "🐼 Pandas Core", 
    "🧹 Data Cleaning", 
    "📈 Visualization", 
    "🚀 Advanced Analysis"
])

with tab1:
    st.markdown("### Module 01: Python Fundamentals for Analysis")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>📌 Python Setup & Basics</h4>
            <ul>
                <li>Installing Python & Anaconda</li>
                <li>Jupyter Notebook vs VS Code</li>
                <li>Python Syntax & Indentation</li>
                <li>Variables & Data Types</li>
                <li>Input/Output Operations</li>
                <li>Comments & Best Practices</li>
            </ul>
            <p class="code-snippet">name = "Data Analyst"<br>age = 25<br>print(f"Hello {name}")</p>
        </div>
        
        <div class="module-card">
            <h4>🔢 Data Structures</h4>
            <ul>
                <li>Lists - Creation & Manipulation</li>
                <li>Tuples - Immutable Collections</li>
                <li>Sets - Unique Elements & Operations</li>
                <li>Dictionaries - Key-Value Pairs</li>
                <li>List Comprehensions</li>
                <li>Nested Data Structures</li>
            </ul>
            <p class="code-snippet">sales = [1200, 3400, 2800, 4500]<br>products = {'Laptop': 55000, 'Mouse': 800}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>🔄 Control Flow</h4>
            <ul>
                <li>Conditional Statements (if/elif/else)</li>
                <li>For Loops for Iteration</li>
                <li>While Loops</li>
                <li>Break, Continue, Pass</li>
                <li>Logical & Comparison Operators</li>
                <li>Looping Through Data Structures</li>
            </ul>
            <p class="code-snippet">for sale in sales:<br>    if sale > 3000:<br>        print(f"High: {sale}")</p>
        </div>
        
        <div class="module-card">
            <h4>⚙️ Functions for Analysis</h4>
            <ul>
                <li>Defining Functions</li>
                <li>Arguments & Return Values</li>
                <li>Lambda Functions</li>
                <li>Map, Filter, Reduce</li>
                <li>*args and **kwargs</li>
                <li>Built-in Functions for Data</li>
            </ul>
            <p class="code-snippet">avg_sales = lambda x: sum(x)/len(x)<br>print(avg_sales(sales))</p>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.markdown("### Module 02: NumPy - Numerical Computing")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>🔢 NumPy Arrays</h4>
            <ul>
                <li>Creating NumPy Arrays</li>
                <li>Array Attributes (shape, size, dtype)</li>
                <li>Array vs List Performance</li>
                <li>Creating Special Arrays (zeros, ones, arange)</li>
                <li>Random Number Generation</li>
                <li>Reshaping & Flattening</li>
            </ul>
            <p class="code-snippet">import numpy as np<br>arr = np.array([1, 2, 3, 4, 5])<br>print(arr.shape)</p>
        </div>
        
        <div class="module-card">
            <h4>🧮 Array Operations</h4>
            <ul>
                <li>Element-wise Operations</li>
                <li>Broadcasting</li>
                <li>Universal Functions (ufuncs)</li>
                <li>Mathematical Operations</li>
                <li>Comparison Operations</li>
                <li>Vectorization for Speed</li>
            </ul>
            <p class="code-snippet">arr * 2<br>np.sqrt(arr)<br>arr + 10</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>📊 Statistical Functions</h4>
            <ul>
                <li>np.mean(), np.median()</li>
                <li>np.std(), np.var()</li>
                <li>np.min(), np.max()</li>
                <li>np.percentile()</li>
                <li>np.sum(), np.cumsum()</li>
                <li>np.corrcoef() for Correlation</li>
            </ul>
            <p class="code-snippet">data = np.array([23, 45, 56, 78, 90])<br>print(f"Mean: {np.mean(data)}")<br>print(f"Std: {np.std(data)}")</p>
        </div>
        
        <div class="module-card">
            <h4>🔍 Indexing & Slicing</h4>
            <ul>
                <li>1D Array Indexing</li>
                <li>2D Array Indexing</li>
                <li>Boolean Indexing</li>
                <li>Fancy Indexing</li>
                <li>Where Function</li>
                <li>Conditional Selection</li>
            </ul>
            <p class="code-snippet">arr[arr > 50]<br>np.where(arr > 50, 'High', 'Low')</p>
        </div>
        """, unsafe_allow_html=True)

with tab3:
    st.markdown("### Module 03: Pandas - Data Analysis Heart")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>🐼 Pandas Series & DataFrames</h4>
            <ul>
                <li>Creating Series</li>
                <li>Creating DataFrames</li>
                <li>Reading Data (CSV, Excel, JSON)</li>
                <li>DataFrame Attributes</li>
                <li>Head, Tail, Info, Describe</li>
                <li>Sample, Shape, Columns</li>
            </ul>
            <p class="code-snippet">import pandas as pd<br>df = pd.read_csv('sales.csv')<br>df.head(10)</p>
        </div>
        
        <div class="module-card">
            <h4>🔍 Data Inspection</h4>
            <ul>
                <li>Viewing Data (head, tail, sample)</li>
                <li>Data Types (dtypes)</li>
                <li>Summary Statistics (describe)</li>
                <li>Information (info)</li>
                <li>Unique Values & Value Counts</li>
                <li>Memory Usage</li>
            </ul>
            <p class="code-snippet">df.info()<br>df.describe()<br>df['column'].value_counts()</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>📌 Selecting & Filtering</h4>
            <ul>
                <li>Column Selection</li>
                <li>Row Selection (loc, iloc)</li>
                <li>Conditional Filtering</li>
                <li>isin() & between()</li>
                <li>Query Method</li>
                <li>Handling NaN Values</li>
            </ul>
            <p class="code-snippet">df[df['sales'] > 1000]<br>df.loc[10:20, ['name', 'sales']]</p>
        </div>
        
        <div class="module-card">
            <h4>➕ Adding & Removing Columns</h4>
            <ul>
                <li>Creating New Columns</li>
                <li>Dropping Columns</li>
                <li>Renaming Columns</li>
                <li>Inserting at Position</li>
                <li>Column Operations</li>
                <li>Assign Method</li>
            </ul>
            <p class="code-snippet">df['total'] = df['price'] * df['quantity']<br>df.drop('old_col', axis=1)</p>
        </div>
        """, unsafe_allow_html=True)

with tab4:
    st.markdown("### Module 04: Data Cleaning & Preparation")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>🧹 Handling Missing Data</h4>
            <ul>
                <li>Detecting Missing Values (isnull, notnull)</li>
                <li>Counting Missing Values</li>
                <li>Dropping Missing Values (dropna)</li>
                <li>Filling Missing Values (fillna)</li>
                <li>Forward/Backward Fill</li>
                <li>Interpolation Techniques</li>
            </ul>
            <p class="code-snippet">df.isnull().sum()<br>df.fillna(df.mean())<br>df.dropna()</p>
        </div>
        
        <div class="module-card">
            <h4>🔄 Handling Duplicates</h4>
            <ul>
                <li>Finding Duplicates (duplicated)</li>
                <li>Removing Duplicates (drop_duplicates)</li>
                <li>Keeping First/Last Occurrence</li>
                <li>Duplicate Based on Subset</li>
                <li>Identifying Duplicate Patterns</li>
            </ul>
            <p class="code-snippet">df.duplicated().sum()<br>df.drop_duplicates(subset=['email'])</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>📝 Data Type Conversion</h4>
            <ul>
                <li>astype() Method</li>
                <li>Converting to datetime</li>
                <li>Extracting Date Components</li>
                <li>String to Numeric</li>
                <li>Categorical Data Types</li>
                <li>Memory Optimization</li>
            </ul>
            <p class="code-snippet">df['date'] = pd.to_datetime(df['date'])<br>df['month'] = df['date'].dt.month</p>
        </div>
        
        <div class="module-card">
            <h4>✂️ String Operations</h4>
            <ul>
                <li>str.lower(), str.upper()</li>
                <li>str.strip(), str.replace()</li>
                <li>str.contains() for Filtering</li>
                <li>str.split() & str.extract()</li>
                <li>str.len() & str.slice()</li>
                <li>Cleaning Text Data</li>
            </ul>
            <p class="code-snippet">df['name'].str.upper()<br>df[df['email'].str.contains('@')]</p>
        </div>
        """, unsafe_allow_html=True)

with tab5:
    st.markdown("### Module 05: Data Visualization")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>📊 Matplotlib Fundamentals</h4>
            <ul>
                <li>Line Plots</li>
                <li>Bar Charts (Vertical & Horizontal)</li>
                <li>Histograms</li>
                <li>Scatter Plots</li>
                <li>Pie Charts</li>
                <li>Customizing Plots (Labels, Titles, Legends)</li>
            </ul>
            <p class="code-snippet">import matplotlib.pyplot as plt<br>plt.plot(x, y)<br>plt.title('Sales Trend')</p>
        </div>
        
        <div class="module-card">
            <h4>🎨 Seaborn for Statistical Plots</h4>
            <ul>
                <li>Distribution Plots (distplot, kdeplot)</li>
                <li>Box Plots for Outliers</li>
                <li>Violin Plots</li>
                <li>Pair Plots for Relationships</li>
                <li>Heatmaps for Correlation</li>
                <li>Count Plots for Categories</li>
            </ul>
            <p class="code-snippet">import seaborn as sns<br>sns.boxplot(x=df['sales'])<br>sns.heatmap(df.corr())</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>📈 Advanced Visualizations</h4>
            <ul>
                <li>Subplots & Multiple Charts</li>
                <li>Time Series Visualization</li>
                <li>Facet Grids</li>
                <li>Joint Plots</li>
                <li>Regression Plots</li>
                <li>Saving Figures</li>
            </ul>
            <p class="code-snippet">sns.jointplot(x='sales', y='profit', data=df)<br>sns.pairplot(df, hue='category')</p>
        </div>
        
        <div class="module-card">
            <h4>📊 Plotly for Interactive Charts</h4>
            <ul>
                <li>Interactive Line Charts</li>
                <li>Interactive Bar Charts</li>
                <li>Scatter Plots with Hover</li>
                <li>Dashboards with Plotly</li>
                <li>Exporting Interactive HTML</li>
            </ul>
            <p class="code-snippet">import plotly.express as px<br>px.line(df, x='date', y='sales')</p>
        </div>
        """, unsafe_allow_html=True)

with tab6:
    st.markdown("### Module 06: Advanced Data Analysis")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>📊 GroupBy Operations</h4>
            <ul>
                <li>GroupBy Fundamentals</li>
                <li>Aggregation Functions</li>
                <li>Multiple Aggregations</li>
                <li>Grouped Transformations</li>
                <li>Filtering Groups</li>
                <li>Pivot Tables</li>
            </ul>
            <p class="code-snippet">df.groupby('category')['sales'].agg(['mean', 'sum'])<br>pd.pivot_table(df, values='sales', index='category')</p>
        </div>
        
        <div class="module-card">
            <h4>🔄 Merging & Joining</h4>
            <ul>
                <li>Concat (Stacking DataFrames)</li>
                <li>Merge (SQL-like Joins)</li>
                <li>Inner, Left, Right, Outer Joins</li>
                <li>Joining on Index</li>
                <li>Handling Overlapping Columns</li>
                <li>Appending Data</li>
            </ul>
            <p class="code-snippet">pd.merge(df1, df2, on='customer_id', how='left')<br>pd.concat([df1, df2], axis=0)</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>📈 Time Series Analysis</h4>
            <ul>
                <li>DateTime Index</li>
                <li>Resampling (Downsampling/Upsampling)</li>
                <li>Rolling Windows (Moving Averages)</li>
                <li>Date Ranges & Frequencies</li>
                <li>Lag & Shift Operations</li>
                <li>Time-based Filtering</li>
            </ul>
            <p class="code-snippet">df.set_index('date', inplace=True)<br>df['sales'].resample('M').sum()<br>df['sales'].rolling(7).mean()</p>
        </div>
        
        <div class="module-card">
            <h4>📊 EDA - Exploratory Data Analysis</h4>
            <ul>
                <li>Complete EDA Workflow</li>
                <li>Univariate Analysis</li>
                <li>Bivariate Analysis</li>
                <li>Multivariate Analysis</li>
                <li>Correlation Analysis</li>
                <li>Insight Extraction & Reporting</li>
            </ul>
            <p class="code-badge">🎯 Complete EDA Framework</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# --- 6 Real Analysis Projects Section ---
st.markdown("## 🏆 6 Portfolio-Ready Analysis Projects")
st.markdown("### Build These Real-World Projects")

project_cols = st.columns(2)

projects = [
    {
        "title": "📊 Sales Data Analysis",
        "description": "Complete analysis of sales data - trends, top products, regional performance",
        "skills": "Pandas, GroupBy, Visualization",
        "dataset": "E-commerce Sales Data"
    },
    {
        "title": "🏠 Housing Price Analysis",
        "description": "Analyze housing prices, factors affecting prices, price predictions",
        "skills": "NumPy, Correlation, Scatter Plots",
        "dataset": "Real Estate Data"
    },
    {
        "title": "📱 E-commerce Customer Analysis",
        "description": "Customer segmentation, purchase patterns, retention analysis",
        "skills": "Pivot Tables, Value Counts, Bar Charts",
        "dataset": "Customer Purchase History"
    },
    {
        "title": "🎬 Movie Industry Analysis",
        "description": "Box office trends, genre analysis, ratings distribution",
        "skills": "Data Cleaning, GroupBy, Heatmaps",
        "dataset": "IMDB/Movie Dataset"
    },
    {
        "title": "🌍 COVID-19 Data Analysis",
        "description": "Trend analysis, country comparisons, visualization dashboard",
        "skills": "Time Series, Rolling Statistics, Line Charts",
        "dataset": "COVID-19 Dataset"
    },
    {
        "title": "📈 Financial Stock Analysis",
        "description": "Stock price trends, moving averages, volatility analysis",
        "skills": "Date Operations, Resampling, Subplots",
        "dataset": "Stock Market Data"
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
            <p><strong>Skills:</strong> {project['skills']}</p>
            <p><strong>Dataset:</strong> {project['dataset']}</p>
            <p><span class="career-badge">Portfolio Project</span></p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# --- Libraries You'll Master ---
st.markdown("## 📚 Libraries You'll Master")
lib_cols = st.columns(4)

libraries = [
    {"name": "Pandas", "desc": "Data Manipulation", "icon": "🐼"},
    {"name": "NumPy", "desc": "Numerical Computing", "icon": "🔢"},
    {"name": "Matplotlib", "desc": "Basic Visualization", "icon": "📊"},
    {"name": "Seaborn", "desc": "Statistical Viz", "icon": "🎨"},
    {"name": "Plotly", "desc": "Interactive Charts", "icon": "📈"},
    {"name": "Scikit-learn", "desc": "Basic ML (Intro)", "icon": "🤖"},
    {"name": "Statsmodels", "desc": "Statistical Tests", "icon": "📐"},
    {"name": "Jupyter", "desc": "Interactive Environment", "icon": "📓"}
]

for i, lib in enumerate(libraries):
    if i % 4 == 0:
        cols = st.columns(4)
    with cols[i % 4]:
        st.markdown(f"""
        <div style="text-align: center; padding: 1rem;">
            <h1>{lib['icon']}</h1>
            <h4>{lib['name']}</h4>
            <p>{lib['desc']}</p>
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
            <li>✅ Python for Data Analysis Certificate</li>
            <li>✅ 6 Project Portfolios (GitHub Ready)</li>
            <li>✅ LinkedIn Profile Optimization</li>
            <li>✅ Resume Building for Analyst Roles</li>
            <li>✅ Interview Preparation Guide</li>
            <li>✅ GitHub Portfolio Setup</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="highlight-box">
        <h4>🎁 Bonuses Included</h4>
        <ul>
            <li>📚 100+ Pandas Code Snippets</li>
            <li>📊 20+ Dataset Files for Practice</li>
            <li>🎥 Lifetime Access to Recordings</li>
            <li>👥 24/7 Doubt Support</li>
            <li>💼 Job Placement Assistance</li>
            <li>🔄 Free Updates for 1 Year</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- FAQ Section ---
st.markdown("## ❓ Frequently Asked Questions")

faq_col1, faq_col2 = st.columns(2)

with faq_col1:
    with st.expander("📌 Do I need coding experience?"):
        st.write("No! We start from Python basics. Absolutely no coding experience required.")
    
    with st.expander("📌 Is this only for Data Analysis (not ML)?"):
        st.write("Yes! Pure Python for Data Analysis. No complex ML algorithms - just analysis and visualization.")
    
    with st.expander("📌 Will I learn Pandas deeply?"):
        st.write("Absolutely! Pandas is the core of this course. You'll master DataFrames, cleaning, transformation, and analysis.")

with faq_col2:
    with st.expander("📌 Can I switch from Excel to Python?"):
        st.write("Yes! This course is perfect for Excel users who want to upgrade to Python for larger datasets.")
    
    with st.expander("📌 Do you provide datasets for practice?"):
        st.write("Yes! 20+ datasets included for practice across different domains - sales, finance, marketing, etc.")
    
    with st.expander("📌 What if I miss a live class?"):
        st.write("All sessions are recorded and available in your dashboard forever. Watch anytime!")

st.markdown("---")

# --- Footer with CTA ---
st.markdown("""
<div style="background: linear-gradient(90deg, #306998 0%, #FFE873 100%); padding: 2.5rem; border-radius: 10px; text-align: center; color: #000000;">
    <h1 style="color: #306998;">🚀 Ready to Master Python for Data Analysis?</h1>
    <h2>Join 5000+ Successful Data Analysts</h2>
    <p style="font-size: 1.3rem;">Next Batch: Starting Soon | Limited to 8 Students Only</p>
    <p style="font-size: 2rem; font-weight: bold; color: #306998;">Early Bird: ₹14,999 (Regular ₹20,000)</p>
    <p>✨ Includes 6 Projects + 20+ Datasets + Lifetime Access</p>
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