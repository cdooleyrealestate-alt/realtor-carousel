# Audio timing and caption alignment
## Shot feasibility
For T seconds, feasible integer count satisfies ceil(T/5) ≤ n ≤ floor(T/3). Choose count near T/4 within this interval. If interval empty, explain incompatibility and ask to change duration/rule. Use total video duration including any authorized silent holds, not just speaking time.
Distribute durations around phrase boundaries, all within [3,5], sum exactly T. Rebalance remainder instead of adding a sub-3-second closing shot. No timeline gaps. Voice continues across shots. If transitions overlap, visible intervals must still meet rule; default hard cuts simplify this.
A storyboard estimated at 60 seconds must be rebuilt if actual narration is 47.2 seconds. Never stretch narration silently to fit draft.
Clip length and visual-shot length differ: generated clip can be longer and trimmed. Use alternate angles/details for additional shots, respecting script meaning.

## Word alignment
Prefer actual TTS word timepoints; otherwise transcribe/force-align final audio using supported tools. Compare transcript to exact script. Detect omissions/insertions before writing subtitle timing. For each word record text, start, end, confidence/source where available. Bound timestamps to audio, monotonically ordered, positive durations. Genuine spoken overlaps must be handled deliberately; do not force arbitrary duration estimates.
Include breaths/silence in timeline without inventing spoken captions. Hold phrase briefly if readability needs it, but active highlight must track actual word interval; no next-word highlight in silence.
Group phrases by semantics/readability. Keep complete words within frame; avoid orphan punctuation and excessive lines. Captions need not reset at every shot cut.
Store alignment status: Estimated / Audio aligned / Human checked. If only audio duration is known, shot timing can be finalized but word captions still pending alignment.
Word-aligned JSON or native editor caption data may carry per-word timings; only output concrete file formats that the selected app supports. ASS/karaoke instructions require verified editor compatibility, not universal claims.

## Accessibility versus visual overlay
SRT/VTT typically provide timed text cues for accessibility; standard SRT cannot define per-word colour. Burned-in highlighting requires app-native word highlight styling, an appropriate supported animated subtitle format or a rendering step.
Provide plain caption transcript even when timing cannot be computed. An estimated SRT must be labelled draft, never ready-to-publish aligned captions. For import/export explain what metadata will survive.
Final QC: replay opening, middle, closing and names/numbers at normal speed; review full video before publication. If file is unavailable provide instructions, not a fabricated pass.

