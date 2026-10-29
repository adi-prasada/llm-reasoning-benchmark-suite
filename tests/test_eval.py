from src.evaluator import ReasoningEvaluator

def test_evaluator_scoring():
    ev = ReasoningEvaluator()
    res = ev.evaluate_response("25", "The value is \\boxed{25}")
    assert res["passed"] is True
    assert res["boxed_match"] is True
