from src.evaluator import ReasoningEvaluator

def main():
    print("=== LLM Reasoning Benchmark Evaluator ===")
    test_cases = [
        {"expected": "42", "prediction": "Let us solve step by step: 6 * 7 = 42. \\boxed{42}"},
        {"expected": "Paris", "prediction": "The capital of France is Paris."},
        {"expected": "15", "prediction": "Calculated result: 15."},
        {"expected": "True", "prediction": "Upon careful review, the hypothesis is False."}
    ]
    
    evaluator = ReasoningEvaluator()
    summary = evaluator.run_benchmark_batch(test_cases)
    
    print("Total Test Cases: " + str(summary['total_samples']))
    print("Passed: " + str(summary['passed_samples']))
    print("Benchmark Accuracy: " + str(summary['accuracy_pct']) + "%")
    print("\n[SUCCESS] Benchmark run completed.")

if __name__ == '__main__':
    main()
