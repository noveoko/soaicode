This curriculum is designed in the spirit of Faraday by focusing on conceptual mastery and experimental necessity. The 199 modules are grouped into 7 main phases, building from mathematical foundations to complex AGI architecture. Each module aims for the "just enough" intuition needed to build or debug a system.
Phase 1: Foundational Mechanics (Modules 1-30)
The essential mathematics and programming concepts treated as the algebra necessary for all models.
| # | Title | Duration | Subtopics |
|---|---|---|---|
| 1 | Vector Basics (Data) | 45 min | Direction & Magnitude; Dot Product as Similarity; Vector \times Scalar. |
| 2 | Matrix as Transformation | 45 min | Matrix \times Vector Intuition; Dimensionality Change; Identity Matrix. |
| 3 | Matrix Multiplication Core | 60 min | The Row-Column Rule (weighted sum); Associativity (layering); Broadcasting. |
| 4 | Linear Equations in Matrix Form | 30 min | \mathbf{Ax}=\mathbf{b} as a system; The concept of a Solution Space; Inversion concept. |
| 5 | Eigenvalues/Eigenvectors | 45 min | Intuition: "Stretching" vectors; Principal Component direction; Stability analysis. |
| 6 | The Chain Rule (Single Variable) | 60 min | Concept: Nested functions; Derivative of f(g(x)); Practical composition. |
| 7 | Partial Derivatives (Slope) | 45 min | \frac{\partial f}{\partial x}: Rate of change for one variable; Holding others constant. |
| 8 | Gradient (\nabla f) Intuition | 45 min | Direction of steepest ascent; Vector of all partials; Visualizing in 3D. |
| 9 | The Normal Distribution | 30 min | Central Limit Theorem intuition; Mean and Standard Deviation; Data Noise Modeling. |
| 10 | Expected Value \mathbb{E}[x] | 30 min | Weighted average concept; Long-run average outcome; Risk assessment. |
| 11 | Conditional Probability $P(A | B)$ | 45 min |
| 12 | Entropy (Uncertainty) | 60 min | Information content; Measure of randomness/surprise; Maximizing uncertainty. |
| 13 | Linear Regression (Conceptual) | 45 min | Fitting a line to data; Minimizing squared error; The \text{argmin} idea. |
| 14 | Cost Function Role | 30 min | Measuring "badness" of a prediction; Landscape visualization; Target to minimize. |
| 15 | Gradient Descent Core | 60 min | Stepping down the slope \mathbf{w} \leftarrow \mathbf{w} - \alpha \nabla; Learning rate \alpha; Local minima risk. |
| 16 | Learning Rate Tuning | 45 min | Too small vs. too large; Oscillations and divergence; The optimal path. |
| 17 | Python NumPy (Arrays) | 60 min | Array creation; Slicing and indexing; Element-wise operations. |
| 18 | Python Pandas (DataFrames) | 60 min | Loading tabular data; Data cleaning concepts; Grouping and aggregation. |
| 19 | Basic Data Normalization | 30 min | Scaling features 0-1 (Min-Max); Standardization (Z-score); Why scaling matters. |
| 20 | Overfitting/Underfitting | 45 min | Bias-Variance Tradeoff (conceptual); Train/Test split; Generalization idea. |
| 21 | Activation: ReLU | 30 min | Max(0, z); Introducing non-linearity; Sparsity and efficiency. |
| 22 | Activation: Sigmoid/Tanh | 45 min | S-shape for probability/bounds; Vanishing gradient risk (conceptual); Center shifting. |
| 23 | Binary Cross-Entropy Loss | 60 min | Log loss intuition; Penalizing confident wrong answers; Probabilistic error. |
| 24 | Categorical Cross-Entropy | 45 min | Multi-class extension; The One-Hot encoding requirement; Softmax link. |
| 25 | Softmax Function | 45 min | Turning scores into probabilities; Exponential scaling; Sum to one rule. |
| 26 | Weight Initialization | 45 min | Symmetry breaking; Need for small random weights; Vanishing/Exploding signals. |
| 27 | Batch Processing | 30 min | Training in chunks; Computational efficiency; Stochastic gradient descent concept. |
| 28 | Batch vs. Stochastic GD | 45 min | Speed vs. noise; True vs. Batch gradient; Minibatch compromise. |
| 29 | Regularization: L2 (Weight Decay) | 45 min | Penalty on large weights; Simplifying the model; Taming complexity. |
| 30 | Dropout Intuition | 45 min | Turning off neurons randomly; Preventing co-adaptation; Ensemble effect. |
Phase 2: Deep Learning Architecture (Modules 31-60)
Focuses on the core structure and training mechanisms of modern neural networks.
| # | Title | Duration | Subtopics |
|---|---|---|---|
| 31 | The Perceptron Model | 30 min | Neuron inputs/weights; Thresholding; Binary decision boundary. |
| 32 | Feedforward Networks (MLP) | 45 min | Layer stacking; Information flow; Universal approximation theory (concept). |
| 33 | Backpropagation Conceptual Flow | 60 min | Output error \rightarrow Gradients \rightarrow Weight Update; The "blame assignment" process. |
| 34 | Optimizer: Momentum | 45 min | Speeding up descent; The "ball rolling down a hill" analogy; Dampening oscillations. |
| 35 | Optimizer: Adam (Adaptive) | 60 min | Adaptive learning rates for each weight; Combining Momentum and RMSprop; Practical default. |
| 36 | Convolution Operation (1D) | 60 min | Sliding a filter (kernel); Feature detection; Local connectivity. |
| 37 | Convolutional Layers (CNN) | 45 min | 2D image kernels; Parameter sharing; Translation invariance. |
| 38 | Pooling Layers | 30 min | Max/Average pooling; Down-sampling (reducing size); Feature robustness. |
| 39 | CNN Architecture Intuition | 45 min | Convolutions \rightarrow Pooling \rightarrow Dense; Feature hierarchy; Visualizing filters. |
| 40 | Recurrent Neural Networks (RNN) | 60 min | Hidden state h_t; Sequence processing; Memory cell concept. |
| 41 | Backpropagation Through Time (BPTT) | 45 min | Unrolling the RNN; Gradient flow in time; Sequence length limits. |
| 42 | Vanishing/Exploding Gradients in RNN | 45 min | Why long sequences are hard; Signal degradation; The need for gates. |
| 43 | LSTM Cell Mechanics | 60 min | Input, Forget, Output gates; C-state (Conveyor belt); Long-term memory. |
| 44 | GRU Cell (Simplified RNN) | 45 min | Update and Reset gates; Efficiency vs. LSTM; Necessary memory mechanisms. |
| 45 | Embedding Layers | 45 min | Turning discrete tokens into vectors; Semantic space; Distributed representation. |
| 46 | Sequence-to-Sequence (Seq2Seq) | 60 min | Encoder-Decoder architecture; Context vector bottleneck; Translation application. |
| 47 | Attention Mechanism | 60 min | Dynamic context weighting; "Looking" at relevant parts of input; Overcoming the bottleneck. |
| 48 | Transformer Architecture | 60 min | Encoder/Decoder stacks; Parallel processing; Key/Query/Value concepts. |
| 49 | Self-Attention | 60 min | Tokens interacting with themselves; Capturing internal dependencies; Global context. |
| 50 | Positional Encodings | 45 min | Injecting sequence order; Why it's needed in Transformers; Relative position concept. |
| 51 | Multi-Head Attention | 45 min | Multiple "views" on the input; Combining different feature subspaces; Richer context. |
| 52 | Generative Adversarial Networks (GAN) | 60 min | Generator/Discriminator competition; Game theory setup; Zero-sum training. |
| 53 | GAN Loss Functions | 45 min | Discriminator trying to be right; Generator trying to fool; Training instability risk. |
| 54 | Autoencoders (Dimensionality Reduction) | 60 min | Encoder \rightarrow Latent Space \rightarrow Decoder; Reconstruction loss; Data compression. |
| 55 | Variational Autoencoders (VAE) | 60 min | Latent space as a distribution (mean/variance); KL Divergence concept; Generative sampling. |
| 56 | Transfer Learning | 45 min | Reusing pre-trained weights; Feature extraction vs. fine-tuning; Knowledge generalization. |
| 57 | Finetuning Strategies | 30 min | Unfreezing layers; Lower learning rates; Domain adaptation. |
| 58 | Zero-Shot Learning | 45 min | Generalizing to unseen categories; Semantic space connections; Prompting concept. |
| 59 | Few-Shot Learning | 45 min | Learning from minimal examples; Meta-learning (learning to learn) concept. |
| 60 | Data Augmentation | 45 min | Creating new data from old; Image transforms (flip, rotate); Synthetic data value. |
Phase 3: Reinforcement Learning Core (Modules 61-90)
The math-light, experimentally-heavy concepts needed for an agent to learn via interaction.
| # | Title | Duration | Subtopics |
|---|---|---|---|
| 61 | RL Framework (S, A, R, T) | 45 min | State, Action, Reward, Transition; Agent/Environment interaction; Markov Decision Process (MDP) concept. |
| 62 | The Reward Hypothesis | 30 min | All goals can be described by maximizing expected reward; Delayed reward problem; Reward shaping. |
| 63 | Value Function V(s) | 45 min | Expected return from state s; Estimating future success; State goodness. |
| 64 | Action-Value Function Q(s, a) | 45 min | Expected return after taking action a in state s; The Q-value; Policy guidance. |
| 65 | **Policy $\pi(a | s)$** | 30 min |
| 66 | Bellman Expectation Equation | 60 min | V^{\pi} in terms of V^{\pi}; Recursive relationship; Bootstrapping idea. |
| 67 | Bellman Optimality Equation | 60 min | V^* as maximum value; Taking the best possible action; The theoretical optimum. |
| 68 | Exploration vs. Exploitation | 45 min | \epsilon-greedy strategy; Trade-off for learning; Multi-Armed Bandit analogy. |
| 69 | Q-Learning (Off-Policy) | 60 min | Tabular Q-update rule; Learning optimal policy while exploring; Off-policy learning. |
| 70 | Deep Q-Networks (DQN) | 60 min | Using a NN to approximate Q(s, a); Experience Replay buffer; Target Network concept. |
| 71 | Experience Replay | 45 min | Storing/sampling past transitions; Breaking data correlation; Stability improvement. |
| 72 | Target Network (DQN) | 30 min | Separating estimation/target; Stabilizing the Bellman update; Reducing oscillation. |
| 73 | SARSA (On-Policy) | 45 min | State-Action-Reward-State'-Action'; Learning the current policy's value; Safe exploration. |
| 74 | Policy Gradients \nabla J(\theta) | 60 min | Directly optimizing the policy parameters \theta; REINFORCE algorithm; Likelihood ratio. |
| 75 | Actor-Critic Framework | 60 min | Actor (policy) & Critic (value function); Reducing variance of gradient; Two-head network. |
| 76 | Advantage Function A(s, a) | 45 min | How much better a is than average; Centering the reward signal; Variance reduction. |
| 77 | Proximal Policy Optimization (PPO) | 60 min | Clipping the policy update; Trust Region concept; Practical default for RL. |
| 78 | Model-Based RL | 60 min | Learning a model of the environment $P(s' |
| 79 | Monte Carlo Tree Search (MCTS) | 60 min | Search \rightarrow Expansion \rightarrow Simulation \rightarrow Backpropagation; Tree policy; AlphaGo intuition. |
| 80 | Curiosity-Driven Exploration | 45 min | Intrinsic Motivation; Reward for novelty (prediction error); Exploring unvisited states. |
| 81 | Inverse Reinforcement Learning (IRL) | 60 min | Inferring the reward function from expert demonstrations; Apprenticeship learning; Goal discovery. |
| 82 | Multi-Agent RL (MARL) | 60 min | Co-operative vs. Competitive; Decentralized execution; Centralized training. |
| 83 | Decentralized Execution | 45 min | Agents acting independently; Local observation space; Communication channel need. |
| 84 | Curriculum Learning for RL | 45 min | Gradually increasing task difficulty; Transferring skills; Boosting sample efficiency. |
| 85 | Hierarchical RL (HRL) | 60 min | Low-level actions (Primitives) & High-level goals (Manager); Abstraction of time; Subgoals. |
| 86 | Sim-to-Real Gap | 45 min | Why models fail in the real world; Domain randomization; Robustness through noise. |
| 87 | Off-Policy Correction (Importance Sampling) | 60 min | Correcting for using old data; Policy ratio; Variance issues in high dimensions. |
| 88 | Intrinsic Motivation | 45 min | Rewards generated internally; Information gain as reward; Generalization driver. |
| 89 | Temporal Difference (TD) Learning | 45 min | Bootstrapping with current estimates; V(s) \leftarrow V(s) + \alpha[R + \gamma V(s') - V(s)]; TD Error. |
| 90 | Discount Factor (\gamma) Role | 30 min | Valuing future rewards; Horizon of the agent; Setting \gamma \approx 1 for long-term. |
Phase 4: Language and Knowledge (Modules 91-120)
Concepts for processing and generating language, the foundation of human-like reasoning.
| # | Title | Duration | Subtopics |
|---|---|---|---|
| 91 | Tokenization | 45 min | Word vs. Subword (BPE/WordPiece); Vocabulary size impact; OOV (Out-Of-Vocabulary) issue. |
| 92 | Word Embeddings (Word2Vec) | 60 min | CBoW vs. Skip-gram; Analogy vector space (King - Man + Woman = Queen); Semantic meaning. |
| 93 | Contextual Embeddings | 45 min | ELMo/BERT concept; Meaning changing by context; Deep bi-directional features. |
| 94 | BERT Architecture (Encoder-only) | 60 min | Masked Language Modeling (MLM); Next Sentence Prediction (NSP); Fine-tuning head. |
| 95 | GPT Architecture (Decoder-only) | 60 min | Causal self-attention; Autoregressive generation; Large-scale pre-training. |
| 96 | Pre-training vs. Fine-tuning | 45 min | Two phases of model life; Knowledge acquisition \rightarrow Task specialization; Resource difference. |
| 97 | Prompt Engineering Core | 45 min | In-context learning; Few-shot prompting; Role of System Prompt. |
| 98 | Chain-of-Thought (CoT) Prompting | 60 min | Explicit step-by-step reasoning; Internal monologue; Revealing the "work." |
| 99 | Retrieval Augmented Generation (RAG) | 60 min | External knowledge base; Hybrid search (vector/keyword); Grounding/Factuality. |
| 100 | Hallucination Problem | 45 min | Generating convincing falsehoods; Sources of error; Mitigation strategies (RAG). |
| 101 | Knowledge Graphs (Conceptual) | 60 min | Nodes (Entities) & Edges (Relations); Structured knowledge representation; Triplets. |
| 102 | Knowledge Graph Embedding | 60 min | Representing entities/relations as vectors; Link prediction; Combining structure/semantics. |
| 103 | Semantic Parsing | 45 min | Mapping natural language to logical forms; Executable commands; Bridging language/action. |
| 104 | Text Classification | 30 min | Sentiment analysis example; Simple output layer; Feature representation. |
| 105 | Named Entity Recognition (NER) | 45 min | Identifying proper nouns/dates/locations; Sequence tagging; Contextual cues. |
| 106 | Abstractive Summarization | 60 min | Generating novel sentences; Encoder-Decoder with attention; Content preservation. |
| 107 | Sentiment Analysis | 30 min | Polarity detection (positive/negative); Intensity measurement; Aspect-Based concept. |
| 108 | Language Modeling (Auto-Regressive) | 45 min | Predicting the next word $P(w_i |
| 109 | Beam Search Decoding | 45 min | Exploring multiple hypotheses (paths); Pruning low-probability paths; Finding better sequences. |
| 110 | Temperature in Sampling | 30 min | Softmax smoothing; Controlling creativity/randomness; High vs. Low \tau. |
| 111 | Human Feedback (RLHF) | 60 min | Preference data collection; Reward model training; Aligning with human values. |
| 112 | Reward Model (RLHF) | 45 min | Training a model to predict human preference score; Ranking loss; Optimizing human approval. |
| 113 | Policy Optimization (PPO for RLHF) | 60 min | Using the RM to guide LLM finetuning; Proximal update constraint; Safety penalty. |
| 114 | Concept Abstraction | 60 min | Learning high-level, reusable concepts; Distilling features; Symbol grounding problem. |
| 115 | Symbolic AI (Conceptual) | 45 min | Rule-based systems; Explicit knowledge representation; Logical inference. |
| 116 | Neuro-Symbolic Integration | 60 min | Combining NN perception with symbolic reasoning; Strengths of both approaches; AGI path. |
| 117 | Logic Programming Basics | 45 min | Facts, Rules, and Queries; Deductive reasoning; Knowledge representation language (Prolog concept). |
| 118 | Commonsense Reasoning | 60 min | Implicit knowledge (gravity, intentions); Challenges in modeling; Dataset requirements. |
| 119 | Theory of Mind (Conceptual) | 60 min | Modeling others' beliefs and intentions; Nested beliefs (He thinks that I think); Social reasoning. |
| 120 | Embodied Language | 60 min | Language grounded in sensory/motor experience; Robotics integration; Situated communication. |
Phase 5: Vision and Perception (Modules 121-150)
Concepts for processing raw sensory data, necessary for grounding an AGI in the real world.
| # | Title | Duration | Subtopics |
|---|---|---|---|
| 121 | Image Representation (Pixels) | 30 min | RGB channels; Resolution impact; Tensor format (H \times W \times C). |
| 122 | Data Preprocessing for Images | 45 min | Normalization by mean/std; Resizing and cropping; Random jitter. |
| 123 | Edge Detection (Conceptual) | 45 min | Simple filters (Sobel); High-frequency features; Low-level visual cues. |
| 124 | Feature Hierarchy in CNN | 60 min | Edges \rightarrow Textures \rightarrow Parts \rightarrow Objects; Layer specialization; Visualization of filters. |
| 125 | Pre-trained CNNs (VGG/ResNet) | 45 min | Reusing feature extractors; Standard benchmarks; Depth vs. Performance. |
| 126 | Residual Connections (ResNet) | 45 min | Skip connections; Solving the degradation problem; Deeper network stability. |
| 127 | Inception Modules (GoogLeNet) | 45 min | Parallel filters (multiple sizes); Efficient computation; Sparse connections. |
| 128 | Image Classification Pipeline | 30 min | Data \rightarrow CNN \rightarrow Global Pooling \rightarrow Softmax; Output interpretation. |
| 129 | Object Localization | 45 min | Bounding box regression; IoU (Intersection over Union); Regression loss part. |
| 130 | Object Detection (R-CNN Family) | 60 min | Region proposals; Two-stage vs. One-stage concept; Speed/Accuracy tradeoff. |
| 131 | YOLO (You Only Look Once) | 45 min | Single-stage detection; Grid cell prediction; Speed for real-time applications. |
| 132 | Semantic Segmentation | 60 min | Pixel-wise classification; Fully Convolutional Networks (FCN); U-Net architecture (concept). |
| 133 | Instance Segmentation (Mask R-CNN) | 60 min | Pixel mask for each object instance; Classification, box, and mask outputs. |
| 134 | Vision Transformers (ViT) | 60 min | Treating image patches as tokens; Global self-attention; Scaling capabilities. |
| 135 | Generative Image Models (Diffusion) | 60 min | Forward process (adding noise); Reverse process (denoising); Iterative generation. |
| 136 | Denoising Autoencoders | 45 min | Reconstructing a clean image from a noisy input; Core of Diffusion models; Loss function. |
| 137 | Contrastive Learning (CLIP) | 60 min | Aligning image/text embeddings; Zero-shot image classification; Cross-modal mapping. |
| 138 | 3D Vision: Depth Estimation | 60 min | Monocular vs. Stereo; Predicting pixel depth; Applications in robotics/AR. |
| 139 | Point Clouds | 45 min | 3D data format; LiDAR/RGB-D sensor output; Registration concept. |
| 140 | 3D Object Detection | 45 min | Bounding box in 3D space; Challenges with sparsity; BEV (Bird's Eye View) concept. |
| 141 | SLAM (Simultaneous Localization and Mapping) | 60 min | Agent tracking its own position; Building a map of the environment; Loop closure. |
| 142 | Optical Flow | 45 min | Estimating pixel motion between frames; Tracking objects; Motion field. |
| 143 | Video Classification | 45 min | Spatio-temporal features; 3D Convolutions (conceptual); Action recognition. |
| 144 | Self-Supervised Learning (Vision) | 60 min | Pretext tasks (e.g., rotation prediction); Learning representations without labels; Data efficiency. |
| 145 | Domain Randomization | 45 min | Training in simulation with random parameters; Bridging Sim-to-Real; Robustness. |
| 146 | Perceptual Loss | 45 min | Using a pre-trained CNN to compare images; Feature space distance; Generating realistic images. |
| 147 | Style Transfer | 45 min | Content and Style loss; Separating features; Artistic applications. |
| 148 | Attention Mechanisms in Vision | 45 min | Channels, spatial, and self-attention; Focusing computation; Interpretable areas. |
| 149 | Visual Question Answering (VQA) | 60 min | Multi-modal fusion; Answering questions based on an image; Joint emb