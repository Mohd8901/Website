import streamlit as st

st.set_page_config(
    page_title="Data Science Mastery Program", 
    page_icon="📊",
    layout="wide"
)

# --- Custom CSS for Data Science Branding ---
st.markdown("""
<style>
    .ds-header {
        background: linear-gradient(90deg, #6C3483 0%, #5DADE2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .ds-header h1 {
        color: #F8C471;
        text-shadow: 2px 2px 4px #000000;
    }
    .highlight-box {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #6C3483;
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
        border-color: #6C3483;
    }
    .career-badge {
        background-color: #6C3483;
        color: #F8C471;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-weight: bold;
        display: inline-block;
    }
    .code-box {
        background-color: #1e1e1e;
        color: #F8C471;
        padding: 0.5rem;
        border-radius: 5px;
        font-family: 'Courier New', monospace;
        border-left: 3px solid #6C3483;
    }
    .project-badge {
        background-color: #5DADE2;
        color: white;
        padding: 0.2rem 0.5rem;
        border-radius: 5px;
        font-size: 0.8rem;
    }
</style>
""", unsafe_allow_html=True)

# --- Header Section ---
st.markdown("""
<div class="ds-header">
    <h1>📊 Data Science Mastery Program</h1>
    <h3>Complete Data Science Journey | Statistics • Python • ML • Deep Learning • Generative AI</h3>
    <p style="font-size: 1.2rem;">Become a Job-Ready Data Scientist in 6 Months</p>
</div>
""", unsafe_allow_html=True)

# --- Quick Stats ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Duration", "6 Months", "Weekend/Hybrid")
with col2:
    st.metric("Level", "Beginner to Expert", "No Prior Coding Needed")
with col3:
    st.metric("Projects", "8 Real-World Projects", "Portfolio Ready")
with col4:
    st.metric("Fee", "₹45,000", "EMI Available")

st.markdown("---")

# --- Why Data Science? Section ---
st.markdown("## 🎯 Why Data Science? The Sexiest Job of the 21st Century")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="highlight-box">
        <h4>📈 Career Opportunities</h4>
        <ul>
            <li><strong>Data Scientist</strong> - ₹8-20 LPA</li>
            <li><strong>Machine Learning Engineer</strong> - ₹10-25 LPA</li>
            <li><strong>AI Engineer</strong> - ₹12-30 LPA</li>
            <li><strong>Data Analyst</strong> - ₹5-12 LPA</li>
            <li><strong>MLOps Engineer</strong> - ₹12-28 LPA</li>
            <li><strong>Research Scientist</strong> - ₹15-35 LPA</li>
        </ul>
        <p><span class="career-badge">🔥 40% Growth in Data Science Jobs</span></p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="highlight-box">
        <h4>🏢 Top Hiring Companies</h4>
        <ul>
            <li>Google • Amazon • Microsoft • Meta</li>
            <li>Flipkart • Uber • Ola • Zomato</li>
            <li>JPMorgan • Goldman Sachs • Citibank</li>
            <li>Deloitte • EY • KPMG • PwC</li>
            <li>Tata • Reliance • Infosys • Wipro</li>
            <li>And 5000+ more companies</li>
        </ul>
        <p><span class="career-badge">🎯 100% Placement Assistance</span></p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- Complete Data Science Curriculum ---
st.markdown("## 📚 Complete Data Science Curriculum")
st.markdown("### Structured Learning Path - From Zero to Data Scientist")

# Create tabs for different domains
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "📊 Foundations", 
    "🐍 Python", 
    "🧮 Statistics", 
    "🧹 Data Prep", 
    "🤖 Machine Learning", 
    "🧠 Deep Learning", 
    "🎨 Generative AI", 
    "🚀 Deployment"
])

with tab1:
    st.markdown("### Module 01: Data Science Foundations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>📌 Introduction to Data Science</h4>
            <ul>
                <li>What is Data Science? Why Data Science?</li>
                <li>Data Science Lifecycle</li>
                <li>Roles: Data Scientist vs Data Analyst vs ML Engineer</li>
                <li>Tools & Technologies Overview</li>
                <li>Industry Applications & Use Cases</li>
                <li>Setting Up Environment (Anaconda, Jupyter, VS Code)</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📊 Types of Data</h4>
            <ul>
                <li>Structured vs Unstructured Data</li>
                <li>Numerical Data (Discrete, Continuous)</li>
                <li>Categorical Data (Nominal, Ordinal)</li>
                <li>Time Series Data</li>
                <li>Text & Image Data</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>🔧 Essential Tools</h4>
            <ul>
                <li>Jupyter Notebook & Jupyter Lab</li>
                <li>Google Colab</li>
                <li>VS Code for Data Science</li>
                <li>Git & GitHub Basics</li>
                <li>Command Line for Data Scientists</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📈 Data Science Project Lifecycle</h4>
            <ul>
                <li>Problem Definition</li>
                <li>Data Collection</li>
                <li>Data Preparation</li>
                <li>Exploratory Data Analysis</li>
                <li>Model Building & Evaluation</li>
                <li>Deployment & Monitoring</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.markdown("### Module 02: Python for Data Science")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>🐍 Python Fundamentals</h4>
            <ul>
                <li>Python Syntax & Indentation</li>
                <li>Variables & Data Types</li>
                <li>Input/Output Operations</li>
                <li>Operators (Arithmetic, Comparison, Logical)</li>
                <li>Control Flow (if/else, loops)</li>
                <li>Functions & Lambda</li>
            </ul>
            <div class="code-box">
                def analyze_data(df):<br>
                &nbsp;&nbsp;&nbsp;&nbsp;return df.describe()
            </div>
        </div>
        
        <div class="module-card">
            <h4>📊 Data Structures</h4>
            <ul>
                <li>Lists & List Comprehensions</li>
                <li>Tuples & Sets</li>
                <li>Dictionaries</li>
                <li>Stack, Queue, Deque</li>
                <li>Iterators & Generators</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>🔢 NumPy for Numerical Computing</h4>
            <ul>
                <li>NumPy Arrays Creation</li>
                <li>Array Indexing & Slicing</li>
                <li>Vectorized Operations</li>
                <li>Broadcasting</li>
                <li>Universal Functions</li>
                <li>Linear Algebra with NumPy</li>
            </ul>
            <div class="code-box">
                import numpy as np<br>
                arr = np.array([1,2,3,4,5])<br>
                print(arr.mean())
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>🐼 Pandas for Data Manipulation</h4>
            <ul>
                <li>Series & DataFrames</li>
                <li>Reading Data (CSV, Excel, JSON, SQL)</li>
                <li>Data Inspection (head, info, describe)</li>
                <li>Selecting & Filtering Data</li>
                <li>Adding/Removing Columns</li>
                <li>GroupBy Operations</li>
                <li>Merging & Joining DataFrames</li>
            </ul>
            <div class="code-box">
                import pandas as pd<br>
                df = pd.read_csv('data.csv')<br>
                df.groupby('category').mean()
            </div>
        </div>
        
        <div class="module-card">
            <h4>📈 Data Visualization</h4>
            <ul>
                <li>Matplotlib Fundamentals</li>
                <li>Line Plots, Bar Charts, Histograms</li>
                <li>Scatter Plots, Pie Charts</li>
                <li>Seaborn for Statistical Plots</li>
                <li>Heatmaps, Pair Plots, Box Plots</li>
                <li>Plotly for Interactive Visualizations</li>
            </ul>
            <div class="code-box">
                import matplotlib.pyplot as plt<br>
                plt.scatter(df.x, df.y)<br>
                plt.show()
            </div>
        </div>
        
        <div class="module-card">
            <h4>⚙️ Advanced Python</h4>
            <ul>
                <li>Exception Handling</li>
                <li>File Handling</li>
                <li>Object-Oriented Programming</li>
                <li>Modules & Packages</li>
                <li>Decorators & Context Managers</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with tab3:
    st.markdown("### Module 03: Statistics & Probability")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>📊 Descriptive Statistics</h4>
            <ul>
                <li>Measures of Central Tendency</li>
                <li>Mean, Median, Mode</li>
                <li>Measures of Dispersion</li>
                <li>Range, Variance, Standard Deviation</li>
                <li>Skewness & Kurtosis</li>
                <li>Quartiles & IQR</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>🎲 Probability Basics</h4>
            <ul>
                <li>Classical, Empirical, Subjective Probability</li>
                <li>Addition & Multiplication Rules</li>
                <li>Conditional Probability</li>
                <li>Bayes' Theorem</li>
                <li>Independent & Dependent Events</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📈 Probability Distributions</h4>
            <ul>
                <li>Random Variables</li>
                <li>Discrete Distributions</li>
                <li>Binomial, Poisson</li>
                <li>Continuous Distributions</li>
                <li>Normal Distribution</li>
                <li>Exponential Distribution</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>📐 Inferential Statistics</h4>
            <ul>
                <li>Sampling Methods</li>
                <li>Central Limit Theorem</li>
                <li>Point Estimation & Interval Estimation</li>
                <li>Confidence Intervals</li>
                <li>Hypothesis Testing</li>
                <li>p-value & Significance Level</li>
                <li>Type I & Type II Errors</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>🔬 Statistical Tests</h4>
            <ul>
                <li>Z-Test & T-Test</li>
                <li>Chi-Square Test</li>
                <li>ANOVA (Analysis of Variance)</li>
                <li>Correlation & Covariance</li>
                <li>Pearson & Spearman Correlation</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📊 EDA with Statistics</h4>
            <ul>
                <li>Univariate Analysis</li>
                <li>Bivariate Analysis</li>
                <li>Multivariate Analysis</li>
                <li>Outlier Detection</li>
                <li>Feature Relationships</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with tab4:
    st.markdown("### Module 04: Data Preparation & Feature Engineering")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>🧹 Data Cleaning</h4>
            <ul>
                <li>Handling Missing Values</li>
                <li>Removing Duplicates</li>
                <li>Data Type Conversion</li>
                <li>String Cleaning & Text Processing</li>
                <li>Date & Time Handling</li>
                <li>Outlier Treatment</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>🔄 Data Transformation</h4>
            <ul>
                <li>Scaling & Normalization</li>
                <li>Min-Max Scaling</li>
                <li>Standardization (Z-score)</li>
                <li>Log Transformation</li>
                <li>Box-Cox Transformation</li>
                <li>Binning & Discretization</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>🔧 Feature Engineering</h4>
            <ul>
                <li>Creating New Features</li>
                <li>Interaction Features</li>
                <li>Polynomial Features</li>
                <li>Domain-Specific Features</li>
                <li>Feature Selection Techniques</li>
                <li>Dimensionality Reduction (PCA, t-SNE)</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📊 Encoding Categorical Variables</h4>
            <ul>
                <li>Label Encoding</li>
                <li>One-Hot Encoding</li>
                <li>Ordinal Encoding</li>
                <li>Target Encoding</li>
                <li>Frequency Encoding</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with tab5:
    st.markdown("### Module 05: Machine Learning")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>🤖 Machine Learning Fundamentals</h4>
            <ul>
                <li>Supervised vs Unsupervised Learning</li>
                <li>Regression vs Classification</li>
                <li>Train-Test Split</li>
                <li>Cross-Validation</li>
                <li>Bias-Variance Tradeoff</li>
                <li>Overfitting & Underfitting</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📈 Regression Algorithms</h4>
            <ul>
                <li>Linear Regression</li>
                <li>Polynomial Regression</li>
                <li>Ridge & Lasso Regression</li>
                <li>ElasticNet</li>
                <li>Evaluation Metrics (MSE, RMSE, MAE, R²)</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📊 Classification Algorithms</h4>
            <ul>
                <li>Logistic Regression</li>
                <li>K-Nearest Neighbors (KNN)</li>
                <li>Naive Bayes</li>
                <li>Support Vector Machines (SVM)</li>
                <li>Decision Trees</li>
                <li>Random Forest</li>
                <li>Evaluation Metrics (Accuracy, Precision, Recall, F1, ROC-AUC)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>🚀 Ensemble Learning</h4>
            <ul>
                <li>Bagging (Bootstrap Aggregating)</li>
                <li>Boosting (AdaBoost, Gradient Boosting)</li>
                <li>XGBoost, LightGBM, CatBoost</li>
                <li>Stacking & Blending</li>
                <li>Voting Classifiers</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>🔍 Unsupervised Learning</h4>
            <ul>
                <li>K-Means Clustering</li>
                <li>Hierarchical Clustering</li>
                <li>DBSCAN</li>
                <li>Gaussian Mixture Models</li>
                <li>Anomaly Detection</li>
                <li>Association Rule Mining (Apriori)</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>⚙️ Model Optimization</h4>
            <ul>
                <li>Hyperparameter Tuning</li>
                <li>Grid Search & Random Search</li>
                <li>Bayesian Optimization</li>
                <li>Feature Importance</li>
                <li>Model Interpretability (SHAP, LIME)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with tab6:
    st.markdown("### Module 06: Deep Learning")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>🧠 Neural Networks Fundamentals</h4>
            <ul>
                <li>Perceptron & Multi-Layer Perceptron</li>
                <li>Activation Functions (ReLU, Sigmoid, Tanh, Softmax)</li>
                <li>Forward Propagation</li>
                <li>Backpropagation</li>
                <li>Loss Functions</li>
                <li>Optimizers (SGD, Adam, RMSprop)</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>🔧 TensorFlow & Keras</h4>
            <ul>
                <li>TensorFlow Basics</li>
                <li>Keras Sequential API</li>
                <li>Keras Functional API</li>
                <li>Callbacks (Early Stopping, Model Checkpoint)</li>
                <li>TensorBoard for Visualization</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>🔥 PyTorch</h4>
            <ul>
                <li>PyTorch Basics</li>
                <li>Tensors & Autograd</li>
                <li>Building Neural Networks</li>
                <li>Training Loops</li>
                <li>DataLoaders & Datasets</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>🖼️ Computer Vision (CNNs)</h4>
            <ul>
                <li>Convolutional Neural Networks</li>
                <li>Pooling Layers</li>
                <li>CNN Architectures (LeNet, AlexNet, VGG)</li>
                <li>Transfer Learning</li>
                <li>Image Classification</li>
                <li>Object Detection (YOLO, SSD)</li>
                <li>Image Segmentation</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📝 Natural Language Processing</h4>
            <ul>
                <li>Text Preprocessing</li>
                <li>Tokenization, Stemming, Lemmatization</li>
                <li>Bag of Words, TF-IDF</li>
                <li>Word Embeddings (Word2Vec, GloVe)</li>
                <li>RNNs & LSTMs</li>
                <li>GRU & Bidirectional RNNs</li>
                <li>Attention Mechanism</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>⏱️ Advanced Deep Learning</h4>
            <ul>
                <li>Regularization (Dropout, Batch Norm)</li>
                <li>Vanishing/Exploding Gradients</li>
                <li>Autoencoders</li>
                <li>Generative Adversarial Networks (GANs)</li>
                <li>Siamese Networks</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with tab7:
    st.markdown("### Module 07: Generative AI")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>🎨 Introduction to Generative AI</h4>
            <ul>
                <li>What is Generative AI?</li>
                <li>LLMs (Large Language Models)</li>
                <li>Transformers Architecture</li>
                <li>Self-Attention Mechanism</li>
                <li>Pre-trained Models Overview</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>🤗 Hugging Face Ecosystem</h4>
            <ul>
                <li>Hugging Face Transformers Library</li>
                <li>Loading Pre-trained Models</li>
                <li>Pipelines for NLP Tasks</li>
                <li>Fine-tuning Transformers</li>
                <li>Hugging Face Datasets</li>
                <li>Hugging Face Hub & Spaces</li>
            </ul>
            <div class="code-box">
                from transformers import pipeline<br>
                generator = pipeline('text-generation')<br>
                generator('Once upon a time')
            </div>
        </div>
        
        <div class="module-card">
            <h4>📝 Popular LLMs</h4>
            <ul>
                <li>BERT & RoBERTa</li>
                <li>GPT Series (GPT-2, GPT-3, GPT-4)</li>
                <li>LLaMA & Mistral</li>
                <li>T5 & BART</li>
                <li>Claude & Gemini</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>🔧 Prompt Engineering</h4>
            <ul>
                <li>Prompt Design Strategies</li>
                <li>Zero-shot & Few-shot Learning</li>
                <li>Chain-of-Thought Prompting</li>
                <li>Instruction Tuning</li>
                <li>Role-based Prompting</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📚 RAG (Retrieval-Augmented Generation)</h4>
            <ul>
                <li>RAG Architecture</li>
                <li>Vector Databases (ChromaDB, FAISS, Pinecone)</li>
                <li>Embeddings & Semantic Search</li>
                <li>Building RAG Pipelines</li>
                <li>LangChain for LLM Applications</li>
            </ul>
            <div class="code-box">
                from langchain import ...<br>
                # Build RAG pipeline<br>
                # Connect to vector DB
            </div>
        </div>
        
        <div class="module-card">
            <h4>🖼️ Multimodal AI</h4>
            <ul>
                <li>CLIP (Contrastive Language-Image Pre-training)</li>
                <li>DALL-E & Stable Diffusion</li>
                <li>Image Generation</li>
                <li>LLaVA (Large Language and Vision Assistant)</li>
                <li>Whisper for Speech</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with tab8:
    st.markdown("### Module 08: Deployment & MLOps")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>🚀 Model Deployment</h4>
            <ul>
                <li>Streamlit for ML Apps</li>
                <li>Gradio for Quick Demos</li>
                <li>Flask & FastAPI for APIs</li>
                <li>Docker Containerization</li>
                <li>Hugging Face Spaces</li>
                <li>Model Serving (TorchServe, TF Serving)</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📦 MLOps Fundamentals</h4>
            <ul>
                <li>Git & GitHub for Version Control</li>
                <li>CI/CD with GitHub Actions</li>
                <li>Model Versioning (DVC)</li>
                <li>Experiment Tracking (MLflow)</li>
                <li>Model Registry</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>☁️ Cloud Deployment</h4>
            <ul>
                <li>AWS (SageMaker, EC2, S3)</li>
                <li>Google Cloud (Vertex AI)</li>
                <li>Azure Machine Learning</li>
                <li>Heroku & Render</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📊 Model Monitoring</h4>
            <ul>
                <li>Model Drift Detection</li>
                <li>Performance Monitoring</li>
                <li>Logging & Alerting</li>
                <li>A/B Testing</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# --- 8 Real-World Data Science Projects ---
st.markdown("## 🏆 8 Portfolio-Ready Data Science Projects")
st.markdown("### Build These Real-World Projects")

project_cols = st.columns(2)

projects = [
    {
        "title": "📈 Sales Forecasting",
        "description": "Time series forecasting for retail sales using ARIMA & Prophet",
        "skills": "Time Series, Regression, Feature Engineering",
        "domain": "E-commerce"
    },
    {
        "title": "🏠 House Price Prediction",
        "description": "Predict house prices using advanced regression techniques",
        "skills": "Linear Regression, Ridge, Lasso, XGBoost",
        "domain": "Real Estate"
    },
    {
        "title": "📱 Customer Churn Prediction",
        "description": "Predict which customers are likely to churn",
        "skills": "Classification, Ensemble, Feature Importance",
        "domain": "Telecom"
    },
    {
        "title": "🛒 Market Basket Analysis",
        "description": "Find product associations using Apriori algorithm",
        "skills": "Association Rules, Data Mining",
        "domain": "Retail"
    },
    {
        "title": "🎬 Movie Recommendation System",
        "description": "Build collaborative & content-based filtering",
        "skills": "Recommendation Systems, Matrix Factorization",
        "domain": "Entertainment"
    },
    {
        "title": "📊 Credit Card Fraud Detection",
        "description": "Detect fraudulent transactions using ML",
        "skills": "Anomaly Detection, Imbalanced Data, SMOTE",
        "domain": "Finance"
    },
    {
        "title": "🤖 Image Classifier",
        "description": "CNN-based image classification with transfer learning",
        "skills": "Deep Learning, CNNs, Transfer Learning",
        "domain": "Computer Vision"
    },
    {
        "title": "💬 Customer Support Chatbot",
        "description": "RAG-based chatbot using LangChain & LLMs",
        "skills": "Generative AI, RAG, Vector Databases",
        "domain": "Customer Service"
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
            <p><span class="project-badge">{project['domain']}</span></p>
            <p><span class="career-badge">Portfolio Project</span></p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# --- Tools & Technologies You'll Master ---
st.markdown("## 🛠️ Tools & Technologies You'll Master")

tech_cols = st.columns(4)

technologies = [
    {"name": "Python", "icon": "🐍"},
    {"name": "Pandas", "icon": "🐼"},
    {"name": "NumPy", "icon": "🔢"},
    {"name": "Scikit-learn", "icon": "🤖"},
    {"name": "TensorFlow", "icon": "🧠"},
    {"name": "PyTorch", "icon": "🔥"},
    {"name": "Hugging Face", "icon": "🤗"},
    {"name": "LangChain", "icon": "🔗"},
    {"name": "Streamlit", "icon": "🚀"},
    {"name": "Docker", "icon": "🐳"},
    {"name": "Git/GitHub", "icon": "📦"},
    {"name": "SQL", "icon": "🗄️"},
    {"name": "Tableau/Power BI", "icon": "📊"},
    {"name": "AWS/GCP", "icon": "☁️"},
    {"name": "MLflow", "icon": "📋"},
    {"name": "Jupyter", "icon": "📓"}
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

# --- Certification & Benefits ---
st.markdown("## 🎓 Certification & Career Support")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="highlight-box">
        <h4>📜 You'll Receive</h4>
        <ul>
            <li>✅ Data Science Certificate (Verified)</li>
            <li>✅ 8 Project Portfolios (GitHub Ready)</li>
            <li>✅ LinkedIn Profile Optimization</li>
            <li>✅ Resume Building for Data Scientist Roles</li>
            <li>✅ Interview Preparation Guide</li>
            <li>✅ GitHub Portfolio Setup</li>
            <li>✅ Kaggle Profile Building</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="highlight-box">
        <h4>🎁 Bonuses Included</h4>
        <ul>
            <li>📚 500+ Interview Questions Bank</li>
            <li>📊 50+ Datasets for Practice</li>
            <li>🎥 Lifetime Access to Recordings</li>
            <li>👥 24/7 Doubt Support</li>
            <li>💼 Job Placement Assistance</li>
            <li>🔄 Free Updates for 1 Year</li>
            <li>📋 1-on-1 Mentorship Sessions</li>
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
    
    with st.expander("📌 Is mathematics background required?"):
        st.write("Basic high school math is enough. We cover all statistics and math concepts from scratch.")
    
    with st.expander("📌 Will I learn Generative AI?"):
        st.write("Yes! Complete module on GenAI including Hugging Face, LangChain, RAG, and LLMs.")
    
    with st.expander("📌 Is this course enough for a Data Scientist job?"):
        st.write("Absolutely! 8 projects, interview prep, and placement assistance make you job-ready.")

with faq_col2:
    with st.expander("📌 Which companies have hired your students?"):
        st.write("Amazon, Deloitte, JPMorgan, Flipkart, Infosys, TCS, and 100+ startups.")
    
with faq_col2:
    with st.expander("📌 Do you provide placement assistance?"):
        st.write("Yes! We provide 100% placement assistance including:")
        st.write("✅ Resume building & optimization")
        st.write("✅ LinkedIn profile enhancement")
        st.write("✅ Mock interviews with industry experts")
        st.write("✅ Job referrals to 100+ partner companies")
        st.write("✅ Interview preparation workshops")
        st.write("✅ Portfolio review & GitHub optimization")
    
    with st.expander("📌 What if I miss a live class?"):
        st.write("All sessions are recorded and available in your learning dashboard forever. You can watch anytime, anywhere!")
    
    with st.expander("📌 Is there any certificate?"):
        st.write("Yes! You'll receive a verified Data Science certificate recognized by 500+ companies.")
    
    with st.expander("📌 Can I switch from another career to Data Science?"):
        st.write("Absolutely! 60% of our students come from non-tech backgrounds. We start from basics and provide extra support.")

st.markdown("---")

# --- Footer with CTA ---
st.markdown("""
<div style="background: linear-gradient(90deg, #6C3483 0%, #5DADE2 100%); padding: 2.5rem; border-radius: 10px; text-align: center; color: white;">
    <h1 style="color: #F8C471;">🚀 Ready to Become a Data Scientist?</h1>
    <h2>Join 5000+ Successful Data Science Professionals</h2>
    <p style="font-size: 1.3rem;">Next Batch: Starting Soon | Limited to 8 Students Only</p>
    <p style="font-size: 2rem; font-weight: bold; color: #F8C471;">Early Bird: ₹39,999 (Regular ₹45,000)</p>
    <p>✨ Includes 8 Projects + 500+ Interview Questions + Placement Support</p>
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