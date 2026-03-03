import streamlit as st

st.set_page_config(
    page_title="Power BI Master Program", 
    page_icon="📊",
    layout="wide"
)

# --- Custom CSS for Power BI Branding ---
st.markdown("""
<style>
    .powerbi-header {
        background: linear-gradient(90deg, #000000 0%, #F2C811 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .powerbi-header h1 {
        color: #F2C811;
        text-shadow: 2px 2px 4px #000000;
    }
    .highlight-box {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #F2C811;
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
    }
    .career-badge {
        background-color: #F2C811;
        color: #000;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-weight: bold;
        display: inline-block;
    }
    .dax-highlight {
        background-color: #000000;
        color: #F2C811;
        padding: 0.5rem;
        border-radius: 5px;
        font-family: monospace;
    }
</style>
""", unsafe_allow_html=True)

# --- Header Section with Power BI Branding ---
st.markdown("""
<div class="powerbi-header">
    <h1>📊 Microsoft Power BI Master Program</h1>
    <h3>From Beginner to BI Expert | PL-300 Certification Ready</h3>
    <p style="font-size: 1.2rem;">Master Data Modeling • DAX • Dashboards • Power Query • Row-Level Security</p>
</div>
""", unsafe_allow_html=True)

# --- Quick Stats ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Duration", "2.5 Months", "Weekend/Hybrid")
with col2:
    st.metric("Level", "Beginner to Expert", "PL-300 Aligned")
with col3:
    st.metric("Projects", "6 Real Dashboards", "Portfolio Ready")
with col4:
    st.metric("Fee", "₹18,000", "EMI Available")

st.markdown("---")

# --- Why Power BI? Section ---
st.markdown("## 🎯 Why Power BI? The #1 BI Tool in the World")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="highlight-box">
        <h4>📈 Career Opportunities</h4>
        <ul>
            <li><strong>Power BI Developer</strong> - ₹5-10 LPA</li>
            <li><strong>Business Intelligence Analyst</strong> - ₹6-12 LPA</li>
            <li><strong>Data Analyst</strong> - ₹4-8 LPA</li>
            <li><strong>BI Consultant</strong> - ₹7-15 LPA</li>
            <li><strong>Reporting Analyst</strong> - ₹4-7 LPA</li>
            <li><strong>Dashboard Designer</strong> - ₹5-9 LPA</li>
        </ul>
        <p><span class="career-badge">🔥 3x Higher Demand than Tableau</span></p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="highlight-box">
        <h4>🏢 Top Hiring Companies</h4>
        <ul>
            <li>Microsoft • Amazon • Google</li>
            <li>Deloitte • PwC • EY • KPMG</li>
            <li>Walmart • Target • Amazon</li>
            <li>JPMorgan • Goldman Sachs</li>
            <li>Tata • Reliance • Infosys</li>
            <li>And 1000+ more</li>
        </ul>
        <p><span class="career-badge">🎯 85% of Fortune 500 use Power BI</span></p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- Comprehensive Power BI Curriculum ---
st.markdown("## 📚 Complete Power BI Mastery Curriculum")
st.markdown("### Structured Learning Path - From Zero to Hero")

# Create tabs for different levels
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🔰 Foundations", "⚡ Power Query", "📊 Data Modeling", "🧮 DAX Mastery", "🚀 Expert"])

with tab1:
    st.markdown("### Module 01: Power BI Foundations")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>📌 Introduction to Power BI</h4>
            <ul>
                <li>What is Business Intelligence?</li>
                <li>Power BI Ecosystem Overview</li>
                <li>Power BI Desktop vs Service vs Mobile</li>
                <li>Installation & Setup</li>
                <li>Interface Tour (Ribbon, Panes, Views)</li>
                <li>Power BI Workflow</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>🔌 Connecting to Data Sources</h4>
            <ul>
                <li>Excel & CSV Files</li>
                <li>SQL Server & Databases</li>
                <li>Web & APIs</li>
                <li>SharePoint & Folders</li>
                <li>Cloud Sources (Azure, Google Analytics)</li>
                <li>DirectQuery vs Import Mode</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>📋 Basic Data Transformation</h4>
            <ul>
                <li>Navigating Power Query Editor</li>
                <li>Promoting Headers</li>
                <li>Changing Data Types</li>
                <li>Removing Columns/Rows</li>
                <li>Filtering & Sorting</li>
                <li>Split & Merge Columns</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>🎨 First Visualization</h4>
            <ul>
                <li>Creating Your First Chart</li>
                <li>Formatting Visuals</li>
                <li>Adding Titles & Labels</li>
                <li>Basic Interactivity</li>
                <li>Saving & Publishing</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.markdown("### Module 02: Power Query - Data Transformation Mastery")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>🔄 Power Query Editor Deep Dive</h4>
            <ul>
                <li>M Language Fundamentals</li>
                <li>Applied Steps & Settings</li>
                <li>Advanced Editor</li>
                <li>Query Dependencies</li>
                <li>Query Parameters</li>
                <li>Performance Optimization</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>🧹 Data Cleaning Techniques</h4>
            <ul>
                <li>Removing Duplicates</li>
                <li>Handling Missing Values</li>
                <li>Replacing Values</li>
                <li>Filling Down/Up</li>
                <li>Pivot & Unpivot Columns</li>
                <li>Transpose & Reverse Rows</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>🔗 Combining Data</h4>
            <ul>
                <li>Append Queries (Union)</li>
                <li>Merge Queries (Join)</li>
                <li>Join Kinds (Inner, Left, Right, Full)</li>
                <li>Fuzzy Matching</li>
                <li>Combining Multiple Files</li>
                <li>Folder as Data Source</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📅 Advanced Transformations</h4>
            <ul>
                <li>Date & Time Transformations</li>
                <li>Conditional Columns</li>
                <li>Custom Columns with M</li>
                <li>Group By & Aggregations</li>
                <li>Index & Custom Columns</li>
                <li>Parsing JSON/XML/PDF</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with tab3:
    st.markdown("### Module 03: Data Modeling - The Heart of Power BI")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>📐 Data Modeling Fundamentals</h4>
            <ul>
                <li>Star Schema vs Snowflake</li>
                <li>Fact Tables vs Dimension Tables</li>
                <li>One-to-Many Relationships</li>
                <li>Cardinality & Cross Filter Direction</li>
                <li>Active vs Inactive Relationships</li>
                <li>Best Practices for Modeling</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>🔗 Managing Relationships</h4>
            <ul>
                <li>Creating Relationships</li>
                <li>Editing Relationships</li>
                <li>Understanding Cardinality</li>
                <li>Filter Flow & Direction</li>
                <li>Role-Playing Dimensions</li>
                <li>Bridge Tables</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>📊 Hierarchies & Columns</h4>
            <ul>
                <li>Creating Date Hierarchies</li>
                <li>Custom Hierarchies</li>
                <li>Calculated Columns</li>
                <li>Sort by Column</li>
                <li>Display Folders</li>
                <li>Synonyms & Descriptions</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📅 Date Tables</h4>
            <ul>
                <li>Importance of Date Tables</li>
                <li>Creating Date Tables (DAX/PQ)</li>
                <li>Mark as Date Table</li>
                <li>Time Intelligence Ready</li>
                <li>Fiscal Year Configurations</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with tab4:
    st.markdown("### Module 04: DAX - Data Analysis Expressions")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>🧮 DAX Fundamentals</h4>
            <ul>
                <li>What is DAX?</li>
                <li>Calculated Columns vs Measures</li>
                <li>DAX Syntax & Context</li>
                <li>Row Context vs Filter Context</li>
                <li>Evaluation Context</li>
                <li>DAX Data Types</li>
            </ul>
            <p class="dax-highlight">Total Sales = SUM(Sales[Amount])</p>
        </div>
        
        <div class="module-card">
            <h4>📊 Basic DAX Functions</h4>
            <ul>
                <li>SUM, AVERAGE, COUNT, DISTINCTCOUNT</li>
                <li>MIN, MAX, SUMX, AVERAGEX</li>
                <li>FILTER, ALL, ALLEXCEPT</li>
                <li>IF, SWITCH, AND, OR</li>
                <li>RELATED, RELATEDTABLE</li>
                <li>USERELATIONSHIP</li>
            </ul>
            <p class="dax-highlight">Sales > 1000 = CALCULATE([Total Sales], Sales[Amount] > 1000)</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>⏱️ Time Intelligence DAX</h4>
            <ul>
                <li>TOTALYTD, TOTALQTD, TOTALMTD</li>
                <li>SAMEPERIODLASTYEAR</li>
                <li>DATEADD, DATESBETWEEN</li>
                <li>PREVIOUSMONTH, NEXTMONTH</li>
                <li>PARALLELPERIOD</li>
                <li>Moving Averages</li>
            </ul>
            <p class="dax-highlight">YTD Sales = TOTALYTD([Total Sales], 'Date'[Date])</p>
        </div>
        
        <div class="module-card">
            <h4>🚀 Advanced DAX</h4>
            <ul>
                <li>CALCULATE & CALCULATETABLE</li>
                <li>FILTER Context Modification</li>
                <li>EARLIER Function</li>
                <li>RANKX</li>
                <li>TOPN</li>
                <li>Variables (VAR) in DAX</li>
            </ul>
            <p class="dax-highlight">Top Products = TOPN(10, Products, [Total Sales])</p>
        </div>
        """, unsafe_allow_html=True)

with tab5:
    st.markdown("### Module 05: Expert Level Power BI")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>📊 Advanced Visualizations</h4>
            <ul>
                <li>Custom Visuals from Marketplace</li>
                <li>Charticulator for Custom Charts</li>
                <li>Python & R Visuals</li>
                <li>Power Apps Integration</li>
                <li>AI Visuals (Key Influencers, Decomposition Tree)</li>
                <li>Paginated Reports (SSRS)</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>🎨 Dashboard Design</h4>
            <ul>
                <li>Bookmarks for Navigation</li>
                <li>Buttons & Drill-Through</li>
                <li>Tooltips (Report Page Tooltips)</li>
                <li>Mobile Layout Optimization</li>
                <li>Themes & Templates</li>
                <li>Best Practices for UX</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>🔒 Row-Level Security (RLS)</h4>
            <ul>
                <li>Static vs Dynamic RLS</li>
                <li>Creating Roles</li>
                <li>Testing Security</li>
                <li>USERNAME & USERPRINCIPALNAME</li>
                <li>RLS in Power BI Service</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>☁️ Power BI Service</h4>
            <ul>
                <li>Publishing to Service</li>
                <li>Workspaces & Apps</li>
                <li>Dashboards vs Reports</li>
                <li>Scheduled Refresh</li>
                <li>Gateway Configuration</li>
                <li>Dataflows & Datamarts</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>🔄 Collaboration & Sharing</h4>
            <ul>
                <li>Sharing Reports & Dashboards</li>
                <li>Export Options (PDF, PPT, Excel)</li>
                <li>Subscriptions & Alerts</li>
                <li>Comments & Annotations</li>
                <li>Workspace Roles & Permissions</li>
                <li>Embedding in SharePoint/Teams</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📈 Performance Optimization</h4>
            <ul>
                <li>Performance Analyzer</li>
                <li>DAX Studio Introduction</li>
                <li>VertiPaq Analyzer</li>
                <li>Best Practices for Speed</li>
                <li>Data Reduction Techniques</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# --- 6 Real-World Projects Section ---
st.markdown("## 🏆 6 Industry-Ready Dashboards You'll Build")
st.markdown("### Add These to Your Portfolio")

project_cols = st.columns(2)

projects = [
    {
        "title": "📈 Sales Performance Dashboard",
        "description": "Interactive dashboard tracking sales KPIs, regional performance, and growth trends",
        "skills": "DAX, Time Intelligence, Slicers",
        "level": "Intermediate"
    },
    {
        "title": "💰 Financial P&L Report",
        "description": "Profit & Loss statement with variance analysis and YTD comparisons",
        "skills": "CALCULATE, SAMEPERIODLASTYEAR, Waterfall Chart",
        "level": "Advanced"
    },
    {
        "title": "📊 HR Analytics & Attrition",
        "description": "Employee attrition analysis, diversity metrics, and workforce planning",
        "skills": "Bookmarks, Tooltips, Key Influencers",
        "level": "Intermediate"
    },
    {
        "title": "🏭 Supply Chain Dashboard",
        "description": "Inventory tracking, supplier performance, and logistics monitoring",
        "skills": "Power Query, Merging, Custom Visuals",
        "level": "Advanced"
    },
    {
        "title": "🎯 Marketing Campaign Analysis",
        "description": "Campaign ROI, channel performance, and customer segmentation",
        "skills": "RLS, Parameters, Drill-Through",
        "level": "Expert"
    },
    {
        "title": "📱 Executive KPI Scorecard",
        "description": "C-level dashboard with company-wide metrics and alerts",
        "skills": "Mobile Layout, Subscriptions, Paginated Reports",
        "level": "Expert"
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
            <p><span class="career-badge">{project['level']}</span></p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# --- PL-300 Certification Prep ---
st.markdown("## 🎓 Microsoft PL-300 Certification Preparation")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="highlight-box">
        <h4>📘 Exam Coverage (PL-300)</h4>
        <ul>
            <li>✅ Prepare Data (25-30%)</li>
            <li>✅ Model Data (25-30%)</li>
            <li>✅ Visualize Data (20-25%)</li>
            <li>✅ Analyze Data (10-15%)</li>
            <li>✅ Deploy & Maintain (5-10%)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="highlight-box">
        <h4>🎁 What You Get</h4>
        <ul>
            <li>📝 Mock Tests & Practice Exams</li>
            <li>📚 Study Guides & Cheat Sheets</li>
            <li>🎥 Exam Tips & Tricks</li>
            <li>🔄 Lifetime Updates</li>
            <li>🏅 Course Completion Certificate</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- Bonuses ---
st.markdown("## 🎁 Exclusive Bonuses")

bonus_cols = st.columns(3)

bonuses = [
    {
        "icon": "📊",
        "title": "50+ Power BI Templates",
        "desc": "Ready-to-use dashboard templates"
    },
    {
        "icon": "📚",
        "title": "DAX Formula Reference Guide",
        "desc": "200+ DAX formulas with examples"
    },
    {
        "icon": "🎥",
        "title": "Power Query M Language Course",
        "desc": "Bonus video series worth ₹5,000"
    },
    {
        "icon": "📋",
        "title": "Interview Q&A Pack",
        "desc": "100+ Power BI interview questions"
    },
    {
        "icon": "🔄",
        "title": "Project Files & Datasets",
        "desc": "All datasets used in projects"
    },
    {
        "icon": "👥",
        "title": "Job Placement Support",
        "desc": "Resume & LinkedIn optimization"
    }
]

for i, bonus in enumerate(bonuses):
    if i % 3 == 0:
        cols = st.columns(3)
    with cols[i % 3]:
        st.markdown(f"""
        <div class="module-card">
            <h1>{bonus['icon']}</h1>
            <h4>{bonus['title']}</h4>
            <p>{bonus['desc']}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# --- FAQ Section ---
st.markdown("## ❓ Frequently Asked Questions")

faq_col1, faq_col2 = st.columns(2)

with faq_col1:
    with st.expander("📌 Do I need prior Excel knowledge?"):
        st.write("Basic Excel is helpful but not mandatory. We cover everything from scratch.")
    
    with st.expander("📌 Will this help me get PL-300 certified?"):
        st.write("Absolutely! The curriculum is fully aligned with Microsoft PL-300 exam objectives.")
    
    with st.expander("📌 Is Power Query covered in depth?"):
        st.write("Yes! We have a dedicated Power Query module with M language fundamentals.")

with faq_col2:
    with st.expander("📌 Can I switch from Tableau to Power BI?"):
        st.write("Yes! Many students switch. We'll help you transition smoothly.")
    
    with st.expander("📌 Do you provide job placement help?"):
        st.write("Yes! Resume review, LinkedIn optimization, and interview prep included.")
    
    with st.expander("📌 What if I miss a live class?"):
        st.write("All sessions are recorded and available in your dashboard forever.")

st.markdown("---")

# --- Footer with CTA ---
st.markdown("""
<div style="background: linear-gradient(90deg, #000000 0%, #F2C811 100%); padding: 2.5rem; border-radius: 10px; text-align: center; color: white;">
    <h1 style="color: #F2C811;">🚀 Ready to Master Power BI?</h1>
    <h2>Join 3000+ Successful Power BI Professionals</h2>
    <p style="font-size: 1.3rem;">Next Batch: Starting Soon | Limited to 8 Students Only</p>
    <p style="font-size: 2rem; font-weight: bold; color: #F2C811;">Early Bird: ₹14,999 (Regular ₹18,000)</p>
    <p>✨ Includes PL-300 Certification Prep + 6 Projects + Lifetime Access</p>
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