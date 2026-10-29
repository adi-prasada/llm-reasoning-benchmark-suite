# LLM Reasoning Benchmark Suite

An enterprise-ready benchmarking harness for evaluating large language model (LLM) performance across logical deduction, math problem solving, multi-turn prompt consistency, and grounded factual accuracy.

## Capabilities
- **Step-by-step Verification**: Evaluates chain-of-thought (CoT) trajectories for logical continuity.
- **Automated Accuracy Scorer**: Strict string extraction, regex verification, and normalized numerical tolerance comparisons.
- **Robust Metrics**: Pass@1, Consistency Score across temperature variations, and Token Efficiency Index.

## Usage
```bash
pip install -r requirements.txt
python main.py
pytest tests/
```
