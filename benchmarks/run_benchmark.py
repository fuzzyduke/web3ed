import requests
import json
import time
import os

# Configuration
NVIDIA_KEY = "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"
ASI1_KEY = "sk_e0b8e522f3b5416c91e70d2bf5afe1a4c930984639e6452f98a7a2955adf7425"

NVIDIA_URL = "https://integrate.api.nvidia.com/v1/chat/completions"
ASI1_URL = "https://api.asi1.ai/v1/chat/completions"

NVIDIA_MODEL = "nvidia/nemotron-3-super-120b-a12b"
ASI1_MODEL = "asi1"

QUESTIONS = [
    {
        "id": "Q1_LOGIC",
        "category": "Reasoning",
        "prompt": "A bat and a ball cost $1.10 in total. The bat costs $1.00 more than the ball. How much does the ball cost? Show your reasoning."
    },
    {
        "id": "Q2_WEB3",
        "category": "Web3 Technical",
        "prompt": "Explain the difference between a Reproducible Execution Environment (REE) and a Trusted Execution Environment (TEE) in the context of decentralized AI compute like Gensyn. Which one does Gensyn favor and why?"
    },
    {
        "id": "Q3_CODE",
        "category": "Coding",
        "prompt": "Write a Python script using Playwright to scrape the titles and URLs of all technical blog posts from the Gensyn blog (https://www.gensyn.ai/blog). Ensure it handles infinite scroll if applicable."
    },
    {
        "id": "Q4_VERIFICATION",
        "category": "Protocol Security",
        "prompt": "Evaluate the security risks of the 'Bisection Game' in probabilistic verification for ML training. Can a malicious solver find a path to pass verification without performing the full computation? Describe the game theory involved."
    },
    {
        "id": "Q5_CREATIVE",
        "category": "Technical Writing",
        "prompt": "Draft a compelling, high-bandwidth technical introduction for a blog post about 'The Intersection of Verifiable Compute and Foundation Models.' Use a tone that appeals to both researchers and infrastructure engineers."
    }
]

def call_model(url, key, model, prompt):
    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2,
        "max_tokens": 2048
    }
    
    start_time = time.time()
    try:
        response = requests.post(url, headers=headers, json=data)
        elapsed = time.time() - start_time
        if response.status_code == 200:
            content = response.json()['choices'][0]['message']['content']
            return {"status": "success", "content": content, "latency": elapsed}
        else:
            return {"status": "error", "message": f"{response.status_code}: {response.text}", "latency": elapsed}
    except Exception as e:
        return {"status": "exception", "message": str(e), "latency": time.time() - start_time}

def run_benchmarks():
    results = []
    
    for q in QUESTIONS:
        print(f"\n--- Running {q['id']} ({q['category']}) ---")
        
        print(f"Calling Nemotron...")
        nemotron_res = call_model(NVIDIA_URL, NVIDIA_KEY, NVIDIA_MODEL, q['prompt'])
        
        print(f"Calling ASI1...")
        asi1_res = call_model(ASI1_URL, ASI1_KEY, ASI1_MODEL, q['prompt'])
        
        results.append({
            "question": q,
            "nemotron": nemotron_res,
            "asi1": asi1_res
        })
        
        # Avoid rate limits if any
        time.sleep(1)

    # Save results to markdown
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"benchmarks/comparison_{timestamp}.md"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# Model Benchmark Comparison: Nemotron-4-340B vs ASI1\n")
        f.write(f"**Date:** {time.strftime('%Y-%m-%d')}\n\n")
        
        for r in results:
            q = r['question']
            f.write(f"## {q['id']}: {q['category']}\n")
            f.write(f"**Prompt:** {q['prompt']}\n\n")
            
            f.write(f"### 🟢 Nemotron-4-340B\n")
            f.write(f"*Latency: {r['nemotron']['latency']:.2f}s*\n\n")
            nemotron_content = r['nemotron'].get('content', f"❌ ERROR: {r['nemotron'].get('message', 'Unknown error')}")
            f.write(f"{nemotron_content}\n\n")
            
            f.write(f"### 🔵 ASI1\n")
            f.write(f"*Latency: {r['asi1']['latency']:.2f}s*\n\n")
            asi1_content = r['asi1'].get('content', f"❌ ERROR: {r['asi1'].get('message', 'Unknown error')}")
            f.write(f"{asi1_content}\n\n")
            f.write(f"---\n\n")
            
    print(f"\nBenchmark complete! Results saved to {filename}")

if __name__ == "__main__":
    run_benchmarks()
