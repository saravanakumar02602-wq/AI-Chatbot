"""Knowledge base. Add entries with e(title, keywords, answer, phrases=[]).
Answers support **bold**, `code` and \\n line breaks. 'phrases' = exact sentences to match."""


def e(t, k, a, p=()):
    return {"t": t, "k": k, "a": a, "p": list(p)}


KB = [
    # ---------------- Greetings & small talk ----------------
    e("Hello", "hi hello hey hola vanakkam namaste greetings howdy yo",
      "Hello. I'm **AI-Chatbot**, a knowledge-base assistant. Ask me about AI, machine learning, deep learning, programming or algorithms.",
      ["hi there", "hello there", "hey there"]),
    e("Good morning", "good morning gm",
      "Good morning. What would you like to learn about AI or technology today?"),
    e("Good afternoon", "good afternoon",
      "Good afternoon. What would you like to know about AI or technology?"),
    e("Good evening", "good evening",
      "Good evening. What topic would you like to explore: AI, machine learning, deep learning, programming or algorithms?"),
    e("Good night", "good night goodnight sleep",
      "Good night. Come back anytime when you'd like to keep learning."),
    e("How are you", "doing fine well feeling",
      "I'm doing well, thank you for asking. How can I help with AI or technology today?",
      ["how are you", "how are you doing", "how do you do", "whats up", "what is up",
       "how is it going", "hows it going", "how r u", "sup"]),
    e("Thanks", "thanks thank thx appreciate",
      "You're welcome. Feel free to ask another question anytime.", ["thank you", "thank you so much"]),
    e("Goodbye", "bye goodbye later exit quit",
      "Goodbye. Keep learning, and come back whenever you have another question.", ["see you", "see you later"]),
    e("Who are you", "who name yourself introduce bot chatbot",
      "I'm **AI-Chatbot**, a Python + Flask chatbot. I have no AI API: I search a built-in knowledge base "
      "and return the best matching answer.",
      ["who are you", "what are you", "your name", "what is your name", "whats your name"]),
    e("Help", "help capabilities topics support",
      "I can answer questions on:\n**AI** concepts, **machine learning**, **deep learning**, "
      "**programming** and **algorithms**.\nTry: `What is overfitting?`, `Explain CNN`, `What is recursion?`",
      ["what can you do", "how can you help me", "help me", "help"]),
    e("How you work", "work works technology built made tfidf matching python flask",
      "Your question is cleaned and split into words, each knowledge-base entry is scored with "
      "**TF-IDF style weights** plus typo tolerance, and the best entry above 45% confidence is returned."),

    # ---------------- Artificial Intelligence ----------------
    e("Artificial Intelligence", "ai artificial intelligence intelligent machines definition concept",
      "**Artificial Intelligence (AI)** is the field of building machines that perform tasks needing human "
      "intelligence: learning, reasoning, perception and decision-making. It includes ML, deep learning, "
      "NLP, robotics and computer vision."),
    e("Types of AI", "types kinds narrow general super strong weak artificial intelligence agi asi",
      "**Narrow AI** does one task (spam filters, chess). **General AI (AGI)** would match human ability "
      "across tasks and does not exist yet. **Super AI** would surpass humans and is hypothetical."),
    e("AI history", "history timeline turing test dartmouth winter origin invented",
      "1950: Alan Turing proposes the **Turing Test**. 1956: the term AI is coined at Dartmouth. "
      "AI winters followed in the 1970s and 80s. 2012: deep learning wins ImageNet. 2017: the "
      "**Transformer** is introduced, leading to today's LLMs."),
    e("AI applications", "applications uses examples real world healthcare finance self driving recommendation",
      "AI is used in healthcare (disease detection), finance (fraud detection), transport (self-driving cars), "
      "e-commerce (recommendations), voice assistants, translation and cybersecurity."),
    e("AI ethics and bias", "ethics bias fairness responsible privacy risks explainable safety",
      "AI can inherit **bias** from its training data, so ethical AI needs fair data, transparency "
      "(explainability), privacy protection and human oversight."),
    e("Generative AI and LLMs", "generative gen llm large language model chatgpt gpt text image generation",
      "**Generative AI** creates new content (text, images, code). **Large Language Models (LLMs)** are "
      "Transformer networks trained on huge text data to predict the next word, which lets them write "
      "and answer questions."),
    e("Natural Language Processing", "nlp natural language processing text sentiment translation tokenization",
      "**NLP** lets computers understand human language. Tasks: sentiment analysis, translation, "
      "summarization, chatbots and named-entity recognition. Libraries: `NLTK`, `spaCy`, Hugging Face."),
    e("Computer Vision", "computer vision image recognition object detection face opencv",
      "**Computer vision** lets machines understand images and video: classification, object detection, "
      "face recognition and segmentation. CNNs and `OpenCV` are the usual tools."),
    e("AI vs ML vs DL", "difference between ai ml dl vs compare relationship",
      "**AI** is the broad goal of smart machines. **Machine learning** is a subset of AI where systems "
      "learn from data. **Deep learning** is a subset of ML that uses many-layered neural networks."),

    # ---------------- Machine Learning ----------------
    e("Machine learning", "machine learning ml learn data patterns concept definition",
      "**Machine learning** lets computers learn patterns from data instead of following fixed rules. "
      "Workflow: collect data → clean → choose model → train → evaluate → deploy."),
    e("Supervised learning", "supervised learning labeled labels training",
      "**Supervised learning** trains on labeled examples (input + correct output). Used for "
      "classification (spam or not) and regression (house price). Examples: linear regression, "
      "decision trees, SVM."),
    e("Unsupervised learning", "unsupervised learning unlabeled clustering kmeans pca dimensionality",
      "**Unsupervised learning** finds hidden structure in unlabeled data. Examples: **K-Means** "
      "clustering, hierarchical clustering and **PCA** for dimensionality reduction."),
    e("Reinforcement learning", "reinforcement learning agent reward environment policy q learning",
      "In **reinforcement learning** an agent interacts with an environment, receives rewards or penalties, "
      "and learns a policy that maximizes total reward. Used in games, robotics and AlphaGo."),
    e("Overfitting and underfitting", "overfitting underfitting overfit generalization variance bias regularization",
      "**Overfitting**: the model memorizes training data and fails on new data. **Underfitting**: it is too "
      "simple to learn the pattern. Fixes: more data, regularization (L1/L2), dropout, simpler models, "
      "cross-validation."),
    e("Train test split", "train test split validation cross dataset holdout",
      "Split data into **training** (learn), **validation** (tune) and **test** (final check) sets, "
      "commonly 70/15/15 or 80/20. `train_test_split` in scikit-learn does this."),
    e("Regression", "regression linear logistic predict continuous price",
      "**Regression** predicts a continuous number. **Linear regression** fits the line "
      "`y = mx + c` that minimizes squared error. Despite its name, logistic regression is used for classification."),
    e("Classification", "classification classify classes category spam label logistic",
      "**Classification** predicts a category (spam/not spam, cat/dog). Common algorithms: logistic "
      "regression, KNN, decision trees, random forest, SVM and neural networks."),
    e("Evaluation metrics", "evaluation metrics accuracy precision recall f1 score confusion matrix auc",
      "**Accuracy** = correct / total. **Precision** = true positives / predicted positives. **Recall** = "
      "true positives / actual positives. **F1** balances precision and recall. For regression use "
      "MAE, MSE, RMSE and R²."),
    e("Decision tree and random forest", "decision tree random forest ensemble bagging boosting xgboost",
      "A **decision tree** splits data with if-else questions. A **random forest** averages many trees "
      "trained on random subsets, which reduces overfitting. **Boosting** (XGBoost) builds trees sequentially."),
    e("K-Nearest Neighbors", "knn nearest neighbors neighbours k distance",
      "**KNN** classifies a point by majority vote of its *k* closest training points (using distance such "
      "as Euclidean). It is simple but slow on large datasets."),
    e("Feature engineering", "feature engineering features selection scaling normalization encoding preprocessing",
      "**Feature engineering** turns raw data into useful model inputs: handle missing values, scale "
      "numbers, one-hot encode categories and create new features. Good features often beat fancy models."),
    e("ML libraries", "libraries scikit learn sklearn pandas numpy tools framework",
      "Python ML stack: `NumPy` (arrays), `pandas` (tables), `matplotlib` (plots), `scikit-learn` "
      "(classic ML) and `TensorFlow`/`PyTorch` (deep learning)."),

    # ---------------- Deep Learning ----------------
    e("Deep learning", "deep learning dl layers neural concept definition",
      "**Deep learning** uses neural networks with many layers to learn features automatically from raw "
      "data such as images, audio and text. It needs lots of data and GPUs."),
    e("Neural network", "neural network neuron layer weights bias perceptron ann activation",
      "A **neural network** is layers of connected neurons: input → hidden → output. Each neuron computes "
      "`activation(w·x + b)`. Common activations: ReLU, sigmoid, tanh, softmax."),
    e("CNN", "cnn convolutional convolution pooling filter image",
      "A **CNN (Convolutional Neural Network)** uses convolution filters to detect edges, shapes and "
      "objects in images, followed by pooling and dense layers. Used in image classification and detection."),
    e("RNN and LSTM", "rnn lstm gru recurrent sequence time series memory",
      "**RNNs** process sequences by passing a hidden state step to step. **LSTM/GRU** add gates to remember "
      "long-term information. Used for time series and speech, and largely replaced by Transformers for text."),
    e("Transformer", "transformer attention self bert gpt encoder decoder",
      "The **Transformer** (2017, \"Attention Is All You Need\") uses **self-attention** to relate every word "
      "to every other word in parallel. It powers BERT, GPT and most modern LLMs."),
    e("Gradient descent and backpropagation", "gradient descent backpropagation backprop loss optimizer learning rate adam",
      "**Gradient descent** updates weights in the direction that reduces the **loss**. "
      "**Backpropagation** computes those gradients layer by layer using the chain rule. "
      "The **learning rate** controls step size; Adam is a popular optimizer."),
    e("TensorFlow and PyTorch", "tensorflow pytorch keras framework gpu library",
      "**TensorFlow** (Google, with Keras) and **PyTorch** (Meta) are the main deep-learning frameworks. "
      "PyTorch is popular for research and flexibility; TensorFlow for production deployment."),

    # ---------------- Programming ----------------
    e("Programming", "programming coding code software developer language concept",
      "**Programming** is writing instructions a computer can execute. Core ideas: variables, conditions, "
      "loops, functions, data structures and problem-solving."),
    e("Python", "python py pip script beginner",
      "**Python** is a readable, general-purpose language used in AI, data science, web (Flask, Django) and "
      "automation.\nExample: `print('Hello')`"),
    e("Object-oriented programming", "object oriented oop class object inheritance polymorphism encapsulation abstraction",
      "**OOP** organizes code into classes and objects. Four pillars: **encapsulation**, **abstraction**, "
      "**inheritance** and **polymorphism**."),
    e("Functions", "function functions def parameter argument return lambda",
      "A **function** is reusable code that takes inputs (parameters) and returns a result.\n"
      "Example: `def add(a, b): return a + b`"),
    e("Data structures", "data structures array list stack queue hash table dictionary tree linked",
      "Key data structures: **array/list**, **stack** (LIFO), **queue** (FIFO), **hash table/dict** "
      "(fast lookup), **linked list**, **tree** and **graph**. Choose by the operations you need."),
    e("API", "api rest endpoint http json request flask",
      "An **API** lets programs talk to each other. A **REST API** uses HTTP methods (GET, POST) and "
      "usually exchanges JSON. This chatbot uses a Flask endpoint, `/api/chat`."),
    e("Git and GitHub", "git github version control commit push pull branch repository",
      "**Git** tracks code changes: `git init`, `git add .`, `git commit -m \"msg\"`, `git push`. "
      "GitHub hosts repositories for sharing and teamwork."),
    e("SQL and databases", "sql database query select join mysql sqlite table",
      "**SQL** queries relational databases.\nExample: `SELECT name FROM students WHERE marks > 80;`\n"
      "Learn SELECT, WHERE, GROUP BY and JOIN first."),
    e("Web development", "html css javascript js web frontend backend website",
      "**HTML** structures a page, **CSS** styles it, **JavaScript** adds behaviour. The backend "
      "(Python/Flask) handles data and logic."),
    e("Debugging", "debugging debug bug error fix exception traceback",
      "Debugging tips: read the error message, reproduce the bug, print or log values, use a debugger "
      "breakpoint, and test small pieces separately."),
    e("Learn programming", "learn study start beginner roadmap practice improve tips",
      "Pick one language (Python is a great start), build small projects early, read other people's code, "
      "practise daily and keep your work on GitHub."),

    # ---------------- Algorithms ----------------
    e("Algorithm", "algorithm algorithms steps procedure concept definition",
      "An **algorithm** is a finite, step-by-step procedure for solving a problem. Good algorithms are "
      "correct and efficient in time and memory."),
    e("Big-O notation", "big o notation complexity time space efficiency runtime",
      "**Big-O** describes how runtime grows with input size *n*: O(1) constant, O(log n) binary search, "
      "O(n) linear scan, O(n log n) merge sort, O(n²) bubble sort."),
    e("Sorting algorithms", "sorting sort bubble merge quick insertion selection heap",
      "**Bubble/insertion/selection** sort are O(n²). **Merge sort** is O(n log n) and stable. "
      "**Quick sort** is O(n log n) on average. Python's `sorted()` uses Timsort."),
    e("Searching algorithms", "searching search binary linear find lookup",
      "**Linear search** checks every item, O(n). **Binary search** halves a *sorted* list each step, "
      "O(log n)."),
    e("Recursion", "recursion recursive base case factorial fibonacci call stack",
      "**Recursion** is a function calling itself on a smaller problem, with a **base case** to stop.\n"
      "Example: `def fact(n): return 1 if n <= 1 else n * fact(n-1)`"),
    e("Dynamic programming", "dynamic programming dp memoization overlapping subproblems knapsack",
      "**Dynamic programming** solves problems by storing answers to overlapping subproblems "
      "(memoization or a table), turning exponential work into polynomial. Examples: Fibonacci, knapsack."),
    e("Graph algorithms", "graph bfs dfs dijkstra shortest path traversal",
      "**BFS** explores level by level (shortest path in unweighted graphs). **DFS** goes deep first. "
      "**Dijkstra** finds shortest paths with non-negative weights."),

    # ---------------- Wider technology ----------------
    e("Data science", "data science analysis analytics analyst insights dataset",
      "**Data science** combines statistics, programming and domain knowledge to extract insights from data: "
      "question → collect → clean → explore → model → present."),
    e("Cloud computing", "cloud computing aws azure gcp server saas iaas paas",
      "**Cloud computing** rents computing power and storage over the internet (AWS, Azure, Google Cloud). "
      "Models: IaaS, PaaS and SaaS."),
    e("Cybersecurity", "cybersecurity security hacking encryption malware phishing password",
      "**Cybersecurity** protects systems and data. Basics: strong unique passwords, 2-factor "
      "authentication, software updates, encryption and caution with phishing links."),
]
