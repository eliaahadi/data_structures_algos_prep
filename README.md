# 2-week DSA refresh plan for AI and cloud solutions architect roles
- Python-focused
- Designed for RAG, GenAI, and customer-facing solution architecture
- Generated January 05, 2026

## What this plan optimizes for
You are targeting AI engineer / AI architect / cloud solutions architect / technical program roles that typically require:

- Fluency with practical DSA patterns (top-k, dedupe, windows, graphs, caching)
- Ability to explain and implement key parts of RAG (indexing, retrieval, rerank, grounding, evaluation)
- Comfort with APIs, data ecosystems, and building POCs (often customer-facing)
- Governance mindset (privacy, security, data handling, reliability)

## Daily workflow (60–90 minutes)
Use the same structure every day so you build speed and recall.
1. Warmup (10 min): implement one core primitive from memory
2. Timed coding (35–45 min): 1–2 interview problems
3. AI/RAG mini-lab (15–25 min): small applied exercise tied to the day’s DSA
4. Talk track (5–10 min): explain solution + tradeoffs like an architect

## Rules of engagement
Code in Python with type hints. Prefer readable patterns over clever tricks.

After each problem, write a 5-line template: pattern, invariants, complexity, edge cases, when to use.

Keep a running mistake log (off-by-one, wrong invariant, forgot tie-breaking, etc.).

For RAG: always mention latency vs accuracy vs cost, and where you add monitoring/evals.

## Two-week schedule overview
Week 1 builds core speed on the patterns that show up constantly in retrieval pipelines. 
Week 2 adds graphs, caching, and end-to-end RAG system thinking.

### Day 1: Hashmaps for retrieval primitives
DSA focus:
Membership, counting, dedupe; build the habit of O(1) lookups and clean invariants.

Timed problems (pick 2):
Two Sum
Group Anagrams
Valid Anagram (speed rep)

AI/RAG mini-lab:
Implement a tiny document store keyed by doc_id; support add_doc, get_doc, delete_doc.
Add a metadata filter (e.g., {source:'policy', year:2025}) using hashmaps/sets.

Architect talk track (say this out loud):
Hash maps show up everywhere in RAG: doc stores, metadata filters, dedupe, cache keys.

Tradeoff: memory overhead vs speed; discuss collision/normalization for stable keys.

Output to save:
Mistake log entry + 2 templates
A doc_store.py snippet (20–40 lines)

### Day 2: Sliding window and chunking
DSA focus:
Two pointers and window invariants for strings/arrays.

Timed problems (pick 2):
Longest Substring Without Repeating Characters
Minimum Window Substring (stretch)

AI/RAG mini-lab:
Write a chunker(text, chunk_size, overlap) that yields chunks with offsets.
Compute coverage and show how overlap impacts recall vs cost.

Architect talk track (say this out loud):
Chunking is a windowing problem: choose size/overlap based on recall and token budget.

Mention evaluation: measure answer accuracy vs latency as chunking changes.

Output to save:
chunker.py with tests
A short note: chunk_size/overlap guidelines

### Day 3: Sorting + intervals for provenance
DSA focus:
Sort, merge, and normalize ranges (high frequency in data work).

Timed problems (pick 2):
Merge Intervals
Insert Interval

AI/RAG mini-lab:
Given chunk offset ranges, merge overlapping spans per source document.

Add provenance: keep (doc_id, start, end) and merge only within same doc.

Architect talk track (say this out loud):
Provenance matters for grounded answers: store offsets so you can cite sources.
Discuss correctness: merging rules, tie-breaking, and preserving citations.

Output to save:
provenance_merge.py
1-page provenance schema sketch

### Day 4: Heaps for top-k retrieval
DSA focus:
Priority queues and top-k patterns; tie-breaking and stable results.

Timed problems (pick 2):
Top K Frequent Elements
Kth Largest Element in an Array

AI/RAG mini-lab:
Simulate retrieval: given scores for chunks, return top_k with deterministic tie-break.
Add optional diversity constraint: at most 2 chunks per doc (simple rule).

Architect talk track (say this out loud):
Retrieval is top-k; reranking is often top-k again. Heaps keep latency reasonable.

Explain tradeoffs: heap vs sort; top-k per doc (diversity) vs raw relevance.

Output to save:
topk.py
Notes on tie-breaking + determinism

### Day 5: BFS/DFS basics (graph-lite)
DSA focus:
Traversal patterns you’ll reuse in pipeline DAGs and dependency graphs.

Timed problems (pick 2):
Number of Islands
Clone Graph (optional)

AI/RAG mini-lab:
Model your RAG pipeline as a DAG (ingest -> chunk -> embed -> index -> retrieve -> rerank -> generate -> eval).
Write a validator that checks connectivity and that required nodes exist.

Architect talk track (say this out loud):
Architect framing: pipelines are graphs. You need observability at each node.
Discuss failure domains: partial failures, retries, idempotency per stage.

Output to save:
pipeline_dag.md sketch
dag_validate.py (simple)

### Day 6: Stacks/queues for streaming + backpressure
DSA focus:
Use stacks for parsing; queues for producers/consumers.

Timed problems (pick 2):
Valid Parentheses
Daily Temperatures (monotonic stack)

AI/RAG mini-lab:
Build a simple in-memory queue that batches items (e.g., chunks) into embedding calls.

Add backpressure: if queue too big, drop/slowdown with a clear policy.

Architect talk track (say this out loud):
Streaming ingestion is queue semantics + batching + rate limits.
Mention operational policies: retries, DLQ (dead-letter), and idempotency keys.

Output to save:
stream_queue.py
Batching policy note (latency vs throughput)

### Day 7: Week 1 checkpoint (mock + recap)
DSA focus:
Speed + clarity. Re-do problems you missed until you can solve them cleanly in 15 minutes.

Timed problems (pick 2):
Redo 3 hardest from Days 1–6
One new mixed problem (your choice)

AI/RAG mini-lab:
Write RAG overview from memory: components, data flow, where evaluation fits.
Create a 60-second explanation of chunking + top-k retrieval + reranking.

Architect talk track (say this out loud):
Hiring signal: you can explain tradeoffs and you can still code under time pressure.
Keep it crisp: what, why, constraints, tradeoffs, monitoring.

Output to save:
1-page RAG talk track
Updated mistake log

### Day 8: Binary search (often hidden in latency/cost constraints)
DSA focus:
Binary search on answer; clear monotonic predicate.

Timed problems (pick 2):
Koko Eating Bananas (binary search on answer)
Find Minimum in Rotated Sorted Array

AI/RAG mini-lab:
Define a monotonic predicate: does this chunk size fit within token/latency budget?
Binary search chunk_size to find the max size under constraints (conceptual + small sim).

Architect talk track (say this out loud):
Architect framing: tunables (chunk size, top-k, rerank-k) should be driven by constraints and evals.
Mention A/B tests and safe rollout.

Output to save:
binary_search_template.md
small_sim.py (predicate + search)

### Day 9: LRU cache (retrieval caching, embeddings caching)
DSA focus:
Classic system DSA: hashmap + doubly linked list.

Timed problems (pick 2):
LRU Cache
AI/RAG mini-lab:
Decide what to cache in RAG: embeddings, retrieval results, rerank results, final answers.
Design invalidation when documents change (versioned index + cache keys).

Architect talk track (say this out loud):
Explain: caching cuts latency/cost but risks staleness. Solve via versioning + TTL + revalidation.
Mention privacy: avoid caching sensitive prompts unless policy allows it.

Output to save:
lru_cache.py
Cache key strategy note

### Day 10: Shortest paths and routing decisions
DSA focus:
BFS shortest path; when you need Dijkstra conceptually.

Timed problems (pick 2):
Shortest Path in Binary Matrix
Word Ladder (stretch)

AI/RAG mini-lab:
Tool routing: represent tools as nodes and transitions as edges; find minimal-step plan to answer.
Add constraints: forbidden tools or required approvals.
Architect talk track (say this out loud):
Architect framing: orchestration is graph routing with constraints and observability.
Discuss guardrails: tool allowlists, data boundaries, and audit logging.
Output to save:
routing_bfs.py
Tooling policy checklist

### Day 11: Union-find for dedupe and entity resolution
DSA focus:
Connected components and merging records reliably.

Timed problems (pick 2):
Accounts Merge
Number of Connected Components

AI/RAG mini-lab:
Near-duplicate chunk dedupe: connect chunks if similarity > threshold, union them.
Pick a representative chunk and preserve links to all originals for traceability.

Architect talk track (say this out loud):
Explain thresholding tradeoff: aggressive dedupe reduces cost but can harm recall.
Mention evaluation: measure retrieval recall@k and answer quality after dedupe.
Output to save:
union_find.py
Dedupe strategy note (threshold, drift)

### Day 12: DP basics for token-budget selection
DSA focus:
1D DP and choose-best-under-constraint thinking.

Timed problems (pick 2):
House Robber
Coin Change (stretch)

AI/RAG mini-lab:
Token budget selection: choose which passages to include in context under max tokens.
Use a simplified DP/greedy comparison; discuss why exact knapsack may be overkill in prod.

Architect talk track (say this out loud):
Architect framing: constraints (token budget) require selection policies (greedy, DP-like heuristics).
Discuss reliability: deterministic selection and explainability of why passages were chosen.
Output to save:
context_select.md
A simple selector function in Python

### Day 13: End-to-end RAG mini build (local)
DSA focus:
Tie the DSA together into a working skeleton you can discuss.
Timed problems (pick 2):
(No new LeetCode today) Do 1 speed rep of Top K Frequent if time
AI/RAG mini-lab:
Build a local RAG skeleton: ingest -> chunk -> embed (mock) -> index (simple) -> retrieve top-k -> generate (mock).
Add logging for each stage and a basic eval harness (precision@k on toy queries).
Architect talk track (say this out loud):
Explain components and boundaries: where state lives, what’s cached, what’s versioned.
Discuss production concerns: latency, retries, rate limits, security, observability.
Output to save:
rag_skeleton/ folder outline
eval_harness.py
README talk track

### Day 14: Final mock interview day (coding + architecture)
DSA focus:
Simulate the interview: one coding screen + one system-design explanation.

Timed problems (pick 2):
Mock coding: LRU Cache OR Course Schedule (choose based on weakness)
Speed rep: Merge Intervals

AI/RAG mini-lab:
Whiteboard an enterprise RAG design: data sources, ingestion, vector store, reranker, LLM, guardrails, eval, monitoring.
Add privacy/security: PII handling, data retention, access controls, prompt logging policy.

Architect talk track (say this out loud):
Use a structured narrative: requirements -> design -> tradeoffs -> failure modes -> monitoring -> rollout.
End with metrics: retrieval recall@k, MRR, latency p95, cost per query, hallucination rate proxies.
Output to save:
2-page architecture notes
A 90-second tell-me-about-RAG script

## Quick reference: the patterns to memorize
Keep this page open while practicing. These are reusable templates.
- Hashmap counting: freq = {}; for x in arr: freq[x] = freq.get(x, 0) + 1
- Sliding window: Move right; while invalid: move left; track best
- Intervals: Sort by start; merge when cur.start <= prev.end
- Top-k heap: Push/pop; keep size k; define deterministic tie-break
- BFS/DFS: Visited set; queue/stack; process neighbors
- LRU cache: Hashmap + doubly-linked list; O(1) get/put
- Union-find: parent/rank; union by rank; path compression

## RAG essentials (what you should be able to explain)
- Ingestion: document sources, parsing, cleaning, dedupe, metadata
- Chunking: size/overlap strategy tied to retrieval/eval and token budget
- Embeddings + index: versioning, refresh strategy, backfills
- Retrieval: top-k + metadata filters + hybrid search (keyword + vector) when needed
- Reranking: improve relevance; trade accuracy vs latency; deterministic tie-breaks
- Generation: grounding instructions, citations/provenance, refusal behavior
- Evaluation: offline (precision@k, MRR) + online (answer acceptance, deflection), and hallucination proxies
- Operations: caching, rate limits, retries, monitoring, and incident playbooks
- Security/privacy: PII handling, access control, logging policies, retention, and model/provider boundaries

## Sources (role signals used to tune this plan)
This plan emphasizes APIs, Python, customer-facing solution building, and governance based on themes in the sample postings you shared.
- Nimble - Senior Solution Consultant (APIs, Python workflows, technical demos/POCs, data ecosystems)
- WRITER - Customer AI architect (custom solutions, APIs, knowledge graph capabilities)
- Technical Program Product Manager III (data governance/privacy/security, APIs, cloud technologies)