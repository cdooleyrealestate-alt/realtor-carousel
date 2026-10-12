---
name: storyboard-faceless-reels
description: Create app-adapted production instructions for clean professional 9:16 faceless reels or stories from creator scripts. Ask which AI/editor app and narration voice they use; plan 3–5-second image/video shots, verbatim captions, spoken-word highlighting and audio-based timing revisions. Use for consulting clients and individual creators.
---

# Faceless Reel Storyboard

Deliver an executable production instruction set, not a claim that a video was rendered. Use the creator's chosen AI/editor app and supplied script. Use images or B-roll, captions and audio narration; no talking-head or visible avatar. A voice avatar means narration identity, not an on-screen person.

Read references/production.md for output templates, visual style and app adaptation. Read references/timing-captions.md before timing, caption or narration tasks. Read references/acceptance.md for checks.

## Efficient intake
Use provided answers and ask at most three focused questions in each round. First ask:
1. "Which AI app or editor will you use? Tell me the name and version if known."
2. "Paste or attach your script. Is it final or may I tighten it?"
3. "For narration, will you use your own authorized voice clone, an AI preset, or a newly designed AI voice?"
If script/app/voice already supplied, do not repeat.
Next ask only unresolved production-critical details: reel or story target platform, intended duration, language/accent, target audience/goal/CTA, brand styling. Infer from script where clear; state defaults. Do not ask a long questionnaire.
Default: 9:16, 1080×1920 planned export, professional photographic imagery, simple captions, one restrained accent colour, no music unless requested. Use creator's own market/brand; no author account defaults.
If own clone: ask whether it exists and which service/profile. For new clone follow chosen app's authorized setup; request only necessary creator-owned audio using secure supported flow. Never request passwords/tokens in chat. Never imply an LLM can identify or access their clone without a connection.
If preset: ask voice preferences or offer 2–3 broad styles; verify actual available voice names in selected app before naming one.
If newly designed: request accent/language, pace, energy and tone; describe an original voice rather than impersonating someone.
Require creator-owned or authorized voice. Explain that voice creation/clone quality may depend on app plan/verification and supplied audio only when applicable. Do not promise exact clone fidelity.
If no script, request it; outline setup but do not invent approved narration. Offer script help if requested. Preserve final supplied wording; suggest edits separately and apply only authorized edits.

## App capability check
Treat app knowledge as provisional. Verify current official documentation/tool capabilities before giving exact UI steps, feature/plan availability or technical formats. Prefer connected tools and primary sources. Ask version or inspect when uncertain.
Evaluate script/voice generation, word alignment, per-word caption highlighting, image/video import, timing, export, and audio duration controls. Separate model prompt capability from editor capability.
If one app cannot do everything, name the missing feature and offer a minimal supported second step/editor. Never claim prompt text alone forces captions, voice cloning or timeline edits. Do not silently substitute providers.
Output neutral instructions when exact features cannot be verified; mark capability unknown.
This plugin has no built-in renderer/voice service or unattended background loop. Operate in stages when creator returns narration/timeline or exports. Use connected tools only if available and authorized.

## Script and audio first
Extract exact final narration, hook, main points, CTA, pronunciation notes and language. Do not fabricate claims/statistics. Resolve claim-sensitive content from creator sources; mark unverified claims for review rather than silently endorsing them.
Produce a draft based on estimated speech rate only when audio is unavailable, clearly label estimated timing. Ask for generated narration audio or reliable word timestamps to finalize.
Choose voice and generate/export narration in selected app using verified instructions. Keep an exact versioned narration script. If spoken wording changes, update narration/captions/storyboard together.
Use actual audio duration and word timestamps to recalculate shots and highlighted captions. Do not claim continuous live monitoring or automatic finished edits while creator works in an external app.

## Storyboard and strict pacing
Every visual shot, including opening and CTA, must last 3.000–5.000 seconds. Derive shot count from total narration/video duration, not the 10/20 counts of a different image plugin.
Use a feasible count n with 3n ≤ T ≤ 5n, then plan cuts at meaningful phrase/action beats. For example 30 seconds can use 8 shots averaging 3.75 seconds.
Allow narration and captions to continue across cuts; do not force sentences into single shots. A shot may use still-image pan/zoom or a video clip. Avoid padding by near-identical repeated visuals merely to hit count.
For mismatches split/merge shots or request alternative visuals; trim clip visuals, not speech. Preserve narration intelligibility and word sync. Only change speech rate within creator-approved natural limits, regenerate and re-align afterward.
A duration below 3 seconds or between 5 and 6 seconds cannot satisfy the rule: explain and ask to lengthen content/hold, or explicitly waive the rule. Never silently create a short final shot. A tiny remainder is redistributed across preceding shots.
Use cuts by default; no overlap transitions unless explicitly accounted for without violating visible-shot durations.
Create a numbered table: Shot ID | Start–End | Duration | Exact spoken excerpt | Image/B-roll concept | Prompt | Motion/Edit | Caption phrase | Notes. Label a spoken excerpt crossing shots as continuation; never omit words.
Image prompts: separate 9:16 composition, realistic setting, subject/action, natural light, shot angle, central safe area and exclusions. Video prompts additionally specify feasible action/camera movement and planned usable duration; generator output duration may require editor trimming.
Maintain same-home/person references where required; fictional education visuals must not masquerade as actual listing footage.

## Captions
Captions are mandatory and verbatim to final narration. Include punctuation/case, readable phrase groups, and per-word active highlighting synchronized to spoken words. Never call guessed timestamps aligned.
Distinguish burned-in visual word highlighting from selectable accessibility captions. Provide both instructions: highlighted overlay plus SRT/VTT accessibility track where supported. SRT alone cannot encode word colour animation.
Use exact word timestamps from supported TTS/alignment/transcription process; validate wording against narration and manually correct names, numbers and contractions. Do not invent timestamps if no audio/tool.
See timing-captions reference for overlaps, silence, formatting, safe areas and format compatibility.

## Delivery and revisions
Deliver one compact package:
1. Production brief and app capability summary.
2. Verbatim narration and chosen voice setup.
3. Complete storyboard with 3–5-second durations.
4. Per-scene image/video prompts.
5. Caption text/style plus estimated or verified timing status.
6. App-specific assembly/export instructions and QC checklist.
7. Missing inputs and next action.
Also provide a reusable paste-ready master prompt referencing this package, not a generic prompt replacing detailed scene instructions.
Avoid creating files unless requested/useful; if created persist through appropriate account/file workflow. Never claim rendered video, generated assets or aligned subtitle file when only instructions exist.
After draft ask "What needs improvement: imagery, pacing, voice, captions, tone or CTA?" Read existing answers before asking. Support scene edits, voice changes, script changes or whole storyboard revisions.
Version script/audio/captions/storyboard together. Preserve prior versions and creator selections; new script/audio invalidates old alignment. Do not overwrite finalized files without authorization.

