# Overview


<p align="center">

  <img src="image/title.png" width="800px"/>

</p>

<p align="center">

   🌐 <a href="https://hongqiong12.github.io/USB-SafeBench/" target="_blank">Website</a> • 🤗 <a href="https://huggingface.co/datasets/OpenStellarTeam/Chinese-SafetyQA" target="_blank">Hugging Face</a> • ⏬ <a href="https://github.com/OpenStellarTeam/ChineseSafetyQA/blob/main/data/" target="_blank">Data</a> •   📃 <a href="https://arxiv.org/abs/2412.15265" target="_blank">Paper</a> •   📊 <a href="http://47.109.32.164/safety" target="_blank">Leader Board</a>  <br>  <a href="https://github.com/OpenStellarTeam/ChineseSafetyQA/blob/main/README_zh.md">   中文</a> | <a href="https://github.com/OpenStellarTeam/ChineseSafetyQA/blob/main/README.md">English</a> 

</p> 




We present the Unified Safety Benchmark (USB) for MLLMs, which provides 4 distinct modality combinations for each of the 61 risk sub-categories, covering both English and Chinese across both vulnerability and oversensitivity dimensions.

**USB-SafeBench's Features**

- **Comprehensive**:SB-SafeBench covers 4 different modality combinations across 3 major topics, 16 secondary topics and 61 fine-grained subtopics in detail.
- **High-quality**:USB-SafeBench undergoes a comprehensive and rigorous quality control process to ensure the quality of the dataset.
- **Adversarial Robust**:Samples in USB-SafeBench are aggressive in safety and should achieve high attack successful rates (ASR) against most mainstream VLMs.

---

**Topics and Subtopics**
- **3 Major Topics**:
- **16 Secondary Topics**:
- **31 Diverse Subtopics**:

---

**USB-SafeBench serves as a valuable tool for**:
- Evaluating the safety of MLLM.

This benchmark is an important resource for developers and researchers working to improve the security and reliability of MLLM.

[//]: # (Please visit our [website]&#40;https://openstellarteam.github.io/ChineseSafetyQA/&#41;)

[//]: # (or check our [paper]&#40;https://arxiv.org/abs/2412.15265&#41; for more details.)

[//]: # (This is the evaluation repository for Chinese SafetyQA)

<p align="center">
  <img src="image/category_en.png" width="700px"/>
</p>


---

[//]: # (## 🆕 News)

[//]: # ()
[//]: # (- **\[2024.12.11\]** We have released the Chinese SafetyQA dataset)

[//]: # (  🤗[huggingface]&#40;https://huggingface.co/datasets/OpenStellarTeam/Chinese-SafetyQA&#41; 🚀🚀🚀)

[//]: # ()
[//]: # (---)

## 💫 Introduction

Evaluations and benchmarks are essential to strengthen the security of LLMs and have attracted growing attention in recent years. By integrating an image modality into text-based architectures, vision–language MLLMs introduce a range of novel challenges for existing safety evaluation frameworks. Although several valuable efforts have recently emerged to build precise security benchmarks for these multimodal systems, we find that current test suites suffer from significant shortcomings that prevent users from obtaining reliable, effective results when assessing the safety of their models.

**Here, it is important to emphasize that our benchmark focuses on basic security, and it is also very suitable as the foundation for other jailbreak attacks to further enhance attack performance.**

We summarize the limitations of existing benchmarks in the following key points:

* **Benchmark Data Quality and Coverage Are Inadequate.** Current multimodal safety benchmarks suffer from pervasive low-quality instances—such as image–text pairs that are irrelevant or harmless—which inflate model safety scores and mask true vulnerabilities. Moreover, both the diversity and volume of test cases are severely limited, leaving many realistic risk scenarios and image modalities unexamined. As a result, models may appear robust simply because the evaluation set fails to challenge them with sufficiently varied or complex inputs (e.g. only XX image types and YY risk categories are represented).

* **Modal Risk Combinations Are Overlooked.** Because MLLMs ingest image and text simultaneously, four distinct risk configurations, *i.e.*, Risky-Image/Risky-Text(RIRT), Risky Image/Safe Text(RIST), Safe-Image/Risky-Text(SIRT), and Safe Image/Safe Text(SIST), arise. Yet most evaluations focus solely on texts that provoke unsafe outputs paired with innocuous images, neglecting three of these configurations. Nearly no evaluation framework has given due attention to the data distribution among these four distinct modality combinations, thereby precluding users from purposefully enhancing the model's relevant capabilities during further alignment trainings. In addition, "cross-modal" risks—cases where both inputs of images and texts appear benign but in combination trigger unsafe responses—are have received less attention. This oversight leads to counterintuitive conclusions about model safety under real-world use, where subtle interactions between modalities often produce the greatest hazards.

* **Difficulty Calibration and Result Consistency Are Lacking.** Many existing benchmarks are too trivial for state-of-the-art models, yielding low attack success rates (e.g. <5% for some MLLMs) that conceal meaningful differences in robustness. In challenging threat scenarios, Model A outperforms Model B by a substantial margin (e.g. XX% vs. XX%), despite similar scores on simplistic tests. Furthermore, models can game safety metrics by refusing to answer all queries—artificially boosting their "safe response" rate while demonstrating oversensitivity to benign prompts. Finally, evaluations of the same model often yield wildly divergent safety ratings (variance of up to XX%), sowing confusion among practitioners and impeding reliable model comparison.

---

[//]: # ()
[//]: # (## 📊 Leaderboard)

[//]: # ()
[//]: # (For More Info：  [📊]&#40;http://47.109.32.164/safety/&#41;)

[//]: # ()
[//]: # (<p align="center">)

[//]: # (  <img src="image/leader_board.png" width="800px"/>)

[//]: # (</p>)

[//]: # ()
[//]: # (---)

[//]: # ()
[//]: # (## 🛠️ Setup)

[//]: # ()
[//]: # (Due to optional dependencies, we do not provide a unified setup. Instead, we offer optional instructions for querying)

[//]: # (different Large Language Models &#40;LLMs&#41;.)

[//]: # ()
[//]: # (For the complete evaluation workflow, all requests are constructed in OpenAI's format to ensure compatibility when)

[//]: # (calling various LLMs.)

[//]: # ()
[//]: # (For the [OpenAI API]&#40;https://pypi.org/project/openai/&#41;:)

[//]: # ()
[//]: # (```bash)

[//]: # (pip install openai)

[//]: # (```)

[//]: # ()
[//]: # (---)

[//]: # ()
[//]: # (## ⚖️ Evals)

[//]: # ()
[//]: # (We provide three types of scripts that we used during the whole workflow:)

[//]: # ()
[//]: # (### Call OpenAI's GPT models to get log probability.)

[//]: # ()
[//]: # (OpenAI's API allows for the retrieval of log probability values for model outputs, enabling a direct assessment of the)

[//]: # (uncertainty in model responses. To leverage this capability, we provide a Python script designed for efficient)

[//]: # (batch-calling of the API. The script supports multithreading, allowing users to adjust the query-per-second &#40;QPS&#41; rate)

[//]: # (by specifying the number of threads.)

[//]: # ()
[//]: # (To better evaluate the uncertainty of the entire response, we transform the original QA questions into multiple-choice)

[//]: # (questions &#40;MCQs&#41;. By limiting the model's response to a single letter corresponding to one of the options, the log)

[//]: # (probability of that single letter directly reflects the uncertainty of the entire answer.)

[//]: # ()
[//]: # (Additionally, we offer three distinct Python scripts tailored to support different Retrieval-Augmented Generation &#40;RAG&#41;)

[//]: # (triggering methods: No RAG, Passive RAG, and Active RAG. The details of these scripts are as follows:)

[//]: # ()
[//]: # (```)

[//]: # (~/batch_scripts/)

[//]: # (└── query_openai_model_get_logprob/)

[//]: # (    ├── batch_active_rag.py)

[//]: # (    ├── batch_passive_rag.py)

[//]: # (    ├── batch_no_rag.py)

[//]: # (```)

[//]: # ()
[//]: # (**How to Use These Scripts**)

[//]: # ()
[//]: # (1. Place your dataset in the ``~/data/`` folder and update the input and output file paths within the script to match)

[//]: # (   your data.)

[//]: # (2. Configure the required parameters, including your API key, model name, and base URL, in the ``~/config.json`` file.)

[//]: # (3. Execute the script using the following command:)

[//]: # ()
[//]: # (```bash)

[//]: # (python3 batch_scripts/query_openai_model_get_logprob/batch_active_rag.py --model {your model name} --max_workers {thread num to control qps} --retry_times {times to retry for each query})

[//]: # (# example: )

[//]: # (python3 batch_scripts/query_openai_model_get_logprob/batch_active_rag.py --model gpt-4o-mini --max_workers 3 --retry_times 3)

[//]: # (```)

[//]: # ()
[//]: # (**Input Data Schema**)

[//]: # (The input data should follow the structure below:)

[//]: # ()
[//]: # (1. question: The question to be asked.  )

[//]: # (   Example: "What is the capital of France?")

[//]: # (2. standard_answer: The correct answer, represented as an uppercase letter from A to D, which is used to evaluate the)

[//]: # (   model's accuracy.  )

[//]: # (   Example: "B")

[//]: # (3. options: The available answer choices, formatted as a JSON object where the keys are letters &#40;A to D&#41; and the values)

[//]: # (   are the corresponding options.  )

[//]: # (   Example:)

[//]: # ()
[//]: # (```json)

[//]: # ({)

[//]: # (  "A": "Berlin",)

[//]: # (  "B": "Paris",)

[//]: # (  "C": "Madrid",)

[//]: # (  "D": "Rome")

[//]: # (})

[//]: # (```)

[//]: # ()
[//]: # (To utilize RAG, you need to implement a custom RAG query function. The function's parameters and return values should)

[//]: # (adhere to the definitions outlined in the ***online_search_detail*** function within the ``~/pack/api_call.py`` script.)

[//]: # ()
[//]: # (---)

[//]: # ()
[//]: # (### Batch-Calling Various LLMs)

[//]: # ()
[//]: # (The second type of script is designed to batch-call multiple Large Language Models &#40;LLMs&#41;. The prompts used throughout)

[//]: # (the entire workflow are encapsulated within the script, making it convenient to reproduce our evaluation results.)

[//]: # ()
[//]: # (This script provides the following features:)

[//]: # ()
[//]: # (1. Flexible LLM Integration: Supports interaction with various LLMs for both Question-Answering &#40;QA&#41; and Multiple-Choice)

[//]: # (   Questions &#40;MCQ&#41; tasks.)

[//]: # (2. Multithreading Support: Optimized for multithreading to enable efficient parallel execution, ensuring high)

[//]: # (   performance when handling large query volumes.)

[//]: # (3. Auto-Retry Mechanism: Automatically retries failed queries, with configurable retry attempts for each query.)

[//]: # ()
[//]: # (The path of these scripts are as follows:)

[//]: # ()
[//]: # (```)

[//]: # (~/batch_scripts/)

[//]: # (└── query_general_model_get_response/)

[//]: # (    ├── batch_call_model.py)

[//]: # (```)

[//]: # ()
[//]: # (**How to Use These Scripts**)

[//]: # ()
[//]: # (1. Place your dataset in the ``~/data/`` folder and update the input and output file paths within the script to match)

[//]: # (   your data.)

[//]: # (2. Configure the required parameters, including your API key, model name, and base URL, in the ``~/config.json`` file.)

[//]: # (3. Execute the script using the following command:)

[//]: # ()
[//]: # (```bash)

[//]: # (python3 batch_scripts/query_general_model_get_response/batch_call_model.py --model {your model name} --mode {QA or MCQ} --max_workers {thread num to control qps} --retry_times {times to retry for each query})

[//]: # (# example: )

[//]: # (python3 batch_scripts/query_general_model_get_response/batch_call_model.py --model gpt-4o-mini --mode QA --max_workers 3 --retry_times 3)

[//]: # (```)

[//]: # ()
[//]: # (**Input Data Schema**)

[//]: # (The input data should follow the structure below:)

[//]: # ()
[//]: # (1. question: The question to be asked.  )

[//]: # (   Example: "What is the capital of France?")

[//]: # (2. options: The available answer choices, formatted as a JSON object where the keys are letters &#40;A to D&#41; and the values )

[//]: # (   are the corresponding options. **only needed for MCQ tasks**.  )

[//]: # (   Example:)

[//]: # ()
[//]: # (```json)

[//]: # ({)

[//]: # (  "A": "Berlin",)

[//]: # (  "B": "Paris",)

[//]: # (  "C": "Madrid",)

[//]: # (  "D": "Rome")

[//]: # (})

[//]: # (```)

[//]: # ()
[//]: # (---)

[//]: # ()
[//]: # (### Evaluate the Model Response and Compute Metrics)

[//]: # ()
[//]: # (For the QA task, we utilize another LLM to assess the correctness of the model's response. The evaluation script is)

[//]: # (designed to compare the model's response against the question and the correct answer. This script includes our)

[//]: # (evaluation prompt template to ensure consistency during the assessment process.)

[//]: # ()
[//]: # (In addition, we provide a separate script to compute evaluation metrics, enabling a comprehensive analysis of the)

[//]: # (model's performance.)

[//]: # ()
[//]: # (The paths to these scripts are as follows:)

[//]: # ()
[//]: # (```)

[//]: # (~/batch_scripts/)

[//]: # (└── evaluation/)

[//]: # (    ├── metrics.py)

[//]: # (    ├── simple_qa_evaluate.py)

[//]: # (```)

[//]: # ()
[//]: # (**How to Use These Scripts**)

[//]: # ()
[//]: # (1. Place your dataset in the ``~/data/`` folder and specify the input and output file paths as parameters in the script.)

[//]: # (2. Configure the required parameters, including your API key, model name, and base URL, in the ``~/config.json`` file.)

[//]: # (3. Execute the script using the following command:)

[//]: # ()
[//]: # (```bash)

[//]: # (# Evaluate Model Response)

[//]: # (python3 batch_scripts/evaluation/simple_qa_evaluate.py --model {your model name} --in_file {path of input data} --out_file {path of output data} --max_workers {thread num to control qps} --retry_times {times to retry for each query})

[//]: # ()
[//]: # (# Compute Metrics)

[//]: # (python3 batch_scripts/evaluation/metrics.py --in_file {path of input data} --out_file {path of output data})

[//]: # (```)

[//]: # ()
[//]: # (**Input Data Schema**)

[//]: # ()
[//]: # (For `simple_qa_evaluate.py`:)

[//]: # ()
[//]: # (1. query: The question to be asked.  )

[//]: # (   Example: "What is the capital of France?")

[//]: # (2. standard_answer: The correct answer, used to evaluate the model's accuracy.  )

[//]: # (   Example: "Paris")

[//]: # (3. model_answer: The response generated by the model.  )

[//]: # (   Example: "Paris")

[//]: # ()
[//]: # (---)

[//]: # ()
[//]: # (For `metrics.py`:)

[//]: # ()
[//]: # (1. question: The specific question being evaluated.  )

[//]: # (   Example: "What is the capital of France?")

[//]: # (2. cate: The category of the question.  )

[//]: # (   Example: "伦理道德风险-个人伦理类-利己利他类")

[//]: # (3. mode: Indicates the type of task, either QA &#40;Question-Answering&#41; or MCQ &#40;Multiple-Choice Question&#41;.  )

[//]: # (   Example: "QA")

[//]: # (4. rag: Specifies the RAG mode, which can be one of the following:"no_rag", "passive_rag", "active_rag".  )

[//]: # (   Example: "no_rag")

[//]: # (5. model: The name of the model being evaluated.  )

[//]: # (   Example: "gpt-4")

[//]: # (6. value_type: Specifies the type of value being recorded. It can be one of the following:    )

[//]: # (   * "model_answer": The model's response.  )

[//]: # (   * "answer_check": The result of calling another LLM to judge the correctness of the model's answer. "A": Correct. "B": Incorrect. "C": Not applicable.  )

[//]: # ()
[//]: # (    Example: "answer_check")

[//]: # (7. value: The actual value of the record.  )

[//]: # (   Example: "Paris" &#40;for model_answer&#41; or "A" &#40;for answer_check&#41;.)

[//]: # (## Contact)

[//]: # (If you are interested in our work, please contact us at `tanyingshui.tys@taobao.com`)

## Citation

Please cite our paper if you use our dataset.

[//]: # (```)

[//]: # (@misc{tan2024chinesesafetyqasafetyshortform,)

[//]: # (      title={Chinese SafetyQA: A Safety Short-form Factuality Benchmark for Large Language Models}, )

[//]: # (      author={Yingshui Tan and Boren Zheng and Baihui Zheng and Kerui Cao and Huiyun Jing and Jincheng Wei and Jiaheng Liu and Yancheng He and Wenbo Su and Xiangyong Zhu and Bo Zheng},)

[//]: # (      year={2024},)

[//]: # (      eprint={2412.15265},)

[//]: # (      archivePrefix={arXiv},)

[//]: # (      primaryClass={cs.CL},)

[//]: # (      url={https://arxiv.org/abs/2412.15265}, )

[//]: # (})

[//]: # (```)

