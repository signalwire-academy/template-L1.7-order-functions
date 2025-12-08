# Lab 1.7: Order Lookup Functions

**Duration:** 60 minutes
**Level:** 1

## Objectives

Complete this lab to demonstrate your understanding of the concepts covered.

## Prerequisites

- Completed previous labs
- Python 3.10+ with signalwire-agents installed
- Virtual environment activated

## Instructions

### 1. Set Up Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Implement Your Solution

Edit `solution/agent.py` according to the lab requirements.

### 3. Test Locally

```bash
# List available functions
swaig-test solution/agent.py --list-tools

# Check SWML output
swaig-test solution/agent.py --dump-swml
```

### 4. Submit

```bash
git add solution/agent.py
git commit -m "Complete Lab 1.7: Order Lookup Functions"
git push
```

## Grading

| Check | Points |
|-------|--------|
| Agent Instantiation | 10 |
| SWML Generation | 10 |
| get_order_status function | 15 |
| find_orders_by_email function | 10 |
| cancel_order function | 10 |
| Test: Order 12345 found | 15 |
| Test: Order 99999 not found | 10 |
| Test: Cancel order 67890 | 20 |
| **Total** | **100** |

**Passing Score:** 70%

## Reference

See `reference/starter.py` for a boilerplate template.

---

## Next Assignment

Ready for certification? [**Start Level 1 Written Exam**](https://classroom.github.com/a/mJzD3NS1)

---

*SignalWire AI Agents Certification*
