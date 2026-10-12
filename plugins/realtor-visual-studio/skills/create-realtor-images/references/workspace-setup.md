# Creator onboarding and workspace adapters

## First use
Introduce a guided setup: "Where would you like to review your images—Airtable, Notion or Google Sheets? Should I create a new workspace or connect one you already use?"
Ask in short rounds, maximum three questions at once:
1. Destination and new/existing.
2. Existing URL or choose from verified accessible accounts/workspaces/parent folders. For new Notion ask parent page; Airtable choose workspace; Sheets choose Drive folder.
3. Creator/brand name and market; collect visual preferences only when needed.
Show recommendation: Airtable visual review; Notion content/project hub; Sheets familiar simple list. Never force provider or create all three.
The creator's request to set up is authority to create their requested structures. Do not ask redundant permission. Do not guess among ambiguous accounts/parents.

Discover connected tools at runtime. Read platform skill if available. If missing, explain connection requirement and help through available plugin connection guidance. No connection means no claimed live setup; continue script planning if possible. Notion is conditional on an installed connector capable of required operations; do not imply it is bundled or connected. Do not ask users to paste secrets into chat.
Resolve actual destination IDs from returned metadata, never derive them from names. Preserve existing unrelated fields/data and sharing. Do not invite third parties. If an existing destination lacks fields, add missing compatible fields rather than rebuild/delete.
Verify final structures by reading them back, save Creator Setup, then supply verified link. No private author IDs or personal defaults are distributed.

## Common logical data model
Creator Setup: Creator ID, Creator/Brand Name, Market, Platform, Destination URL/ID, Structure IDs, Field Mapping, Aspect defaults, Brand Brief, People preference, Exclusions, Setup Status, Last verified.
Projects: Project ID, Project Name, Script, Short/Long, Platform, Audience, Aspect Ratio, Visual Brief, Target Count, Status, Current Batch ID.
Batches: Batch ID, Project ID, Version, Parent Batch ID, Revision Brief, Expected Count, Completed Count, Status, Failure Notes.
Images: Image ID, Project ID, Batch ID, Scene Number, Version, Replaces Image ID, Script Excerpt, Suggested Timing, Scene Purpose, Prompt, Asset, Alt Text, Disclosure, Actual Dimensions, QA Notes, Selected, Status, Rating, Improvement Notes.
Statuses: Planned, Generating, Partial, Ready for review, Selected, Revision requested, Rejected, Approved, Upload failed. Map platform-native compatible types.
Use stable text IDs for joins if relational fields are unavailable. Preserve revisions as new rows/pages/records.

## Airtable
Create a base named "<Brand> — Realtor Visual Studio" in the creator's chosen accessible workspace, or add structures to existing base. Tables: Creator Setup, Projects, Batches, Images.
Use Image attachment field, Selected checkbox, Status single select, Rating integer, text feedback/prompts, count/scene/version numbers. Discover supported create-base/table/field operations and exact schemas. Read Airtable skill. Native attachments require verified supported upload transport; URLs must be accessible for ingestion.
Create Gallery view when supported; otherwise explain optional one-time UI setup using Image cover. Maintain grid selection until gallery available. Never reuse author base IDs.

## Notion
Within selected parent page, create "<Brand> — Realtor Visual Studio". Use Creator Setup page, Projects/Batches/Images databases where supported. Images database uses Files & media asset, Selected checkbox, Status select, Improvement Notes rich text, scene/version numbers and IDs. Put longer script and prompt in page body if property limits require it. Gallery should use uploaded/external accessible image as preview.
Discover database/data-source/page creation and upload operations; use actual returned IDs and current schemas. If only page operations exist, create project pages with scene subpages, explicit Selected/Status/Improvement sections and image blocks; report reduced functionality, never claim database/gallery was created.
If no Notion tools exist, explain connection needed. Offer a different supported platform only as a choice, not silent substitution.

## Google Sheets
Use connected Google Drive/Sheets and registered Spreadsheets skill. Follow current skill's mandated creation/import workflow. Tabs: Creator Setup, Projects, Batches, Images. Freeze header rows, wrap excerpts/notes, use status dropdowns and Selected checkboxes where supported. Keep scene rows easy to scan; readable column widths.
Store durable Image URL and clickable Open Image link. An optional thumbnail formula may be used only if URL is supported and accessible; do not claim a formula embeds an uploaded original. Keep Drive originals accessible to authorized creator without making them public. Private Drive links may not render through IMAGE; use working clickable file link and report thumbnail limitation. Do not expose signed URLs as permanent references or store images as base64 in cells.
Record file IDs/URLs alongside scene metadata; verify links and updated cells. Do not upload/change sharing automatically to make thumbnails public.
Use native Google Sheet output, not an Excel file falsely labelled Sheets.

## Guided creator prompts
Store a Setup Checklist section with actionable steps and status:
- Choose destination / connect account.
- Set creator/market/brand preferences.
- Paste script; select short or long; set aspect ratio.
- Generate 10 or 20 individual scenes.
- Review assets; select favourites.
- Enter what needs improvement.
- Return to plugin with "Read my selections and revise."
At end of setup prompt for script and format. At review ask which assets to keep and what needs to improve. Per-asset notes should say: "What should change? What should stay the same?"
Prompts are visible fields/instructions, not push notifications. Files cannot message the creator independently. Chat-invoked checks are supported; notifications/polling need a separately configured automation. Do not promise background operation.

