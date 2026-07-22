You are evaluating a completed Autonomous Integration Lab run.

Read these files:
- evaluators/scorecard-rubric.md
- evaluators/dx-issue-taxonomy.md
- runs/{{RUN_ID}}/manifest.json
- runs/{{RUN_ID}}/findings.md
- runs/{{RUN_ID}}/logs/run.log

If present, also inspect:
- runs/{{RUN_ID}}/transcript.ndjson
- runs/{{RUN_ID}}/app/README.md
- runs/{{RUN_ID}}/source-manifest.md

Your task:
1. Assign rubric scores (0–3) for all six categories per scorecard-rubric.md
2. Classify every issue by dx-issue-taxonomy.md bucket and severity
3. Count human interventions from manifest.json or transcript evidence
4. Determine whether the run is replayable (all required fields present, versions pinned)
5. Produce a JSON object that matches evaluators/scorecard.schema.json exactly

Rules:
- Do not soften findings. Friction is evidence, not criticism.
- Do not infer success without a log line or API response confirming it.
- If evidence is incomplete or ambiguous, set confidence to "medium" or "low" and explain in notes.
- Every issue in the issues array must have a bucket from dx-issue-taxonomy.md.
- The status field must be "success", "partial", or "failed" — nothing else.

Output only the JSON object, no prose, no markdown code fences.
