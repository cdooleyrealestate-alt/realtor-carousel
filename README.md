# realtor-carousel

Tools, skills and plugins for creating real estate social-media visuals.

## Realtor Visual Studio

Source: [plugins/realtor-visual-studio](plugins/realtor-visual-studio)

Version 1.1.0 is a ChatGPT skills-based plugin that:
- Reads supplied video scripts and plans matching visual scenes.
- Creates 10 separate images for short-form or 20 for long-form videos with available ChatGPT image-generation tools.
- Guides each creator through setting up Airtable, Notion or Google Sheets for review.
- Tracks favourites, improvement notes and versioned revisions.
- Supports consistent same-home renovation and landscaping comparisons.

### Use
Invoke the installed plugin and say:
"Set up Realtor Visual Studio for my business using Airtable."
Or choose Notion or Google Sheets. Connect the chosen service, select a new or existing destination, then provide your script and short/long format. Review delivered assets and return with "Read my selections and revise."

This repository contains workflow instructions, not a standalone image-generation server. Each creator needs ChatGPT image creation and compatible tools for their chosen review platform. Attachment transfer depends on supported file export/upload. Notion requires a compatible connector. There is no background polling, publishing or notification service. Full image-to-workspace delivery remains to be tested with an actual script.

### Package
From repository root:
```bash
python3 scripts/package_plugin.py
```
This produces `dist/realtor-visual-studio-1.1.0.zip` containing one plugin directory. The archive can be used in a supported private plugin import flow; storing source on GitHub does not install or publish it in ChatGPT.

No creator-specific account IDs or credentials are included. Each user's destination configuration belongs in their own review workspace.
