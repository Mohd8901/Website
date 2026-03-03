import streamlit as st

st.set_page_config(
    page_title="Excel & Advanced Excel Program", 
    page_icon="📊",
    layout="wide"
)

# --- Custom CSS for better styling ---
st.markdown("""
<style>
    .excel-header {
        background: linear-gradient(90deg, #1D6F42 0%, #21A366 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .highlight-box {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #21A366;
    }
    .module-card {
        background-color: white;
        padding: 1.2rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
        border: 1px solid #e0e0e0;
    }
    .career-badge {
        background-color: #FFD700;
        color: #000;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-weight: bold;
        display: inline-block;
    }
</style>
""", unsafe_allow_html=True)

# --- Header Section with Excel Branding ---
st.markdown("""
<div class="excel-header">
    <h1>📊 Microsoft Excel & Advanced Excel</h1>
    <h3>From Beginner to Expert | 100% Job-Ready Skills</h3>
    <p style="font-size: 1.2rem;">Master Excel Like a Pro • Data Analysis • Automation • Business Intelligence</p>
</div>
""", unsafe_allow_html=True)

# --- Quick Stats in Columns ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Duration", "2 Months", "Weekend Batches")
with col2:
    st.metric("Level", "Beginner to Advanced", "Certification")
with col3:
    st.metric("Projects", "5 Real-World Projects", "Portfolio Ready")
with col4:
    st.metric("Fee", "₹12,000", "EMI Available")

st.markdown("---")

# --- Why Excel? Section ---
st.markdown("## 🎯 Why Master Excel?")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="highlight-box">
        <h4>📈 Career Opportunities</h4>
        <ul>
            <li>Data Analyst - ₹4-8 LPA</li>
            <li>Business Analyst - ₹5-10 LPA</li>
            <li>Financial Analyst - ₹4-9 LPA</li>
            <li>Operations Manager - ₹6-12 LPA</li>
            <li>MIS Executive - ₹3-6 LPA</li>
            <li>Reporting Analyst - ₹4-7 LPA</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="highlight-box">
        <h4>💼 Industries Hiring</h4>
        <ul>
            <li>Banking & Finance</li>
            <li>IT & Consulting</li>
            <li>Retail & E-commerce</li>
            <li>Manufacturing</li>
            <li>Healthcare</li>
            <li>Government Sector</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- Comprehensive Curriculum ---
st.markdown("## 📚 Complete Excel Mastery Curriculum")
st.markdown("### From Zero to Excel Hero - Structured Learning Path")

# Create tabs for different levels
tab1, tab2, tab3, tab4 = st.tabs(["🔰 Beginner", "📊 Intermediate", "⚡ Advanced", "🚀 Expert"])

with tab1:
    st.markdown("### Module 01: Excel Fundamentals")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>📌 Getting Started</h4>
            <ul>
                <li>Excel Interface Navigation</li>
                <li>Workbook vs Worksheet</li>
                <li>Cells, Rows, Columns</li>
                <li>Data Entry Best Practices</li>
                <li>Saving & File Formats (.xlsx, .xls, .csv)</li>
                <li>Keyboard Shortcuts Mastery</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>🔢 Basic Formulas & Functions</h4>
            <ul>
                <li>SUM, AVERAGE, COUNT, COUNTA</li>
                <li>MAX, MIN, LARGE, SMALL</li>
                <li>AutoSum & Quick Analysis</li>
                <li>Relative vs Absolute References ($)</li>
                <li>Named Ranges</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>🎨 Formatting & Appearance</h4>
            <ul>
                <li>Font Formatting & Alignment</li>
                <li>Number Formatting (Currency, Date, Percentage)</li>
                <li>Borders & Fill Colors</li>
                <li>Conditional Formatting Basics</li>
                <li>Format Painter & Styles</li>
                <li>Themes & Templates</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📋 Data Management</h4>
            <ul>
                <li>Sorting (A-Z, Z-A, Custom)</li>
                <li>Filtering Data</li>
                <li>Find & Replace</li>
                <li>Go To Special</li>
                <li>Remove Duplicates</li>
                <li>Text to Columns</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.markdown("### Module 02: Intermediate Excel")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>📊 Charts & Visualization</h4>
            <ul>
                <li>Column, Bar, Line Charts</li>
                <li>Pie, Doughnut Charts</li>
                <li>Combo Charts</li>
                <li>Chart Formatting & Design</li>
                <li>Sparklines (Mini Charts)</li>
                <li>Best Practices for Visuals</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>🔍 Logical Functions</h4>
            <ul>
                <li>IF Function (Basic to Nested)</li>
                <li>AND, OR, NOT Functions</li>
                <li>IFERROR, IFNA</li>
                <li>SWITCH Function</li>
                <li>Practical Business Scenarios</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>🔗 Lookup & Reference</h4>
            <ul>
                <li>VLOOKUP (Vertical Lookup)</li>
                <li>HLOOKUP (Horizontal Lookup)</li>
                <li>INDEX & MATCH (Advanced)</li>
                <li>XLOOKUP (Modern Replacement)</li>
                <li>CHOOSE, COLUMN, ROW</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>📅 Date & Time Functions</h4>
            <ul>
                <li>TODAY, NOW</li>
                <li>DAY, MONTH, YEAR</li>
                <li>DATEDIF (Age Calculation)</li>
                <li>WORKDAY, NETWORKDAYS</li>
                <li>EOMONTH, EDATE</li>
                <li>Project Timeline Calculations</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📈 Statistical Functions</h4>
            <ul>
                <li>COUNTIF, COUNTIFS</li>
                <li>SUMIF, SUMIFS</li>
                <li>AVERAGEIF, AVERAGEIFS</li>
                <li>RANK, PERCENTILE</li>
                <li>QUARTILE, FREQUENCY</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📑 Working with Text</h4>
            <ul>
                <li>CONCAT, TEXTJOIN</li>
                <li>LEFT, RIGHT, MID</li>
                <li>LEN, FIND, SEARCH</li>
                <li>UPPER, LOWER, PROPER</li>
                <li>TRIM, CLEAN, SUBSTITUTE</li>
                <li>Data Cleaning Techniques</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with tab3:
    st.markdown("### Module 03: Advanced Excel")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>🔄 PivotTables & PivotCharts</h4>
            <ul>
                <li>Creating PivotTables</li>
                <li>Grouping & Filtering Data</li>
                <li>Calculated Fields & Items</li>
                <li>Slicers & Timelines</li>
                <li>PivotCharts for Dynamic Reports</li>
                <li>GETPIVOTDATA Function</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📊 Advanced Charts</h4>
            <ul>
                <li>Waterfall Chart</li>
                <li>Gantt Chart (Project Planning)</li>
                <li>Histogram & Pareto Chart</li>
                <li>Box & Whisker Plot</li>
                <li>Funnel Chart</li>
                <li>Map Charts (Geography)</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>🔧 Data Validation & Protection</h4>
            <ul>
                <li>Creating Drop-down Lists</li>
                <li>Custom Validation Rules</li>
                <li>Protecting Sheets & Workbooks</li>
                <li>Password Protection</li>
                <li>Allowing Specific Edits</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>📈 What-If Analysis</h4>
            <ul>
                <li>Scenario Manager</li>
                <li>Goal Seek</li>
                <li>Data Tables (One & Two Variable)</li>
                <li>Solver Add-in (Optimization)</li>
                <li>Financial Modeling Basics</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📂 Power Query (Get & Transform)</h4>
            <ul>
                <li>Importing from CSV, Text, Web</li>
                <li>Merging & Appending Queries</li>
                <li>Data Transformation Techniques</li>
                <li>Unpivoting Data</li>
                <li>Automating Data Refresh</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📊 Power Pivot & DAX</h4>
            <ul>
                <li>Data Modeling Basics</li>
                <li>Relationships between Tables</li>
                <li>DAX Formulas (CALCULATE, FILTER)</li>
                <li>Measures vs Calculated Columns</li>
                <li>Time Intelligence (YTD, QTD, MTD)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with tab4:
    st.markdown("### Module 04: Expert Level Excel")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>🤖 Macros & VBA</h4>
            <ul>
                <li>Recording Macros</li>
                <li>Understanding VBA Code</li>
                <li>Editing Recorded Macros</li>
                <li>Creating Custom Functions</li>
                <li>Automating Repetitive Tasks</li>
                <li>VBA Loops & Conditions</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📊 Dynamic Dashboards</h4>
            <ul>
                <li>Interactive Dashboard Design</li>
                <li>Form Controls (Buttons, Sliders)</li>
                <li>Combining Charts & Slicers</li>
                <li>Camera Tool for Snapshots</li>
                <li>Real-time Data Connections</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>🔄 Advanced Formulas</h4>
            <ul>
                <li>Array Formulas (CSE)</li>
                <li>Dynamic Array Functions</li>
                <li>FILTER, SORT, UNIQUE</li>
                <li>SEQUENCE, RANDARRAY</li>
                <li>LAMBDA & LET Functions</li>
                <li>Complex Formula Combinations</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>💼 Excel for Business</h4>
            <ul>
                <li>Financial Modeling</li>
                <li>Budgeting & Forecasting</li>
                <li>Profit & Loss Statements</li>
                <li>Sales Dashboard Creation</li>
                <li>KPI Tracking Systems</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# --- Real-World Projects Section ---
st.markdown("## 🏆 5 Real-World Projects You'll Build")
project_cols = st.columns(3)

projects = [
    {
        "title": "📊 Sales Dashboard",
        "description": "Interactive dashboard tracking sales performance, regional analysis, and growth trends",
        "skills": "PivotTables, Charts, Slicers"
    },
    {
        "title": "💰 Financial Model",
        "description": "Complete financial model with P&L, balance sheet, and cash flow statements",
        "skills": "What-If Analysis, Financial Functions"
    },
    {
        "title": "📈 HR Analytics",
        "description": "Employee attendance tracker with leave management and overtime calculation",
        "skills": "Date Functions, Conditional Formatting"
    },
    {
        "title": "🏭 Inventory Management",
        "description": "Automated inventory system with stock alerts and reorder calculations",
        "skills": "VLOOKUP, Conditional Logic"
    },
    {
        "title": "📅 Project Planner",
        "description": "Gantt chart based project tracker with milestone tracking",
        "skills": "Advanced Charts, Formulas"
    },
    {
        "title": "🤖 Automation Tool",
        "description": "VBA-powered tool that automates monthly report generation",
        "skills": "Macros, VBA Programming"
    }
]

for i, project in enumerate(projects):
    if i % 3 == 0:
        cols = st.columns(3)
    with cols[i % 3]:
        st.markdown(f"""
        <div class="module-card">
            <h4>{project['title']}</h4>
            <p>{project['description']}</p>
            <p><strong>Skills:</strong> {project['skills']}</p>
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
            <li>✅ Microsoft Excel Certification Prep</li>
            <li>✅ Course Completion Certificate</li>
            <li>✅ Portfolio of 5 Projects</li>
            <li>✅ LinkedIn Profile Optimization</li>
            <li>✅ Resume Building Support</li>
            <li>✅ Interview Preparation Guide</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="highlight-box">
        <h4>🎁 Bonuses Included</h4>
        <ul>
            <li>📚 100+ Excel Shortcut Cheat Sheet</li>
            <li>📊 50+ Professional Templates</li>
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

with st.expander("📌 Is this course for complete beginners?"):
    st.write("Absolutely! We start from the very basics and gradually move to advanced topics. No prior Excel knowledge is required.")

with st.expander("📌 Will I get a certificate after completion?"):
    st.write("Yes! You'll receive a verified certificate. We also prepare you for Microsoft Office Specialist (MOS) certification.")

with st.expander("📌 What if I miss a class?"):
    st.write("All classes are recorded and available in your learning dashboard. You can access them anytime, anywhere.")

with st.expander("📌 Is this course online or offline?"):
    st.write("We offer both options! You can join our hybrid mode with live online classes or in-person classroom training.")

with st.expander("📌 Will this help me get a job?"):
    st.write("Yes! Excel is the #1 skill required in 80% of jobs. With 5 projects and placement support, you'll be job-ready.")

st.markdown("---")

# --- Footer with CTA ---
st.markdown("""
<div style="background: linear-gradient(90deg, #1D6F42 0%, #21A366 100%); padding: 2rem; border-radius: 10px; text-align: center; color: white;">
    <h2>🚀 Ready to Become an Excel Expert?</h2>
    <h3>Join 5000+ Successful Students</h3>
    <p style="font-size: 1.2rem;">Batch Starting Soon | Limited Seats (6 per batch)</p>
    <p style="font-size: 1.5rem; font-weight: bold;">Early Bird: ₹9,999 (Regular ₹12,000)</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- Apply Now Button ---
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.page_link("pages/Apply_Now.py", label="📩 APPLY NOW & GET FREE DEMO CLASS", icon="🎯")

st.markdown("---")
st.caption("*Note: Clicking 'Apply Now' will work once the 'pages/Apply_Now.py' file is created.*")