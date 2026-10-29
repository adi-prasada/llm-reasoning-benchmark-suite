from typing import List, Dict, Any
import re

class ReasoningEvaluator:
    def __init__(self):
        pass

    def evaluate_response(self, expected_answer: str, model_output: str) -> Dict[str, Any]:
        cleaned_expected = str(expected_answer).strip().lower()
        cleaned_output = str(model_output).strip().lower()
        
        exact_match = cleaned_expected == cleaned_output
        boxed_match = False
        boxed_candidates = re.findall(r'\\boxed\{([^}]+)\}', model_output)
        if boxed_candidates:
            boxed_match = any(c.strip().lower() == cleaned_expected for c in boxed_candidates)
            
        final_answer_match = cleaned_expected in cleaned_output
        passed = exact_match or boxed_match or final_answer_match
        
        return {
            "passed": passed,
            "exact_match": exact_match,
            "boxed_match": boxed_match,
            "reasoning_length_chars": len(model_output),
            "step_count_estimate": model_output.count("\n") + 1
        }
        
    def run_benchmark_batch(self, test_cases: List[Dict[str, str]]) -> Dict[str, Any]:
        results = [self.evaluate_response(tc["expected"], tc["prediction"]) for tc in test_cases]
        pass_count = sum(1 for r in results if r["passed"])
        total = len(results)
        
        return {
            "total_samples": total,
            "passed_samples": pass_count,
            "accuracy_pct": round(100.0 * pass_count / total, 2) if total > 0 else 0.0,
            "details": results
        }
