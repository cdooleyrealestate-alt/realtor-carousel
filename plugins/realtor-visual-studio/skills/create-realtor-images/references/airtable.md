# Airtable operations
Use the current creator's verified Creator Setup IDs and inspect fresh schema before mutations. No credentials are packaged. Require connected Airtable access.
Projects store script and brief; Batches store revision history and completion; Images store one output each. Project ID/Batch ID are text joins, not linked-record fields.
Use stable unique IDs: RSV-<project>, <project>-B01, <project>-S01-V01. Lookup Image ID before create to avoid duplicate retries. New creative revision always creates a new record; upload retry may update existing pending record.
Discover current read/create/update and attachment schemas. Resolve field IDs; write supported select values, use option IDs for filters where required. Batch writes up to current tool limit, default 10. Inspect every per-record result; retry only failed rows.
Attachment transfer: discover direct file upload or supported URL operation. Never send sandbox paths, data URLs, Library IDs or opaque generation handles as fetchable URLs. Signed URLs must last through ingestion; do not expose them to the user/logs. Read back attachment presence/ID/name/thumbnail. If unsupported mark Upload failed and explain what export/connection is needed. Never pretend prompts constitute image delivery.
States: Planned → Generated → Ready for review → Selected/Rejected/Revision requested; upload failure → Upload failed. Batch remains Partial until N usable attachments verified. Review is not final approval.
Selected checkbox is creator choice; Status records workflow. Selected plus Revision requested means preserve selected original and add a new alternative. Never clear selections or select replacement without instruction.
Optional manual Gallery setup: Images → add Gallery view → Image as cover. Show Scene Number, Script Excerpt, Selected, Status, Improvement Notes. Filter by Project ID/Batch ID; useful views Ready for review, Selected, Revision requested. Do not claim UI changes were made by tools if unavailable.
No notifications, polling or external automations are configured. On each revision invocation read fresh notes before generating.


