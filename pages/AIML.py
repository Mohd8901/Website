import streamlit as st

st.set_page_config(
    page_title="AI & Machine Learning Program", 
    page_icon="🤖",
    layout="wide"
)

# --- Custom CSS for AI/ML Branding ---
st.markdown("""
<style>
    .aiml-header {
        background: linear-gradient(90deg, #FF6B6B 0%, #4ECDC4 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .aiml-header h1 {
        color: #FFE66D;
        text-shadow: 2px 2px 4px #000000;
    }
    .highlight-box {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #FF6B6B;
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
        border-color: #4ECDC4;
    }
    .career-badge {
        background-color: #FF6B6B;
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-weight: bold;
        display: inline-block;
    }
    .code-box {
        background-color: #1e1e1e;
        color: #4ECDC4;
        padding: 0.5rem;
        border-radius: 5px;
        font-family: 'Courier New', monospace;
        border-left: 3px solid #FF6B6B;
    }
    .project-badge {
        background-color: #4ECDC4;
        color: white;
        padding: 0.2rem 0.5rem;
        border-radius: 5px;
        font-size: 0.8rem;
    }
    .algorithm-tag {
        background-color: #FFE66D;
        color: #000;
        padding: 0.2rem 0.5rem;
        border-radius: 15px;
        font-size: 0.8rem;
        display: inline-block;
        margin: 0.2rem;
    }
</style>
""", unsafe_allow_html=True)

# --- Header Section ---
st.markdown("""
<div class="aiml-header">
    <h1>🤖 AI & Machine Learning Mastery Program</h1>
    <h3>Complete AI/ML Journey | Machine Learning • Deep Learning • Generative AI • MLOps</h3>
    <p style="font-size: 1.2rem;">Become a Job-Ready AI/ML Engineer in 6 Months</p>
</div>
""", unsafe_allow_html=True)

# --- Quick Stats ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Duration", "6 Months", "Weekend/Hybrid")
with col2:
    st.metric("Level", "Beginner to Expert", "Math + Coding")
with col3:
    st.metric("Projects", "8 Industry Projects", "Portfolio Ready")
with col4:
    st.metric("Fee", "₹55,000", "EMI Available")

st.markdown("---")

# --- Why AI/ML? Section ---
st.markdown("## 🎯 Why AI/ML? The Future of Technology")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="highlight-box">
        <h4>📈 Career Opportunities</h4>
        <ul>
            <li><strong>Machine Learning Engineer</strong> - ₹10-25 LPA</li>
            <li><strong>AI Engineer</strong> - ₹12-30 LPA</li>
            <li><strong>Computer Vision Engineer</strong> - ₹12-28 LPA</li>
            <li><strong>NLP Engineer</strong> - ₹12-28 LPA</li>
            <li><strong>Generative AI Specialist</strong> - ₹15-40 LPA</li>
            <li><strong>Research Scientist</strong> - ₹18-45 LPA</li>
            <li><strong>MLOps Engineer</strong> - ₹15-35 LPA</li>
        </ul>
        <p><span class="career-badge">🔥 50% Growth in AI Jobs</span></p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="highlight-box">
        <h4>🏢 Top Hiring Companies</h4>
        <ul>
            <li>Google • Microsoft • Meta • Amazon</li>
            <li>OpenAI • Anthropic • Cohere</li>
            <li>NVIDIA • Intel • AMD</li>
            <li>JPMorgan • Goldman Sachs • Citadel</li>
            <li>Uber • Airbnb • Flipkart • Ola</li>
            <li>And 3000+ AI-first companies</li>
        </ul>
        <p><span class="career-badge">🎯 100% Placement Assistance</span></p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- Complete AI/ML Curriculum ---
st.markdown("## 📚 Complete AI/ML Curriculum")
st.markdown("### Structured Learning Path - From Zero to AI Engineer")

# Create tabs for different domains
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "📐 Foundations", 
    "🐍 Python for ML", 
    "📊 ML Fundamentals", 
    "🤖 Advanced ML", 
    "🧠 Deep Learning", 
    "👁️ Computer Vision", 
    "📝 NLP & GenAI", 
    "🚀 MLOps"
])

with tab1:
    st.markdown("### Module 01: AI/ML Foundations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>📌 Introduction to AI & ML</h4>
            <ul>
                <li>What is AI? History & Evolution</li>
                <li>AI vs ML vs DL vs GenAI</li>
                <li>Types of Machine Learning</li>
                <li>Supervised, Unsupervised, Reinforcement</li>
                <li>AI Applications Across Industries</li>
                <li>Ethics in AI & Responsible AI</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📊 Mathematics for ML</h4>
            <ul>
                <li>Linear Algebra Basics</li>
                <li>Vectors, Matrices, Tensors</li>
                <li>Matrix Operations & Eigenvalues</li>
                <li>Calculus for ML (Derivatives, Gradients)</li>
                <li>Optimization Techniques</li>
                <li>Probability & Statistics Review</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>🔧 Essential Tools</h4>
            <ul>
                <li>Jupyter Notebook & Google Colab</li>
                <li>VS Code for ML Development</li>
                <li>Git & GitHub for ML Projects</li>
                <li>Command Line for ML Engineers</li>
                <li>Docker Basics for ML</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📈 ML Project Lifecycle</h4>
            <ul>
                <li>Problem Definition & Framing</li>
                <li>Data Collection & Labeling</li>
                <li>Feature Engineering</li>
                <li>Model Selection & Training</li>
                <li>Evaluation & Validation</li>
                <li>Deployment & Monitoring</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.markdown("### Module 02: Python for Machine Learning")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>🐍 Python Fundamentals</h4>
            <ul>
                <li>Python Syntax & Data Types</li>
                <li>Control Flow & Functions</li>
                <li>List Comprehensions & Generators</li>
                <li>OOP for ML Applications</li>
                <li>Exception Handling</li>
                <li>File Operations</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>🔢 NumPy for ML</h4>
            <ul>
                <li>NumPy Arrays & Operations</li>
                <li>Broadcasting & Vectorization</li>
                <li>Linear Algebra with NumPy</li>
                <li>Random Number Generation</li>
                <li>Performance Optimization</li>
            </ul>
            <div class="code-box">
                import numpy as np<br>
                X = np.random.randn(1000, 10)<br>
                y = X @ np.random.randn(10) + 0.1 * np.random.randn(1000)
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>🐼 Pandas for Data</h4>
            <ul>
                <li>DataFrames & Series</li>
                <li>Data Loading & Inspection</li>
                <li>Data Cleaning & Preprocessing</li>
                <li>GroupBy & Aggregations</li>
                <li>Merging & Joining Datasets</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📊 Visualization for ML</h4>
            <ul>
                <li>Matplotlib for ML Plots</li>
                <li>Seaborn for Statistical Viz</li>
                <li>Plotly for Interactive Charts</li>
                <li>Visualizing Model Performance</li>
                <li>Feature Distribution Analysis</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with tab3:
    st.markdown("### Module 03: Machine Learning Fundamentals")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>🤖 ML Core Concepts</h4>
            <ul>
                <li>Train-Test Split</li>
                <li>Cross-Validation (K-Fold, Stratified)</li>
                <li>Bias-Variance Tradeoff</li>
                <li>Overfitting & Underfitting</li>
                <li>Learning Curves</li>
                <li>Model Complexity</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📈 Regression Algorithms</h4>
            <ul>
                <li>Linear Regression</li>
                <li>Polynomial Regression</li>
                <li>Regularization (Ridge, Lasso, ElasticNet)</li>
                <li>Evaluation Metrics</li>
                <li>MSE, RMSE, MAE, R², Adjusted R²</li>
            </ul>
            <div class="code-box">
                from sklearn.linear_model import Ridge<br>
                model = Ridge(alpha=1.0)<br>
                model.fit(X_train, y_train)
            </div>
        </div>
        
        <div class="module-card">
            <h4>📊 Classification Algorithms</h4>
            <ul>
                <li>Logistic Regression</li>
                <li>K-Nearest Neighbors</li>
                <li>Naive Bayes</li>
                <li>Support Vector Machines</li>
                <li>Decision Trees</li>
                <li>Evaluation Metrics</li>
                <li>Confusion Matrix, Precision, Recall, F1, ROC-AUC</li>
            </ul>
            <span class="algorithm-tag">SVM</span>
            <span class="algorithm-tag">KNN</span>
            <span class="algorithm-tag">Decision Trees</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>🔍 Unsupervised Learning</h4>
            <ul>
                <li>K-Means Clustering</li>
                <li>Hierarchical Clustering</li>
                <li>DBSCAN</li>
                <li>Gaussian Mixture Models</li>
                <li>Evaluation Metrics (Silhouette Score)</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📉 Dimensionality Reduction</h4>
            <ul>
                <li>PCA (Principal Component Analysis)</li>
                <li>t-SNE for Visualization</li>
                <li>UMAP</li>
                <li>Feature Selection Techniques</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📊 Model Evaluation</h4>
            <ul>
                <li>Cross-Validation Strategies</li>
                <li>Hyperparameter Tuning</li>
                <li>Grid Search & Random Search</li>
                <li>Bayesian Optimization</li>
                <li>Model Interpretability</li>
                <li>SHAP & LIME</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with tab4:
    st.markdown("### Module 04: Advanced Machine Learning")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>🌲 Ensemble Learning</h4>
            <ul>
                <li>Bagging (Bootstrap Aggregating)</li>
                <li>Random Forest</li>
                <li>Boosting (AdaBoost, Gradient Boosting)</li>
                <li>XGBoost - Extreme Gradient Boosting</li>
                <li>LightGBM</li>
                <li>CatBoost</li>
                <li>Stacking & Blending</li>
                <li>Voting Classifiers</li>
            </ul>
            <div class="code-box">
                import xgboost as xgb<br>
                model = xgb.XGBClassifier(n_estimators=100)<br>
                model.fit(X_train, y_train)
            </div>
        </div>
        
        <div class="module-card">
            <h4>⏱️ Time Series Analysis</h4>
            <ul>
                <li>Time Series Components</li>
                <li>Stationarity & ADF Test</li>
                <li>ARIMA & SARIMA Models</li>
                <li>Prophet by Facebook</li>
                <li>LSTMs for Time Series</li>
                <li>Forecasting Evaluation</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>🔍 Anomaly Detection</h4>
            <ul>
                <li>Statistical Methods</li>
                <li>Isolation Forest</li>
                <li>One-Class SVM</li>
                <li>Autoencoders for Anomaly Detection</li>
                <li>Applications in Fraud Detection</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📊 Recommendation Systems</h4>
            <ul>
                <li>Content-Based Filtering</li>
                <li>Collaborative Filtering</li>
                <li>Matrix Factorization</li>
                <li>Neural Collaborative Filtering</li>
                <li>Hybrid Recommenders</li>
                <li>Evaluation Metrics</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with tab5:
    st.markdown("### Module 05: Deep Learning")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>🧠 Neural Networks Fundamentals</h4>
            <ul>
                <li>Perceptron & MLP</li>
                <li>Activation Functions</li>
                <li>ReLU, Sigmoid, Tanh, Softmax</li>
                <li>Forward & Backward Propagation</li>
                <li>Loss Functions</li>
                <li>Optimizers (SGD, Adam, RMSprop)</li>
                <li>Learning Rate Scheduling</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>🔧 TensorFlow 2.x</h4>
            <ul>
                <li>TensorFlow Basics</li>
                <li>Keras Sequential API</li>
                <li>Keras Functional API</li>
                <li>Custom Layers & Models</li>
                <li>Callbacks (EarlyStopping, ModelCheckpoint)</li>
                <li>TensorBoard for Visualization</li>
            </ul>
            <div class="code-box">
                import tensorflow as tf<br>
                model = tf.keras.Sequential([<br>
                &nbsp;&nbsp;tf.keras.layers.Dense(64, activation='relu')<br>
                ])
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>🔥 PyTorch</h4>
            <ul>
                <li>PyTorch Tensors</li>
                <li>Autograd & Computational Graphs</li>
                <li>Building Neural Networks</li>
                <li>Training Loops</li>
                <li>DataLoaders & Datasets</li>
                <li>GPU Acceleration</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>⚙️ Advanced DL Concepts</h4>
            <ul>
                <li>Regularization (Dropout, Batch Norm)</li>
                <li>Vanishing/Exploding Gradients</li>
                <li>Weight Initialization</li>
                <li>Transfer Learning</li>
                <li>Fine-Tuning Strategies</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with tab6:
    st.markdown("### Module 06: Computer Vision")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>👁️ CNN Fundamentals</h4>
            <ul>
                <li>Convolutional Layers</li>
                <li>Pooling Layers</li>
                <li>Stride & Padding</li>
                <li>Feature Maps</li>
                <li>CNN Architectures</li>
                <li>LeNet, AlexNet, VGG</li>
                <li>ResNet, Inception, DenseNet</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>🖼️ Image Classification</h4>
            <ul>
                <li>Image Preprocessing</li>
                <li>Data Augmentation</li>
                <li>Transfer Learning for Vision</li>
                <li>Fine-tuning CNNs</li>
                <li>Popular Architectures</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>🎯 Object Detection</h4>
            <ul>
                <li>R-CNN, Fast R-CNN, Faster R-CNN</li>
                <li>YOLO (You Only Look Once)</li>
                <li>SSD (Single Shot Detector)</li>
                <li>Detection Evaluation (mAP, IoU)</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>🔍 Image Segmentation</h4>
            <ul>
                <li>Semantic Segmentation</li>
                <li>Instance Segmentation</li>
                <li>U-Net Architecture</li>
                <li>Mask R-CNN</li>
                <li>Applications in Medical Imaging</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>🎨 Advanced Vision</h4>
            <ul>
                <li>Face Detection & Recognition</li>
                <li>Pose Estimation</li>
                <li>Optical Character Recognition</li>
                <li>Video Analysis</li>
                <li>Generative Models (GANs for Images)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with tab7:
    st.markdown("### Module 07: NLP & Generative AI")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>📝 NLP Fundamentals</h4>
            <ul>
                <li>Text Preprocessing</li>
                <li>Tokenization, Stemming, Lemmatization</li>
                <li>Stop Words & Punctuation</li>
                <li>Bag of Words & TF-IDF</li>
                <li>n-grams</li>
                <li>Word Embeddings (Word2Vec, GloVe)</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📊 NLP Tasks</h4>
            <ul>
                <li>Text Classification</li>
                <li>Sentiment Analysis</li>
                <li>Named Entity Recognition</li>
                <li>Topic Modeling</li>
                <li>Text Summarization</li>
                <li>Machine Translation</li>
                <li>Question Answering</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>🔄 RNNs & LSTMs</h4>
            <ul>
                <li>Recurrent Neural Networks</li>
                <li>LSTM & GRU</li>
                <li>Bidirectional RNNs</li>
                <li>Sequence-to-Sequence Models</li>
                <li>Attention Mechanism</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>🤖 Transformers Architecture</h4>
            <ul>
                <li>Attention is All You Need</li>
                <li>Self-Attention & Multi-Head Attention</li>
                <li>Positional Encoding</li>
                <li>Encoder-Decoder Architecture</li>
                <li>BERT, GPT, T5 Architectures</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>🤗 Hugging Face Ecosystem</h4>
            <ul>
                <li>Transformers Library</li>
                <li>Pipelines for NLP Tasks</li>
                <li>Pre-trained Models Hub</li>
                <li>Fine-tuning Transformers</li>
                <li>Datasets & Tokenizers</li>
                <li>Hugging Face Spaces</li>
            </ul>
            <div class="code-box">
                from transformers import pipeline<br>
                classifier = pipeline("sentiment-analysis")<br>
                classifier("I love AI!")
            </div>
        </div>
        
        <div class="module-card">
            <h4>🎨 Generative AI</h4>
            <ul>
                <li>Large Language Models (LLMs)</li>
                <li>GPT-3, GPT-4, LLaMA, Mistral</li>
                <li>Prompt Engineering</li>
                <li>Few-shot & Zero-shot Learning</li>
                <li>Chain-of-Thought Prompting</li>
                <li>RAG (Retrieval-Augmented Generation)</li>
                <li>LangChain for LLM Applications</li>
                <li>Vector Databases (ChromaDB, FAISS)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with tab8:
    st.markdown("### Module 08: MLOps & Deployment")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>🚀 Model Deployment</h4>
            <ul>
                <li>Streamlit for ML Apps</li>
                <li>Gradio for Quick Demos</li>
                <li>Flask & FastAPI for APIs</li>
                <li>RESTful API Development</li>
                <li>Model Serving (TorchServe, TF Serving)</li>
                <li>ONNX for Model Interoperability</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>🐳 Containerization</h4>
            <ul>
                <li>Docker for ML Models</li>
                <li>Docker Compose</li>
                <li>DockerHub</li>
                <li>Container Best Practices</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>📦 MLOps Tools</h4>
            <ul>
                <li>Git & GitHub Actions</li>
                <li>DVC (Data Version Control)</li>
                <li>MLflow for Experiment Tracking</li>
                <li>Model Registry</li>
                <li>Weights & Biases</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>☁️ Cloud Deployment</h4>
            <ul>
                <li>AWS SageMaker</li>
                <li>Google Cloud Vertex AI</li>
                <li>Azure Machine Learning</li>
                <li>Hugging Face Spaces</li>
                <li>Streamlit Cloud</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📊 Model Monitoring</h4>
            <ul>
                <li>Model Drift Detection</li>
                <li>Performance Monitoring</li>
                <li>Logging & Alerting</li>
                <li>A/B Testing</li>
                <li>CI/CD for ML</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# --- 8 Industry AI/ML Projects ---
st.markdown("## 🏆 8 Industry-Ready AI/ML Projects")
st.markdown("### Build These Production-Ready Projects")

project_cols = st.columns(2)

projects = [
    {
        "title": "🖼️ Image Classification System",
        "description": "CNN-based classifier for 100+ object categories with transfer learning",
        "skills": "CNNs, Transfer Learning, Data Augmentation",
        "tools": "TensorFlow, ResNet, Streamlit",
        "level": "Intermediate"
    },
    {
        "title": "📝 Sentiment Analysis API",
        "description": "Real-time sentiment analysis API with Transformers",
        "skills": "NLP, Transformers, API Development",
        "tools": "Hugging Face, FastAPI, Docker",
        "level": "Intermediate"
    },
    {
        "title": "🔍 Object Detection System",
        "description": "Real-time object detection using YOLOv8",
        "skills": "Object Detection, YOLO, Computer Vision",
        "tools": "PyTorch, OpenCV, YOLO",
        "level": "Advanced"
    },
    {
        "title": "🤖 Customer Support Chatbot",
        "description": "RAG-based chatbot using LangChain & LLMs",
        "skills": "RAG, LLMs, Vector Databases",
        "tools": "LangChain, ChromaDB, OpenAI/GPT",
        "level": "Advanced"
    },
    {
        "title": "📊 Recommendation Engine",
        "description": "Movie/Product recommendation system",
        "skills": "Collaborative Filtering, Matrix Factorization",
        "tools": "Scikit-learn, Surprise, FastAPI",
        "level": "Intermediate"
    },
    {
        "title": "🏥 Medical Image Segmentation",
        "description": "Brain tumor segmentation using U-Net",
        "skills": "Segmentation, U-Net, Medical Imaging",
        "tools": "PyTorch, MONAI, TensorFlow",
        "level": "Advanced"
    },
    {
        "title": "📈 Time Series Forecasting",
        "description": "Stock price/sales forecasting with LSTMs",
        "skills": "Time Series, LSTMs, Sequence Models",
        "tools": "TensorFlow, Prophet, Streamlit",
        "level": "Intermediate"
    },
    {
        "title": "🔄 Text Generation System",
        "description": "Fine-tuned LLM for domain-specific text generation",
        "skills": "LLMs, Fine-tuning, Prompt Engineering",
        "tools": "Hugging Face, LoRA, Gradio",
        "level": "Advanced"
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
            <p><strong>Tools:</strong> {project['tools']}</p>
            <p><span class="project-badge">{project['level']}</span> <span class="career-badge">Portfolio Project</span></p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# --- Algorithms You'll Master ---
st.markdown("## 🧠 Algorithms & Techniques You'll Master")

algo_cols = st.columns(3)

algorithms = [
    "Linear Regression", "Logistic Regression", "Decision Trees", "Random Forest",
    "XGBoost", "LightGBM", "CatBoost", "SVM", "KNN", "Naive Bayes",
    "K-Means", "Hierarchical Clustering", "DBSCAN", "PCA", "t-SNE",
    "Neural Networks", "CNNs", "RNNs/LSTMs", "Transformers", "BERT",
    "GPT", "YOLO", "U-Net", "GANs", "Autoencoders",
    "Attention Mechanism", "RAG", "Word2Vec", "Transfer Learning", "Reinforcement Learning"
]

for i, algo in enumerate(algorithms):
    if i % 10 == 0:
        cols = st.columns(3)
    with cols[i % 3]:
        st.markdown(f"""
        <div style="margin: 0.2rem;">
            <span class="algorithm-tag">{algo}</span>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# --- Tools & Frameworks ---
st.markdown("## 🛠️ AI/ML Tools & Frameworks")

tech_cols = st.columns(4)

technologies = [
    {"name": "Python", "icon": "🐍"},
    {"name": "TensorFlow", "icon": "🧠"},
    {"name": "PyTorch", "icon": "🔥"},
    {"name": "Scikit-learn", "icon": "🤖"},
    {"name": "Hugging Face", "icon": "🤗"},
    {"name": "LangChain", "icon": "🔗"},
    {"name": "OpenCV", "icon": "👁️"},
    {"name": "XGBoost", "icon": "⚡"},
    {"name": "Streamlit", "icon": "🚀"},
    {"name": "FastAPI", "icon": "⚙️"},
    {"name": "Docker", "icon": "🐳"},
    {"name": "MLflow", "icon": "📋"},
    {"name": "Weights & Biases", "icon": "📊"},
    {"name": "AWS SageMaker", "icon": "☁️"},
    {"name": "Jupyter", "icon": "📓"},
    {"name": "Git/GitHub", "icon": "📦"}
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
            <li>✅ AI/ML Engineering Certificate (Verified)</li>
            <li>✅ 8 Project Portfolios (GitHub Ready)</li>
            <li>✅ LinkedIn Profile Optimization</li>
            <li>✅ Resume Building for AI/ML Roles</li>
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
            <li>📝 Research Paper Reading Group</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- FAQ Section ---
st.markdown("## ❓ Frequently Asked Questions")

faq_col1, faq_col2 = st.columns(2)

with faq_col1:
    with st.expander("📌 Do I need strong math background?"):
        st.write("We cover all required math (linear algebra, calculus, probability) from basics. High school math is sufficient.")
    
    with st.expander("📌 Is coding experience required?"):
        st.write("We start with Python fundamentals. No prior coding experience needed.")
    
    with st.expander("📌 Will I learn Generative AI?"):
        st.write("Yes! Complete module on GenAI including Transformers, Hugging Face, RAG, LangChain, and LLMs.")
    
    with st.expander("📌 Is this course enough for AI Engineer job?"):
        st.write("Absolutely! 8 industry projects, interview prep, and placement assistance make you job-ready.")

with faq_col2:
    with st.expander("📌 Which companies hire your students?"):
        st.write("Google, Microsoft, Amazon, JPMorgan, Flipkart, Uber, and 300+ AI startups.")
    
    with st.expander("📌 Do you provide placement assistance?"):
        st.write("Yes! Resume reviews, mock interviews, LinkedIn optimization, and job referrals.")
    
    with st.expander("📌 What if I miss a live class?"):
        st.write("All sessions are recorded and available in your dashboard forever. Watch anytime!")
    
    with st.expander("📌 Is there any project work?"):
        st.write("8 industry projects covering CV, NLP, GenAI, and MLOps. All projects are portfolio-ready.")

st.markdown("---")

# --- Footer with CTA ---
st.markdown("""
<div style="background: linear-gradient(90deg, #FF6B6B 0%, #4ECDC4 100%); padding: 2.5rem; border-radius: 10px; text-align: center; color: white;">
    <h1 style="color: #FFE66D;">🚀 Ready to Become an AI/ML Engineer?</h1>
    <h2>Join 3000+ Successful AI Professionals</h2>
    <p style="font-size: 1.3rem;">Next Batch: Starting Soon | Limited to 8 Students Only</p>
    <p style="font-size: 2rem; font-weight: bold; color: #FFE66D;">Early Bird: ₹45,000 (Regular ₹55,000)</p>
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